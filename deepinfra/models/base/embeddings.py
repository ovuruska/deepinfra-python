from deepinfra.models.base import BaseModel
from deepinfra.types.embeddings.request import EmbeddingsRequest
from deepinfra.types.embeddings.response import EmbeddingsResponse


class Embeddings(BaseModel):
    """
    @docs Check the available models at https://deepinfra.com/models/embeddings
    """

    def __init__(self, endpoint: str, auth_token: str):
        """
        Initializes the embeddings model.
        @param endpoint: The endpoint of the model or the model name.
        @param auth_token: The API key to authenticate the requests.
        """
        super().__init__(endpoint, auth_token)

    def generate(self, body: EmbeddingsRequest) -> EmbeddingsResponse:
        """
        Generates embeddings.
        :param body:
        :return:
        """
        response = self.client.post(body)
        return response
