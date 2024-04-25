import time
import requests

from deepinfra.exceptions import MaxRetriesExceededError
from deepinfra.constants import MAX_RETRIES, USER_AGENT, INITIAL_BACKOFF, SUBSEQUENT_BACKOFF


class DeepInfraClient:
	max_retries = MAX_RETRIES
	initial_backoff = INITIAL_BACKOFF
	subsequent_backoff = SUBSEQUENT_BACKOFF


	def __init__(self, url, auth_token):
		self.url = url
		self.auth_token = auth_token


	def backoff_delay(self, attempt):
		delay = self.initial_backoff if attempt == 1 else self.subsequent_backoff
		time.sleep(delay)


	def post(self, data, config=None):
		if config is None:
			config = {}
		config_headers = config.get('headers', {})
		headers = {'content-type': 'application/json', **config_headers, 'User-Agent': USER_AGENT,  'Authorization': f'Bearer {self.auth_token}'}
		for attempt in range(self.max_retries + 1):
			try:
				response = requests.post(self.url, data=data, headers=headers)
				response.raise_for_status()
				return response
			except requests.RequestException as error:
				if attempt < self.max_retries:
					print(f'Request failed, retrying... Attempt {attempt + 1}/{self.max_retries}')
					self.backoff_delay(attempt + 1)
				else:
					raise error

		raise MaxRetriesExceededError()
