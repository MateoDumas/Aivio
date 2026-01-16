from typing import Sequence

import torch


class RecommendationModel(torch.nn.Module):
    def forward(self, user_ids: torch.Tensor, item_ids: torch.Tensor) -> torch.Tensor:
        scores = torch.rand(item_ids.shape[0])
        return scores


model = RecommendationModel()


def predict_scores(user_id: int, item_ids: Sequence[int]) -> list[float]:
    user_tensor = torch.tensor([user_id], dtype=torch.long)
    items_tensor = torch.tensor(list(item_ids), dtype=torch.long)
    with torch.no_grad():
        scores = model(user_tensor, items_tensor)
    return scores.tolist()

