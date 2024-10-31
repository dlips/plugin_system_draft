import os
import importlib.util
import sys
from plugin_system import PluginManager
import yaml


def main():
    # Load the plugins
    manager = PluginManager()

    print("Loaded plugins:")
    print([key for key in manager.plugins.keys()])

    with open('config.yaml', 'r') as file:
        data = yaml.safe_load(file)

    print(data)

    plgs = {}
    for id, settings in data.items():
        plugin_type = settings.pop("type")
        plgs[id] = manager.get_instance(plugin_type, settings)
    
    for plg in plgs.values():
        plg.run()


if __name__ == '__main__':
    main()