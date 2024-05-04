import unittest
from unittest.mock import patch

from deepinfra import Embeddings

model_name = "BAAI/bge-large-en-v1.5"
api_key = "API KEY"


class TestEmbeddings(unittest.TestCase):
    @patch("requests.post")
    def test_generate(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "embeddings": [1, 2, 3],
            "input_tokens": 123,
            "inference_status": None,
        }

        embeddings = Embeddings(model_name, api_key)
        body = {"text": "Hello, World!"}
        response = embeddings.generate(body)

        called_args, called_kwargs = mock_post.call_args
        url = called_args[0]
        header = called_kwargs["headers"]
        body = called_kwargs["data"]

        self.assertEqual(url, f"https://api.deepinfra.com/v1/inference/{model_name}")
        self.assertEqual(body, '{"text": "Hello, World!"}')
        self.assertEqual(response.embeddings, [1, 2, 3])
        self.assertEqual(header["Authorization"], f"Bearer {api_key}")
