from typing import Any
from sd_utils.plugins.plugin_base import PluginBase
from . import mypluginmanager


@mypluginmanager.register("myplugin")
class MyPlugin(PluginBase):
    """
    """

    def __init__(self, **kwargs):
        """
        """
        self.operations = []
        self.data = []

    def on_register(self):
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
        self.data.append(data)

    def on_find(self, data: Any = None):
        """
        runs when the manager specifically queries this plugin
        """
        self.operations.append("found")
        self.data.append(data)
        return data
