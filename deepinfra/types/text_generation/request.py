from dataclasses import dataclass, field
from typing import Optional, List, Dict

@dataclass
class TextGenerationRequest:
    input: str
    stream: Optional[bool] = None
    max_new_tokens: Optional[int] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None
    top_k: Optional[int] = None
    repetition_penalty: Optional[float] = None
    stop: Optional[List[str]] = None
    num_responses: Optional[int] = None
    response_format: Optional[Dict[str, str]] = None
    presence_penalty: Optional[float] = None
    frequency_penalty: Optional[float] = None
    webhook: Optional[str] = None