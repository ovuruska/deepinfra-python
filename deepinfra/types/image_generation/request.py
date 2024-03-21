from dataclasses import dataclass
from typing import Optional

@dataclass
class ImageGenerationRequest:
	prompt: str
	negative_prompt: Optional[str] = None
	image: Optional[str] = None
	mask: Optional[str] = None
	width: Optional[int] = None
	height: Optional[int] = None
	num_outputs: Optional[int] = None
	scheduler: Optional[str] = None
	num_inference_steps: Optional[int] = None
	guidance_scale: Optional[float] = None
	prompt_strength: Optional[float] = None
	seed: Optional[int] = None
	refine: Optional[str] = None
	high_noise_frac: Optional[float] = None
	refine_steps: Optional[int] = None
	apply_watermark: Optional[bool] = None