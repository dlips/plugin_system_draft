from plugin_system import Plugin
import numpy as np

class HouseholdLoad(Plugin):
    def __init__(self, id, average_consumption):
        self.id = id
        self.average_consumption = average_consumption

    def forecast_type(self):
        return "static"

    def run(self, prediction_steps):
        return {
            self.id: {
                'load': (1.0 + np.sin(np.linspace(0, 2*np.pi, prediction_steps))) * self.average_consumption
            }
        }