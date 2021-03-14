import os
from typing import List
from sd_utils.logger import create_logger


def test_create_logger():
    """
    Tests that creating a logger works correctly
    """
    MESSAGE = "THIS IS A TESTING MESSAGE"

    logger = create_logger(__file__)

    logger.info(MESSAGE)

    with open("tests/test_logger.py.log", "r") as fp:
        lines: List[str] = fp.readlines()
        contents: str = "\n".join(lines)

        assert MESSAGE in contents

    os.remove("tests/test_logger.py.log")
