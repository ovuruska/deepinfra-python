from deepinfra.models.base.text_generation import TextGenerationBaseModel


class Mixtral(TextGenerationBaseModel):
	"""
	Wrapper for the Mixtral-8x7B-Instruct-v0.1 model.
	"""
	endpoint='https://api.deepinfra.com/v1/inference/mistralai/Mixtral-8x7B-Instruct-v0.1'

	def __init__(self, auth_token: str):
		super().__init__(Mixtral.endpoint, auth_token)