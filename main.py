import os
import importlib.util
import sys
from plugin_system import PluginManager



def main():
    # Load the plugins
    manager = PluginManager()

    print([key for key in manager.plugins.keys()])

    third = manager.get_instance('ThirdPlugin')
    third.run()

if __name__ == '__main__':
    main()