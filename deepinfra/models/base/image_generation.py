from deepinfra.models.base.base import BaseModel


class ImageGenerationBaseModel(BaseModel):
	def __init__(self, endpoint: str, auth_token: str):
		super().__init__(endpoint, auth_token)
		self.endpoint = endpoint
		self.auth_token = auth_token

	def generate(self, input):
		body = {
			'input': input
		}
		try:
			response = self.client.post(body)
			return response
		except Exception as error:
			print('Error generating image:', error)
			raise error


