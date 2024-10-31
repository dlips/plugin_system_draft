import os
import importlib
import sys 

# Metaclass that registers plugins
class PluginRegistry(type):
    plugins = {}

    def __init__(cls, name, bases, attrs):
        # Avoid registering the base Plugin class itself
        if name != 'Plugin':
            PluginRegistry.plugins[name] = cls
        super().__init__(name, bases, attrs)

# Base class for all plugins
class Plugin(metaclass=PluginRegistry):
    pass

class PluginManager:
    def __init__(self, plugin_dir="plugins"):
        self.load_plugins(plugin_dir)
        self.plugins = PluginRegistry.plugins

    def load_plugins(self, plugin_directory):
        # Get the absolute path to the plugins directory
        plugin_dir = os.path.join(os.path.dirname(__file__), plugin_directory)

        for filename in os.listdir(plugin_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                module_name = filename[:-3]  # Strip .py extension
                module_path = os.path.join(plugin_dir, filename)

                # Load the module from the file path
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)

    def run_all(self):
        # Using the PluginRegistry to access and run plugins
        for plugin_name, plugin_cls in self.plugins.items():
            plugin_instance = plugin_cls()
            print(f"Executing {plugin_name}:")
            if hasattr(plugin_instance, 'run'):
                plugin_instance.run()
            else:
                print(f"{plugin_name} does not have a 'run' method")

    def get_instance(self, plugin_name): 
        return self.plugins[plugin_name]()