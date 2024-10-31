from plugin_system import Plugin

class ThirdPlugin(Plugin):
    def __init__(self, config: dict):
        print(__name__)
        for k, v  in config.items():
            print(f"{k}: {v}")

    def run(self):
        print("Running ThirdPlugin")