# mozilla-repo-urls

Process Mozilla's repository URLs. The intent is to centralize URLs parsing.

## Running tests

1. `uv tool install tox --with tox-uv`
1. `uv tool run tox -e py39`

## Preparing a release

1. Change the version in pyproject.toml
1. Once the change is merged, `uv tool run hatch build`
1. ```
export VERSION=<version>
git tag -s ${VERSION} -m ${VERSION}
uv tool run twine upload dist/mozilla_repo_urls-${VERSION}.tar.gz dist/mozilla_repo_urls-${VERSION}-py3-none-any.whl
```
