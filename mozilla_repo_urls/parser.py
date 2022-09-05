import giturlparse

from mozilla_repo_urls.platforms import ADDITIONAL_PLATFORMS

from .result import GitUrlParsed, HgUrlParsed

for i, platform in enumerate(ADDITIONAL_PLATFORMS):
    giturlparse.platforms.PLATFORMS.insert(i, platform)


def parse(url_string):
    # Workaround for https://github.com/nephila/giturlparse/issues/43
    url_string = url_string.rstrip("/")
    return (
        _parse_hg(url_string)
        if "hg.mozilla.org" in url_string
        else _parse_git(url_string)
    )


def _parse_hg(url_string):
    parsed_info = giturlparse.parser.parse(url_string)
    url_object = HgUrlParsed(parsed_info)
    return url_object


def _parse_git(url_string):
    parsed_info = giturlparse.parser.parse(url_string)
    return GitUrlParsed(parsed_info)
