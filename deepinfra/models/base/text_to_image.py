from deepinfra.models.base import BaseModel


class TextToImage(BaseModel):
    """
    Initializes one of the DeepInfra image generation models.
    @docs Check the available models at https://deepinfra.com/models/text-to-image
    """

    def generate(self, input):
        """
        Generates an image.
        :param input:
        :return:
        """
        body = {"input": input}
        response = self.client.post(body)
        return response
