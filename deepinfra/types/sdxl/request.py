from dataclasses import dataclass

from deepinfra.types.text_to_image import TextToImageRequest


@dataclass
class SdxlRequest:
    input: TextToImageRequest
