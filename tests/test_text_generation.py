import unittest
from unittest.mock import patch

from deepinfra.models.base.text_generation import TextGeneration

model_name = "mistralai/Mistral-7B-Instruct-v0.2"
api_key = "API KEY"


class TestTextGeneration(unittest.TestCase):
    @patch("requests.post")
    def test_generate(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"text": "Hello, World!"}

        text_generation = TextGeneration(model_name, api_key)
        body = {"text": "Hello, World!"}
        response = text_generation.generate(body)

        called_args, called_kwargs = mock_post.call_args
        url = called_args[0]
        header = called_kwargs["headers"]
        self.assertEqual(url, f"https://api.deepinfra.com/v1/inference/{model_name}")

        self.assertEqual(response["text"], "Hello, World!")
        self.assertEqual(header["Authorization"], f"Bearer {api_key}")
