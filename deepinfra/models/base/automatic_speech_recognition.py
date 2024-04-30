"""
The automatic speech recognition model.
"""

from deepinfra.models.base import BaseModel
from deepinfra.types.automatic_speech_recognition.response import (
    AutomaticSpeechRecognitionResponse,
)
from deepinfra.utils.form_data import FormDataUtils


class AutomaticSpeechRecognition(BaseModel):
    """
    @docs Check the available models at https://deepinfra.com/models/automatic-speech-recognition
    """

    def generate(self, body):
        """
        Generates the automatic speech recognition response.
        @param body: The request body.
        @return: The response.

        """

        form_data = FormDataUtils.get_form_data(body, blob_keys=["audio"])
        response = self.client.post(
            form_data, {"headers": {"content-type": form_data.content_type}}
        )
        return response.json()
