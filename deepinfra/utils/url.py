from urllib.parse import urlparse


class URLUtils:
    @staticmethod
    def is_valid_url(url):
        """
        Checks if a URL is valid.
        :param url: The URL to be checked.
        :return: True if the URL is valid, False otherwise.
        """
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False
