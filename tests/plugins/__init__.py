from sd_utils.plugins.plugin_base import PluginBase
from sd_utils.plugins.plugin_collector import collect_plugins
from sd_utils.plugins.plugin_manager import PluginManager

mypluginmanager = PluginManager()

collect_plugins(__file__, __name__, PluginBase)
