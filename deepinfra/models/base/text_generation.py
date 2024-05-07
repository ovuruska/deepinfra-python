"""
    This module contains the TextGeneration class,
    which is the base class for all text generation models.
"""

import json
from typing import Union

from deepinfra.models.base import BaseModel
from deepinfra.types.text_generation.request import TextGenerationRequest
from deepinfra.types.text_generation.response import TextGenerationResponse


class TextGeneration(BaseModel) -> TextGenerationResponse:
    """
    Initializes one of the DeepInfra text generation models.
    @docs Check the available models at https://deepinfra.com/models/text-generation
    """

    def generate(self, body: dict):
        """
        Generates text.
        :param body:
        :return:
        """
        response = self.client.post(json.dumps(body))
        return TextGenerationResponse(**response.json())
