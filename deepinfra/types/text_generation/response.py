from dataclasses import dataclass
from typing import List, Optional

from deepinfra.types.common.inference_status import InferenceStatus


@dataclass
class GeneratedText:
    generated_text: str


@dataclass
class TextGenerationResponse:
    inference_status: InferenceStatus
    results: List[GeneratedText]
    num_tokens: int
    num_input_tokens: int
