class MaxRetriesExceededError(Exception):
    def __init__(self, message="Maximum retries exceeded"):
        super().__init__(message)
