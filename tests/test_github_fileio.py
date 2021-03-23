import os
from sd_utils.github.fileio import get_file


def test_github_fileio():
    """
    """

    content = get_file(
        "stephend017", "pencil-pusher", "action.yml", os.environ["GH_PAT"]
    )

    assert 'name: "pencil_pusher"' in content
