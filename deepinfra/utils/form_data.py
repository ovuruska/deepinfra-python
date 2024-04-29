from typing import List, Optional

from requests_toolbelt import MultipartEncoder

from deepinfra.utils.read_stream import ReadStreamUtils


class FormDataUtils:
    """
    Utilities for creating form data.

    """

    @staticmethod
    def get_form_data(data, blob_keys: Optional[List[str]] = None):
        """
        Creates a MultipartEncoder object from the data.
        :param data:
        :param blob_keys:
        :return:
        """
        if blob_keys is None:
            blob_keys = list()
        body = {}

        for key, value in data.items():
            if key in blob_keys:
                body[key] = (key, ReadStreamUtils.get_read_stream(value))
            else:
                body[key] = value

        return MultipartEncoder(fields=body)
