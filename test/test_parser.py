import pytest

import mozilla_repo_urls


@pytest.mark.parametrize(
    "url_string, expected",
    (
        (
            "https://hg.mozilla.org/mozilla-central",
            {
                "github": False,
                "groups": [],
                "hgmo": True,
                "host": "hg.mozilla.org",
                "name": "mozilla-central",
                "normalized": "https://hg.mozilla.org/mozilla-central",
                "path_raw": "",
                "path": "",
                "pathname": "/mozilla-central",
                "platform": "hgmo",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "mozilla-central",
                "repo_type": "hg",
                "resource": "hg.mozilla.org",
                "urls": {
                    "https": "https://hg.mozilla.org/mozilla-central",
                    "ssh": "ssh://hg.mozilla.org/mozilla-central",
                },
                "user": "",
                "valid": True,
            },
        ),
        (
            "https://hg.mozilla.org/releases/mozilla-beta",
            {
                "github": False,
                "groups": [],
                "hgmo": True,
                "host": "hg.mozilla.org",
                "name": "releases/mozilla-beta",
                "normalized": "https://hg.mozilla.org/releases/mozilla-beta",
                "path_raw": "",
                "path": "",
                "pathname": "/releases/mozilla-beta",
                "platform": "hgmo",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "releases/mozilla-beta",
                "repo_type": "hg",
                "resource": "hg.mozilla.org",
                "urls": {
                    "https": "https://hg.mozilla.org/releases/mozilla-beta",
                    "ssh": "ssh://hg.mozilla.org/releases/mozilla-beta",
                },
                "user": "",
                "valid": True,
            },
        ),
        (
            "https://hg.mozilla.org/releases/mozilla-release",
            {
                "github": False,
                "groups": [],
                "hgmo": True,
                "host": "hg.mozilla.org",
                "name": "releases/mozilla-release",
                "normalized": "https://hg.mozilla.org/releases/mozilla-release",
                "path_raw": "",
                "path": "",
                "pathname": "/releases/mozilla-release",
                "platform": "hgmo",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "releases/mozilla-release",
                "repo_type": "hg",
                "resource": "hg.mozilla.org",
                "urls": {
                    "https": "https://hg.mozilla.org/releases/mozilla-release",
                    "ssh": "ssh://hg.mozilla.org/releases/mozilla-release",
                },
                "user": "",
                "valid": True,
            },
        ),
        (
            "https://hg.mozilla.org/try",
            {
                "groups": [],
                "hgmo": True,
                "host": "hg.mozilla.org",
                "name": "try",
                "normalized": "https://hg.mozilla.org/try",
                "path_raw": "",
                "path": "",
                "pathname": "/try",
                "platform": "hgmo",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "try",
                "repo_type": "hg",
                "resource": "hg.mozilla.org",
                "urls": {
                    "https": "https://hg.mozilla.org/try",
                    "ssh": "ssh://hg.mozilla.org/try",
                },
                "user": "",
                "valid": True,
            },
        ),
        (
            "https://hg.mozilla.org/mozilla-central/raw-file/tip/taskcluster/ci/config.yml",  # noqa: E501
            {
                "groups": [],
                "hgmo": True,
                "host": "hg.mozilla.org",
                "name": "mozilla-central",
                "normalized": "https://hg.mozilla.org/mozilla-central/raw-file/tip/taskcluster/ci/config.yml",  # noqa: E501
                "path_raw": "/raw-file/tip/taskcluster/ci/config.yml",
                "path": "tip/taskcluster/ci/config.yml",
                "pathname": "/mozilla-central",
                "platform": "hgmo",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "mozilla-central",
                "repo_type": "hg",
                "resource": "hg.mozilla.org",
                "urls": {
                    "https": "https://hg.mozilla.org/mozilla-central/raw-file/tip/taskcluster/ci/config.yml",  # noqa: E501
                    "ssh": "ssh://hg.mozilla.org/mozilla-central",
                },
                "user": "",
                "valid": True,
            },
        ),
        (
            "https://hg.mozilla.org/mozilla-central/file/tip/taskcluster/ci/config.yml",  # noqa: E501
            {
                "github": False,
                "groups": [],
                "hgmo": True,
                "host": "hg.mozilla.org",
                "name": "mozilla-central",
                "normalized": "https://hg.mozilla.org/mozilla-central/file/tip/taskcluster/ci/config.yml",  # noqa: E501
                "path_raw": "/file/tip/taskcluster/ci/config.yml",
                "path": "tip/taskcluster/ci/config.yml",
                "pathname": "/mozilla-central",
                "platform": "hgmo",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "mozilla-central",
                "repo_type": "hg",
                "resource": "hg.mozilla.org",
                "urls": {
                    "https": "https://hg.mozilla.org/mozilla-central/file/tip/taskcluster/ci/config.yml",  # noqa: E501
                    "ssh": "ssh://hg.mozilla.org/mozilla-central",
                },
                "user": "",
                "valid": True,
            },
        ),
        (
            "https://github.com/mozilla-mobile/fenix",
            {
                "github": True,
                "groups": [],
                "hgmo": False,
                "host": "github.com",
                "name": "fenix",
                "normalized": "https://github.com/mozilla-mobile/fenix.git",
                "owner": "mozilla-mobile",
                "path_raw": "",
                "path": "",
                "pathname": "/mozilla-mobile/fenix",
                "platform": "github",
                "port": "",
                "protocol": "https",
                "protocols": ["https"],
                "repo": "fenix",
                "repo_type": "git",
                "resource": "github.com",
                "urls": {
                    "git": "git://github.com/mozilla-mobile/fenix.git",
                    "https": "https://github.com/mozilla-mobile/fenix.git",
                    "ssh": "git@github.com:mozilla-mobile/fenix.git",
                },
                "user": "git",
                "valid": True,
            },
        ),
    ),
)
def test_parse(url_string, expected):
    url_object = mozilla_repo_urls.parse(url_string)
    for attribute_name, expected_value in expected.items():
        actual_value = getattr(url_object, attribute_name)
        assert (
            actual_value == expected_value
        ), f"[{url_string}] Property '{attribute_name}' should be "
        f"'{expected_value}' but is '{actual_value}'"
