# redix_client/exceptions.py
class RedixAPIError(Exception):
    def __init__(self, status_code, message):
        super().__init__(f"Redix API Error {status_code}: {message}")
        self.status_code = status_code
        self.message = message