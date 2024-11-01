import numpy as np
from plugin_system import Plugin

class PVForecast(Plugin):
    def __init__(self, id, kwPeak, direction, longitude, latitude):
        self.id = id
        self.kwPeak = kwPeak
        self.direction = direction
        self.longitude = longitude
        self.latitdue = latitude

    def forecast_type(self):
        return "static"

    def run(self, predict_steps):
        return {
            self.id: {
                'pv_generation': np.ones(predict_steps) * self.kwPeak
            }
        }