from deepinfra.clients import DeepInfraClient


class BaseModel:
    def __init__(self, endpoint, auth_token):
        self.endpoint = endpoint
        self.auth_token = auth_token
        self.client = DeepInfraClient(self.endpoint, self.auth_token)