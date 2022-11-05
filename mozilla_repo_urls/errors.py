class RepoUrlsBaseError(Exception):
    pass


class InvalidRepoUrlError(RepoUrlsBaseError):
    def __init__(self, url_string) -> None:
        super().__init__(f"Could not parse URL: {url_string}")


class UnsupportedPlatformError(RepoUrlsBaseError):
    @property
    def supported_platforms(self):
        return list(self._supported_platforms)

    def __init__(self, url_string, platform, supported_platforms) -> None:
        self._supported_platforms = supported_platforms
        super().__init__(
            f"Unsupported version control host. Got: {host}. "
            f"Expected one of: {supported_platforms}. URL: {url_string}"
        )
