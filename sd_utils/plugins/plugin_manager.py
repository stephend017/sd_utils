from sd_utils.plugins.plugin_base import PluginBase
from typing import Any, ClassVar, final


class PluginManager:
    def __init__(self):
        self._plugins = {}

    @final
    def register(self, name: str, **kwargs):
        """
        decorator for registering a plugin to this instance of a
        plugin manager
        """

        def decorator(plugin: ClassVar[PluginBase]):
            if name in self._plugins:
                raise ValueError(f"Plugin with name [{name}] already exists")

            class Wrapper:
                def __init__(self, plugin):
                    self.name = name
                    self.plugin = plugin

            w = Wrapper(plugin(**kwargs))

            self._plugins[name] = w
            w.plugin.on_register()

            return w

        return decorator

    @final
    def run(
        self, name: str, on_search_params: dict = {}, on_find_params: dict = {}
    ):
        """
        runs a given plugin.

        Note: this function

        Args:
            name (str): the name of the plugin to run
            on_search_params (dict): parameters to pass to
                the get_on_search_params function
        """

        to_run = None
        for plugin_name, wrapper in self._plugins.items():
            if name == plugin_name:
                to_run = wrapper
            try:
                wrapper.plugin.on_search(
                    self.get_on_search_params(name, **on_search_params)
                )
            except NotImplementedError:
                # just skip if its not implemented
                pass

        if to_run is None:
            raise ValueError(f"Unable to find plugin with name [{name}]")

        to_run.plugin.on_find(self.get_on_find_params(name, **on_find_params))

    def get_on_search_params(self, name: str, **kwargs) -> Any:
        """
        function that generates parameters for the on
        search function of a plugin given its name
        """
        return kwargs

    def get_on_find_params(self, name: str, **kwargs) -> Any:
        """
        function that generates parameters for the on
        find function of a plugin given its name
        """
        return kwargs
