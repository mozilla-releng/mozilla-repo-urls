import giturlparse

from .platforms import HG_PLATFORMS


class RepoUrlParsed(giturlparse.result.GitUrlParsed):
    @property
    def hgmo(self) -> bool:
        return self.platform == "hgmo"


class GitUrlParsed(RepoUrlParsed):
    repo_type = "git"


class HgUrlParsed(RepoUrlParsed):
    repo_type = "hg"

    def __init__(self, parsed_info) -> None:
        old_platforms = giturlparse.result.PLATFORMS
        giturlparse.result.PLATFORMS = HG_PLATFORMS
        super().__init__(parsed_info)
        giturlparse.result.PLATFORMS = old_platforms
