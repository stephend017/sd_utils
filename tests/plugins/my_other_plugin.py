from typing import Any
from sd_utils.plugins.plugin_base import PluginBase
from . import mypluginmanager


@mypluginmanager.register("myotherplugin")
class MyOtherPlugin(PluginBase):
    """
    """

    def __init__(self, **kwargs):
        """
        """
        self.operations = []

    def on_register(self, data: Any = None):
        """
        runs when this plugin is registered with
        the plugin manager
        """
        self.operations.append("registered")

    def on_search(self, data: Any = None):
        """
        runs when the manager begins a query for
        any plugin.
        """
        self.operations.append("searched")

    def on_find(self, data: Any = None):
        """
        runs when the manager specifically queries this plugin
        """
        self.operations.append("found")
