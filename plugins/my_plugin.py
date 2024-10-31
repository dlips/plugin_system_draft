# plugins/my_plugin.py

from plugin_system import Plugin

class MyPlugin(Plugin):
    def run(self):
        print("Running MyPlugin")