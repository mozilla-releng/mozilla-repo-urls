class RepoUrlsBaseError(Exception):
    pass


class InvalidRepoUrlError(RepoUrlsBaseError):
    def __init__(self, url_string) -> None:
        super().__init__(f"Could not parse URL: {url_string}")
