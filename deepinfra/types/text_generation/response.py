from dataclasses import dataclass
from typing import List

from deepinfra.types.common.inference_status import InferenceStatus


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
