from typing import List

from dataclasses import dataclass

from deepinfra.types.common.inference_status import InferenceStatus


@dataclass(kw_only=True)
class AutomaticSpeechRecognitionWord:
	text: str
	start: int
	end: int
	confidence: float

@dataclass(kw_only=True)
class AutomaticSpeechRecognitionSegment:
	id: int
	seek: int
	start: int
	end: int
	text: str
	tokens: List[int]
	temperature: float
	avg_logprob: float
	compression_ratio: float
	no_speech_prob: float
	confidence: float
	words: List[AutomaticSpeechRecognitionWord]

@dataclass(kw_only=True)
class AutomaticSpeechRecognitionResponse:
	text: str
	segments: List[AutomaticSpeechRecognitionSegment]
	language: str
	input_length_ms: int
	request_id: str
	inference_status: InferenceStatus

