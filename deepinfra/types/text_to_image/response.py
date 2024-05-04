from dataclasses import dataclass
from typing import Optional, List, Dict

from deepinfra.types.common.inference_status import InferenceStatus


@dataclass
class Metrics:
    predict_time: int


@dataclass
class TextToImageResponse:
    request_id: str
    inference_status: InferenceStatus
    images: List[str]
    nsfw_content_detected: bool
    seed: str
    version: Optional[str] = None
    created_at: Optional[str] = None
    error: Optional[str] = None
    webhook: Optional[str] = None
