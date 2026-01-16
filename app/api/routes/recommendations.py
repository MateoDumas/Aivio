from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user, get_db
from app.db.models import Recommendation
from app.ml.model import predict_scores


router = APIRouter()


class RecommendationRequest(BaseModel):
    item_ids: list[int]


class RecommendationItem(BaseModel):
    item_id: int
    score: float


class RecommendationResponse(BaseModel):
    user_id: int
    recommendations: list[RecommendationItem]


@router.post("/", response_model=RecommendationResponse)
async def recommend(
    payload: RecommendationRequest,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
) -> RecommendationResponse:
    scores = predict_scores(current_user.id, payload.item_ids)
    items = [
        RecommendationItem(item_id=item_id, score=score)
        for item_id, score in zip(payload.item_ids, scores)
    ]
    items.sort(key=lambda x: x.score, reverse=True)
    for item in items:
        db_rec = Recommendation(
            user_id=current_user.id,
            item_id=item.item_id,
            score=item.score,
        )
        db.add(db_rec)
    await db.commit()
    return RecommendationResponse(user_id=current_user.id, recommendations=items)

