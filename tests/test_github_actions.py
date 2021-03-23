from sd_utils.github_actions.action import GithubAction


def test_action():
    """
    """
    environ = {
        "INPUT_GITHUB_TOKEN": "mytoken",
        "INPUT_CONFIG_FILE": "myfile",
        "GITHUB_REPOSITORY": "myrepo",
    }

    my_action = GithubAction(
        "stephend017",
        "pencil-pusher",
        environ,
        required_builtins={"repository"},
    )

    t_b = my_action.builtins["repository"]
    t_i = my_action.inputs["github_token"]

    assert t_b == "myrepo"
    assert t_i == "mytoken"
