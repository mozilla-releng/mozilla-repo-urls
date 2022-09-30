import giturlparse

from mozilla_repo_urls.platforms import ADDITIONAL_PLATFORMS

from .errors import InvalidRepoUrlError, UnsupportedPlatformError
from .result import RepoUrlParsed

for i, platform in enumerate(ADDITIONAL_PLATFORMS):
    giturlparse.platforms.PLATFORMS.insert(i, platform)


_SUPPORTED_PLATFORMS = ("hgmo", "github")


def parse(url_string):
    # Workaround for https://github.com/nephila/giturlparse/issues/43
    url_string = url_string.rstrip("/")
    parsed_info = giturlparse.parser.parse(url_string)
    parsed_url = RepoUrlParsed(parsed_info)

    if not parsed_url.valid:
        raise InvalidRepoUrlError(url_string)

    if parsed_url.platform not in _SUPPORTED_PLATFORMS:
        """
        For error reporting purposes, the exception object includes the domain
        for each supported platform.
        """
        raise UnsupportedPlatformError(url_string, parsed_url.host,
                                       [domain
                                        for domains in
                                          [platform[1].DOMAINS
                                           for platform in giturlparse.platforms.PLATFORMS
                                           if platform[0] in _SUPPORTED_PLATFORMS]
                                        for domain in domains])
    return parsed_url
