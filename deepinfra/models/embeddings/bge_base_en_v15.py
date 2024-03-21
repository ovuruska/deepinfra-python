from deepinfra.models.base.text_embedding import TextEmbeddingBaseModel


class BgeBaseEnV15(TextEmbeddingBaseModel):
	endpoint = 'https://api.deepinfra.com/v1/inference/BAAI/bge-base-en-v1.5'

	def __init__(self, auth_token: str):
		super().__init__(BgeBaseEnV15.endpoint, auth_token)
