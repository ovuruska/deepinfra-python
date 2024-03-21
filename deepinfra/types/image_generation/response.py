from dataclasses import dataclass
from typing import Optional, List, Dict



@dataclass
class InferenceStatus:
    status: str
    runtime_ms: int
    cost: float
    tokens_generated: Optional[int] = None
    tokens_input: Optional[int] = None

@dataclass
class Metrics:
    predict_time: int

@dataclass
class ImageGenerationResponse:
    request_id: str
    inference_status: InferenceStatus
    input: Dict
    output: List[str]
    id: str
    started_at: str
    completed_at: str
    logs: str
    status: str
    metrics: Metrics
    webhook_events_filter: List[str]
    output_file_prefix: str
    version: Optional[str] = None
    created_at: Optional[str] = None
    error: Optional[str] = None
    webhook: Optional[str] = None
