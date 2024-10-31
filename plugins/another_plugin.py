# plugins/another_plugin.py

from plugin_system import Plugin

class AnotherPlugin(Plugin):
    def run(self):
        print("Running AnotherPlugin")