import json

from requests_toolbelt import MultipartEncoder

from deepinfra.utils.read_stream import ReadStreamUtils


class FormDataUtils:
	@staticmethod
	def get_form_data(data, blob_keys=()):

		body = {}

		for key, value in data.items():
			if key in blob_keys:
				body[key] = (key,ReadStreamUtils.get_read_stream(value))
			else:
				body[key] = json.dumps(value)

		return MultipartEncoder(fields=body)
