"""
    Base class for all models.
"""
import os
from typing import Union

from deepinfra.clients import DeepInfraClient
from deepinfra.constants.client import ROOT_URL
from deepinfra.utils.url import URLUtils


class BaseModel:
    """
    Base class for all models
    @param endpoint: The endpoint of the model or the model name.
    @param auth_token: The API key to authenticate the requests.
    """

    def __init__(self, endpoint, auth_token: Union[str | None] = None):
        if URLUtils.is_valid_url(endpoint):
            self.endpoint = endpoint
        else:
            self.endpoint = ROOT_URL + endpoint
        self.auth_token = (
            auth_token
            or self._get_auth_token_from_env()
            or self._warn_about_missing_api_key()
        )
        self.client = DeepInfraClient(self.endpoint, self.auth_token)

    def _get_auth_token_from_env(self):
        """
        Fetches the API key from the environment.
        @return: The API key.
        """
        self.auth_token = os.getenv("DEEPINFRA_API_KEY")
        return self.auth_token

    def _warn_about_missing_api_key(self):
        """
        Warns the user about the missing API key.
        @return: An empty string.
        """
        if not self.auth_token:
            print(
                "Warning: No API key provided. "
                "Please provide an API key to authenticate your requests."
            )
        return ""
