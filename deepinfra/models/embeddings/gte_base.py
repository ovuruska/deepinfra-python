from deepinfra.models.base.text_embedding import TextEmbeddingBaseModel


class GteBase(TextEmbeddingBaseModel):
	endpoint = 'https://api.deepinfra.com/v1/inference/thenlper/gte-base'

	def __init__(self, auth_token: str):
		super().__init__(GteBase.endpoint, auth_token)
