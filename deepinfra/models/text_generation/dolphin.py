from deepinfra.models.base.text_generation import TextGenerationBaseModel


class Dolphin(TextGenerationBaseModel):
	"""
	Wrapper for the dolphin-2.6-mixtral-8x7b model.
	"""
	endpoint='https://api.deepinfra.com/v1/inference/cognitivecomputations/dolphin-2.6-mixtral-8x7b'

	def __init__(self, auth_token: str):
		super().__init__(Dolphin.endpoint, auth_token)

