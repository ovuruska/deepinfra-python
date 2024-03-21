from deepinfra.constants import MAX_RETRIES, USER_AGENT, INITIAL_BACKOFF, SUBSEQUENT_BACKOFF
import time
import requests

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


	def post(self, data, headers=None):
		if headers is None:
			headers = {}
		headers.update(
			{'Content-Type': 'application/json', 'Authorization': f'Bearer {self.auth_token}', 'User-Agent': USER_AGENT})

		for attempt in range(self.max_retries + 1):
			try:
				response = requests.post(self.url, json=data, headers=headers)
				response.raise_for_status()  # Will raise exception for 4xx/5xx errors
				return response
			except requests.RequestException as error:
				if attempt < self.max_retries:
					print(f'Request failed, retrying... Attempt {attempt + 1}/{self.max_retries}')
					self.backoff_delay(attempt + 1)
				else:
					raise error  # Re-throw error on last attempt

		raise Exception('Maximum retries exceeded')
