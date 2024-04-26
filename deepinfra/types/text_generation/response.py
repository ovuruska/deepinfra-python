from dataclasses import dataclass
from typing import List, Optional, Dict


@dataclass(kw_only=True)
class InferenceStatus:
    status: str
    runtime_ms: int
    cost: float
    tokens_generated: int


@dataclass(kw_only=True)
class GeneratedText:
    generated_text: str


@dataclass(kw_only=True)
class TextGenerationResponse:
    request_id: str
    inference_status: InferenceStatus
    results: List[GeneratedText]
    num_tokens: int
    num_input_tokens: int
