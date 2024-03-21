from deepinfra.models.base import BaseModel
from deepinfra.types.text_generation.request import TextGenerationRequest
from deepinfra.types.text_generation.response import TextGenerationResponse


class TextGenerationBaseModel(BaseModel):
	def __init__(self, endpoint: str, auth_token: str):
		super().__init__(endpoint, auth_token)
		self.endpoint = endpoint
		self.auth_token = auth_token

	def generate(self, body: TextGenerationRequest) -> TextGenerationResponse:
		try:
			response = self.client.post(body)
			return response
		except Exception as error:
			print('Error generating text:', error)
			raise error