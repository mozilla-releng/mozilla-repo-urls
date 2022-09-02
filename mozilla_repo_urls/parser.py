import giturlparse

from .platforms import HG_PLATFORMS
from .result import GitUrlParsed, HgUrlParsed


def parse(url_string):
    # Workaround for https://github.com/nephila/giturlparse/issues/43
    url_string = url_string.rstrip("/")
    return (
        _parse_hg(url_string)
        if "hg.mozilla.org" in url_string
        else _parse_git(url_string)
    )


def _parse_hg(url_string):
    old_platforms = giturlparse.parser.PLATFORMS
    giturlparse.parser.PLATFORMS = HG_PLATFORMS
    parsed_info = giturlparse.parser.parse(url_string)
    url_object = HgUrlParsed(parsed_info)
    giturlparse.parser.PLATFORMS = old_platforms
    return url_object


def _parse_git(url_string):
    parsed_info = giturlparse.parser.parse(url_string)
    return GitUrlParsed(parsed_info)
