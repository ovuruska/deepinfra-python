from deepinfra.models.base.text_embedding import TextEmbeddingBaseModel


class GteLarge(TextEmbeddingBaseModel):
	endpoint = 'https://api.deepinfra.com/v1/inference/thenlper/gte-large'

	def __init__(self, auth_token: str):
		super().__init__(GteLarge.endpoint, auth_token)