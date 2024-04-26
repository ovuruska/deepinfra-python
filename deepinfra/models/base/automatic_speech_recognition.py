from deepinfra.models.base import BaseModel
from deepinfra.types.automatic_speech_recognition.response import (
    AutomaticSpeechRecognitionResponse,
)
from deepinfra.utils.form_data import FormDataUtils


class AutomaticSpeechRecognition(BaseModel):

    """
    Initializes the automatic speech recognition model.
    @param endpoint: The endpoint of the model or the model name.
    @param auth_token: The API key to authenticate the requests. If not provided, it will be fetched from the environment.
    @docs Check the available models at https://deepinfra.com/models/automatic-speech-recognition
    """

    def __init__(self, endpoint: str, auth_token: str = None):
        super().__init__(endpoint, auth_token)

    def generate(self, body) -> AutomaticSpeechRecognitionResponse:
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
