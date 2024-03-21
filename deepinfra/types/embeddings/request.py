from dataclasses import dataclass
from typing import Optional, List

@dataclass
class EmbeddingsRequest:
	inputs: List[str]
	normalize: Optional[bool] = None
	image: Optional[str] = None
	webhook: Optional[str] = None