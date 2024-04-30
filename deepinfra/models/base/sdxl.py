import json

from black import Optional

from deepinfra import BaseModel
from deepinfra.constants import SDXL
from deepinfra.types.sdxl.request import SdxlRequest
from deepinfra.types.sdxl.response import SdxlResponse


class Sdxl(BaseModel):
    """
    Class for the SDXL model.
    @docs Check the model at https://deepinfra.com/stability-ai/sdxl/api
    """

    def __init__(self, api_token: Optional[str] = None):
        super().__init__(SDXL, api_token)

    def generate(self, body: dict) -> SdxlResponse:
        """
        Generates an image.
        :param input:
        :return:
        """
        response = self.client.post(json.dumps(body))
        return response.json()
