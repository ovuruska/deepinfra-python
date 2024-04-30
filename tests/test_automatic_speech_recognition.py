import unittest
from unittest.mock import patch

from deepinfra import AutomaticSpeechRecognition

model_name = "openai/whisper-base"
api_key = "API KEY"


class TestAutomaticSpeechRecognition(unittest.TestCase):
    @patch("requests.post")
    def test_generate(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"text": "Hello, World!"}
        audio_data = b"audio data"
        asr = AutomaticSpeechRecognition(model_name, api_key)
        body = {"audio": audio_data}
        response = asr.generate(body)

        called_args, called_kwargs = mock_post.call_args
        url = called_args[0]
        self.assertEqual(url, f"https://api.deepinfra.com/v1/inference/{model_name}")

        called_headers = called_kwargs["headers"]
        self.assertEqual(called_headers["Authorization"], f"Bearer {api_key}")

        self.assertEqual(response["text"], "Hello, World!")
