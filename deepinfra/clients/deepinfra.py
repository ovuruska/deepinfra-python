import json
import time
import requests

from deepinfra.constants import (
    MAX_RETRIES,
    USER_AGENT,
    INITIAL_BACKOFF,
    SUBSEQUENT_BACKOFF,
)


class DeepInfraClient:
    max_retries = MAX_RETRIES
    initial_backoff = INITIAL_BACKOFF
    subsequent_backoff = SUBSEQUENT_BACKOFF

    def __init__(self, url, auth_token):
        self.url = url
        self.auth_token = auth_token

    def post(self, data, config=None):
        """
        Performs a POST request.
        Config can be used to pass additional parameters to the request.
        :param data:
        :param config:
        :return:
        """
        if config is None:
            config = {}
        config_headers = config.get("headers", {})
        headers = {
            "content-type": "application/json",
            **config_headers,
            "User-Agent": USER_AGENT,
            "Authorization": f"Bearer {self.auth_token}",
        }
        try:
            response = requests.post(self.url, data=data, headers=headers)
            response.raise_for_status()
            return response
        except requests.RequestException as error:
            raise error
