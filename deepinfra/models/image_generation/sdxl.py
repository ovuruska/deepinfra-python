from deepinfra.models.base import ImageGenerationBaseModel


class Sdxl(ImageGenerationBaseModel):
	endpoint = 'https://api.deepinfra.com/v1/inference/stability-ai/sdxl'

	def __init__(self, auth_token: str):
		super().__init__(Sdxl.endpoint, auth_token)
