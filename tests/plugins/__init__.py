from sd_utils.plugins.plugin_collector import collect_plugins
from sd_utils.plugins.plugin_manager import PluginManager

mypluginmanager = PluginManager()

__all__ = collect_plugins(__file__, __name__)
