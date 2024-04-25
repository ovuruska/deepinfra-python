"""
import {ReadStreamInput} from "@/lib/utils/read-stream";

export interface AutomaticSpeechRecognitionRequest {
  audio: ReadStreamInput;
  task?: "transcribe" | "translate";
  language?: string;
  temperature?: number;
  patience?: number;
  suppress_tokens?: string;
  initial_prompt?: string;
  condition_on_previous_text?: boolean;
  temperature_increment_on_fallback?: number;
  compression_ratio_threshold?: number;
  logprob_threshold?: number;
  no_speech_threshold?: number;
  webhook?: string;
}

"""
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
