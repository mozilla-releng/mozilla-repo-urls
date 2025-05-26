import pytest

from mozilla_repo_urls import parse


@pytest.mark.parametrize(
    "left,right,should_be_equal",
    (
        pytest.param(
            "https://github.com/mozilla/repo.git",
            parse("https://github.com/mozilla/repo.git"),
            True,
        ),
        pytest.param(
            "https://hg.mozilla.org/mozilla-central",
            parse("https://hg.mozilla.org/mozilla-central"),
            True,
        ),
        pytest.param(
            "https://github.com/mozilla/repo.git",
            parse("https://github.com/mozilla/repo2.git"),
            False,
        ),
        pytest.param(
            "https://github.com/mozilla/repo.git",
            parse("https://github.com/mozilla2/repo.git"),
            False,
        ),
        pytest.param(
            "https://hg.mozilla.org/mozilla-central",
            parse("https://github.com/mozilla/repo.git"),
            False,
        ),
        pytest.param(
            "https://hg.mozilla.org/mozilla-central",
            None,
            False,
        ),
        pytest.param(
            "https://hg.mozilla.org/mozilla-central",
            "https://hg.mozilla.org/mozilla-central",  # This is a str on purpose
            False,
        ),
        pytest.param(
            "https://hg.mozilla.org/mozilla-central",
            42,
            False,
        ),
    ),
)
def test_equality(left, right, should_be_equal):
    left = parse(left)

    if should_be_equal:
        assert left == right
    else:
        assert left != right
