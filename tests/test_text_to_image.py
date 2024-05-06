import json
import unittest
from unittest.mock import patch

from deepinfra import TextToImage

model_name = "CompVis/stable-diffusion-v1-4"
api_key = "API KEY"


class TestTextToImage(unittest.TestCase):
    @patch("requests.post")
    def test_generate(self, mock_post):
        mock_post.return_value.status_code = 200
        images = ["image data"]

        mock_post.return_value.json.return_value = {
            "request_id": "123",
            "inference_status": None,
            "images": images,
            "nsfw_content_detected": False,
            "seed": "seed",
            "version": "1.0",
            "created_at": "2022-01-01",
        }

        text_to_image = TextToImage(model_name, api_key)
        body = {"text": "Hello, World!"}
        response = text_to_image.generate(body)

        called_args, called_kwargs = mock_post.call_args
        url = called_args[0]
        header = called_kwargs["headers"]
        data = called_kwargs["data"]
        self.assertEqual(url, f"https://api.deepinfra.com/v1/inference/{model_name}")

        self.assertEqual(response.images, images)
        self.assertEqual(header["Authorization"], f"Bearer {api_key}")
        self.assertEqual(data, json.dumps(body))
