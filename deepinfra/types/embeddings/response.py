from dataclasses import dataclass
from typing import Optional, List


@dataclass(kw_only=True)
class EmbeddingStatus:
	status: str
	runtime_ms: int
	cost: float
	tokens_generated: int
	tokens_input: int

@dataclass(kw_only=True)
class EmbeddingsResponse:
	embeddings: List[List[float]]
	input_tokens: int
	inference_status: EmbeddingStatus
	request_id: Optional[str] = None
