class GitHubRepoError(Exception):
    def __init__(self, status_code):
        if status_code == 403:
            message = "Rate limit exceeded"
        else:
            message = f"Status code was: {status_code}"

        super().__init__(message)