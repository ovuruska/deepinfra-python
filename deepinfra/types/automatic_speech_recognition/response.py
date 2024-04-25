from typing import List

from deepinfra.types.common.inference_status import InferenceStatus


class AutomaticSpeechRecognitionWord:
	text: str
	start: int
	end: int
	confidence: float

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

class AutomaticSpeechRecognitionResponse:
	text: str
	segments: List[AutomaticSpeechRecognitionSegment]
	language: str
	input_length_ms: int
	request_id: str
	inference_status: InferenceStatus

