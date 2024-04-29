"""
    This module contains the TextGeneration class,
    which is the base class for all text generation models.
"""
from deepinfra.models.base import BaseModel
from deepinfra.types.text_generation.request import TextGenerationRequest
from deepinfra.types.text_generation.response import TextGenerationResponse


class TextGeneration(BaseModel):
    """
    Initializes one of the DeepInfra text generation models.
    @docs Check the available models at https://deepinfra.com/models/text-generation
    """

    def __init__(self, endpoint: str, auth_token: str):
        """
        Initializes the text generation model.
        :param endpoint:
        :param auth_token:
        """
        super().__init__(endpoint, auth_token)

    def generate(self, body: TextGenerationRequest) -> TextGenerationResponse:
        """
        Generates text.
        :param body:
        :return:
        """
        response = self.client.post(body)
        return response
