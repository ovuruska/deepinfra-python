from deepinfra.models.base.text_embedding import TextEmbeddingBaseModel


class BgeLargeEnV15(TextEmbeddingBaseModel):
	endpoint = 'https://api.deepinfra.com/v1/inference/BAAI/bge-large-en-v1.5'

	def __init__(self, auth_token: str):
		super().__init__(BgeLargeEnV15.endpoint, auth_token)
