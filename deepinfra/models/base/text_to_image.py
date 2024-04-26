from deepinfra.models import BaseModel


class TextToImage(BaseModel):

    """
    Initializes one of the DeepInfra image generation models.
    @docs Check the available models at https://deepinfra.com/models/text-to-image
    """

    def __init__(self, endpoint: str, auth_token: str):
        """
        Initializes the image generation model.
        @param endpoint: The endpoint of the model or the model name.
        @param auth_token: The API key to authenticate the requests. If not provided, it will be fetched from the environment.
        """
        super().__init__(endpoint, auth_token)

    def generate(self, input):
        """
        Generates an image.
        :param input:
        :return:
        """
        body = {"input": input}
        response = self.client.post(body)
        return response
