import giturlparse

from mozilla_repo_urls.platforms import ADDITIONAL_PLATFORMS

from .result import RepoUrlParsed

for i, platform in enumerate(ADDITIONAL_PLATFORMS):
    giturlparse.platforms.PLATFORMS.insert(i, platform)


def parse(url_string):
    # Workaround for https://github.com/nephila/giturlparse/issues/43
    url_string = url_string.rstrip("/")
    parsed_info = giturlparse.parser.parse(url_string)
    return RepoUrlParsed(parsed_info)
