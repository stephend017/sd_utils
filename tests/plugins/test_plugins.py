from . import mypluginmanager
import pytest


def test_registered():
    """
    Tests that a plugin is registered correctly by the system
    """

    assert (
        "registered" in mypluginmanager._plugins["myplugin"].plugin.operations
    )


def test_search_and_find():
    """
    Tests that a plugin is searched and found properly
    when the manager is run
    """

    mypluginmanager.run("myplugin")
    assert "searched" in mypluginmanager._plugins["myplugin"].plugin.operations
    assert "found" in mypluginmanager._plugins["myplugin"].plugin.operations

    mypluginmanager._plugins["myplugin"].plugin.operations.remove("searched")
    mypluginmanager._plugins["myplugin"].plugin.operations.remove("found")


def test_plugin_doesnt_exist():
    """
    Tests that an error is thrown when a plugin doesn't
    exist
    """
    with pytest.raises(ValueError):
        mypluginmanager.run("notmyplugin")

    mypluginmanager._plugins["myplugin"].plugin.operations.remove("searched")


def test_search_only():
    """
    Tests that only search is called when a
    different plugin is run
    """

    mypluginmanager.run("myotherplugin")
    assert "searched" in mypluginmanager._plugins["myplugin"].plugin.operations
    assert (
        "found" not in mypluginmanager._plugins["myplugin"].plugin.operations
    )

    mypluginmanager._plugins["myplugin"].plugin.operations.remove("searched")
