from typing import Sequence
import random

try:
    import torch
    
    class RecommendationModel(torch.nn.Module):
        def forward(self, user_ids: torch.Tensor, item_ids: torch.Tensor) -> torch.Tensor:
            scores = torch.rand(item_ids.shape[0])
            return scores

    model = RecommendationModel()
    HAS_TORCH = True

except ImportError:
    HAS_TORCH = False
    model = None


def predict_scores(user_id: int, item_ids: Sequence[int]) -> list[float]:
    if HAS_TORCH and model:
        user_tensor = torch.tensor([user_id], dtype=torch.long)
        items_tensor = torch.tensor(list(item_ids), dtype=torch.long)
        with torch.no_grad():
            scores = model(user_tensor, items_tensor)
        return scores.tolist()
    else:
        # Fallback for environments without PyTorch (e.g. Vercel Free Tier)
        return [random.random() for _ in item_ids]

