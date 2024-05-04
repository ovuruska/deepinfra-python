import json

from deepinfra.models.base import BaseModel
from deepinfra.types.text_to_image import TextToImageResponse


class TextToImage(BaseModel):
    """
    Initializes one of the DeepInfra image generation models.
    @docs Check the available models at https://deepinfra.com/models/text-to-image
    """

    def generate(self, input) -> TextToImageResponse:
        """
        Generates an image.
        :param input:
        :return:
        """
        body = {"input": input}
        response = self.client.post(json.dumps(input))
        return TextToImageResponse(**response.json())
