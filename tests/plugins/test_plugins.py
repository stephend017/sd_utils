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

    mypluginmanager._plugins["myplugin"].plugin.operations.clear()


def test_plugin_doesnt_exist():
    """
    Tests that an error is thrown when a plugin doesn't
    exist
    """
    with pytest.raises(ValueError):
        mypluginmanager.run("notmyplugin")

    mypluginmanager._plugins["myplugin"].plugin.operations.clear()


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

    mypluginmanager._plugins["myplugin"].plugin.operations.clear()


def test_get_on_search_params():
    """
    Tests that get_on_search params properly takes in
    the correct arguments
    """

    mydata = {"data": "value"}
    mypluginmanager.run("myplugin", mydata)

    assert mydata in mypluginmanager._plugins["myplugin"].plugin.data

    mypluginmanager._plugins["myplugin"].plugin.data.clear()


def test_get_on_find_params():
    """
    Tests that get_on_search params properly takes in
    the correct arguments
    """

    mydata = {"data": "value"}
    mypluginmanager.run("myplugin", on_find_params=mydata)

    assert mydata in mypluginmanager._plugins["myplugin"].plugin.data

    mypluginmanager._plugins["myplugin"].plugin.data.clear()


def test_on_find_return_value():
    """
    Tests that get_on_search params properly takes in
    the correct arguments
    """

    mydata = {"data": "value"}
    response = mypluginmanager.run("myplugin", on_find_params=mydata)

    assert response == mydata

    mypluginmanager._plugins["myplugin"].plugin.data.clear()
