"""
This error is raised when the maximum number of retries is exceeded by DeepInfraClient.
"""
class MaxRetriesExceededError(Exception):
    def __init__(self, message="Maximum retries exceeded"):
        super().__init__(message)
