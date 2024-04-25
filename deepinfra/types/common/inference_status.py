from dataclasses import dataclass


@dataclass(kw_only=True)
class InferenceStatus:
	status: str
	runtime_ms: int
	cost: int
	tokens_generated: int
	tokens_input: int

@dataclass(kw_only=True)
class Status:
	UNKNOWN = "unknown"
	QUEUED = "queued"
	RUNNING = "running"
	SUCCEEDED = "succeeded"
	FAILED = "failed"
