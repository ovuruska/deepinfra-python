import json

from black import Optional

from deepinfra.models.base import BaseModel
from deepinfra.constants import SDXL


class Sdxl(BaseModel):
    """
    Class for the SDXL model.
    @docs Check the model at https://deepinfra.com/stability-ai/sdxl/api
    """

    def __init__(self, api_token: Optional[str] = None):
        super().__init__(SDXL, api_token)

    def generate(self, body: dict):
        """
        Generates an image.
        :param input:
        :return:
        """
        response = self.client.post(json.dumps(body))
        return response.json()
