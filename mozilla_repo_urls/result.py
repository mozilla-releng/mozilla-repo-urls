import giturlparse


class RepoUrlParsed(giturlparse.result.GitUrlParsed):
    @property
    def hgmo(self) -> bool:
        return self.platform == "hgmo"


class GitUrlParsed(RepoUrlParsed):
    repo_type = "git"


class HgUrlParsed(RepoUrlParsed):
    repo_type = "hg"
