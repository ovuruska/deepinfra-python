from deepinfra.models.base import BaseModel
from deepinfra.types.embeddings.request import EmbeddingsRequest
from deepinfra.types.embeddings.response import EmbeddingsResponse


class TextEmbeddingBaseModel(BaseModel):
	def __init__(self, endpoint: str, auth_token: str):
		super().__init__(endpoint, auth_token)
		self.endpoint = endpoint
		self.auth_token = auth_token

	def generate(self, body: EmbeddingsRequest) -> EmbeddingsResponse:
		try:
			response = self.client.post(body)
			return response
		except Exception as error:
			print('Error generating embeddings:', error)
			raise error
