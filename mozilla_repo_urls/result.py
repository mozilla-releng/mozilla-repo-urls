import giturlparse


class RepoUrlParsed(giturlparse.result.GitUrlParsed):
    @property
    def hgmo(self) -> bool:
        return self.platform == "hgmo"

    @property
    def repo_type(self) -> str:
        return "hg" if self.platform == "hgmo" else "git"

    @property
    def taskcluster_role_prefix(self) -> str:
        return f"repo:{self.host}{self.pathname}"
