import giturlparse

_DOT_GIT_SUFFIX = ".git"


class RepoUrlParsed(giturlparse.result.GitUrlParsed):
    @property
    def hgmo(self) -> bool:
        return self.platform == "hgmo"

    @property
    def repo_type(self) -> str:
        return "hg" if self.platform == "hgmo" else "git"

    @property
    def taskcluster_role_prefix(self) -> str:
        path_name = (
            self.pathname[: -len(_DOT_GIT_SUFFIX)]
            if self.pathname.endswith(_DOT_GIT_SUFFIX)
            else self.pathname
        )
        path_name = path_name if path_name.startswith("/") else f"/{path_name}"
        return f"repo:{self.host}{path_name}"
