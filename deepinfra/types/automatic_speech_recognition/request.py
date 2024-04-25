from dataclasses import dataclass
from typing import Optional


@dataclass
class AutomaticSpeechRecognitionRequest:
	audio: str
	task: Optional[str]
	language: Optional[str]
	temperature: Optional[float]
	patience: Optional[int]
	suppress_tokens: Optional[str]
	initial_prompt: Optional[str]
	condition_on_previous_text: Optional[bool]
	temperature_increment_on_fallback: Optional[float]
	compression_ratio_threshold: Optional[float]
	logprob_threshold: Optional[float]
	no_speech_threshold: Optional[float]
	webhook: Optional[str]
