from deepinfra.models.base import BaseModel
from deepinfra.types.embeddings.request import EmbeddingsRequest
from deepinfra.types.embeddings.response import EmbeddingsResponse


class Embeddings(BaseModel):
    """
    @docs Check the available models at https://deepinfra.com/models/embeddings
    """


    def generate(self, body: EmbeddingsRequest) -> EmbeddingsResponse:
        """
        Generates embeddings.
        :param body:
        :return:
        """
        response = self.client.post(body)
        return response
