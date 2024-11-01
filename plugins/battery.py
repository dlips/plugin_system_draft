import numpy as np
from plugin_system import Plugin

class Battery(Plugin):
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity

    def forecast_type(self):
        return "dynamic"

    def run(self, staatic_forecasts, control_schedule, prediction_steps):
        return {
            self.id: {
                'soc': np.linspace(0, self.capacity, prediction_steps) / self.capacity
            }
        }