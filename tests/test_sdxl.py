import unittest
from unittest.mock import patch

from deepinfra import TextToImage
from deepinfra.constants import SDXL
from deepinfra.models.base.sdxl import Sdxl

model_name = SDXL
api_key = "API KEY"


class TestSdxl(unittest.TestCase):
    @patch("requests.post")
    def test_generate(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"image": "image data"}

        text_to_image = Sdxl(api_key)
        body = {"input": {"prompt": "Hello, World!"}}
        response = text_to_image.generate(body)

        called_args, called_kwargs = mock_post.call_args
        url = called_args[0]
        header = called_kwargs["headers"]
        self.assertEqual(url, f"https://api.deepinfra.com/v1/inference/{model_name}")

        self.assertEqual(response["image"], "image data")
        self.assertEqual(header["Authorization"], f"Bearer {api_key}")
