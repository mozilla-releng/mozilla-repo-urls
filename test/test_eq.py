import pytest

from mozilla_repo_urls import parse


@pytest.mark.parametrize(
    "left,right,should_be_equal",
    (
        pytest.param(
            "https://github.com/mozilla/repo.git",
            "https://github.com/mozilla/repo.git",
            True,
        ),
        pytest.param(
            "https://hg.mozilla.org/mozilla-central",
            "https://hg.mozilla.org/mozilla-central",
            True,
        ),
        pytest.param(
            "https://github.com/mozilla/repo.git",
            "https://github.com/mozilla/repo2.git",
            False,
        ),
        pytest.param(
            "https://github.com/mozilla/repo.git",
            "https://github.com/mozilla2/repo.git",
            False,
        ),
        pytest.param(
            "https://hg.mozilla.org/mozilla-central",
            "https://github.com/mozilla/repo.git",
            False,
        ),
    ),
)
def test_equality(left, right, should_be_equal):
    left = parse(left)
    right = parse(right)

    if should_be_equal:
        assert left == right
    else:
        assert left != right
