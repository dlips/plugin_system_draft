import importlib.util
from plugin_system import PluginFactory
import yaml
import pprint

def adjust_control_schedule(control_schedule, cost):
    return control_schedule

def calculate_cost_function(system_state, dynamic_forecasts, control_schedule):
    return 0

class EMS:
    def __init__(self, static_forecasters, dynamic_forecasters):
        self.static_forecasters = static_forecasters
        self.dynamics_forecasters = dynamic_forecasters

    def simulate(self):
        prediction_steps = 10
        # Static forecast need to be run only once before the optimization starts
        # because they are not controllable 
        static_forecasts = {}
        for forecast in self.static_forecasters:
            static_forecasts.update(forecast.run(prediction_steps))

        # Here we should set an initial control schedule as initial value for
        # the optimization
        control_schedule = {}
        dynamic_forecasts = {}
        # Optimize the loads/generators we can control
        for i in range(0, 10):
            for forecaster in self.dynamics_forecasters:
                dynamic_forecasts.update(forecaster.run(static_forecasts, control_schedule, prediction_steps))

            cost = calculate_cost_function(static_forecasts, dynamic_forecasts, control_schedule)
            control_schedule = adjust_control_schedule(control_schedule, cost)

        pprint.pprint(static_forecasts)
        pprint.pprint(dynamic_forecasts)
            


def main():
    # Load the plugins
    factory = PluginFactory()

    print("Loaded plugins:")
    pprint.pprint([key for key in factory.plugins.keys()])

    with open('config.yaml', 'r') as file:
        data = yaml.safe_load(file)

    static_forecasters = []
    dynamic_forecasters = []

    for id, settings in data.items():
        plugin_type = settings.pop("type")
        settings["id"] = id
        plg = factory.create_plugin(plugin_type, settings)
        if plg.forecast_type() == "static":
            static_forecasters.append(plg)
        else:
            dynamic_forecasters.append(plg)

    EMS(static_forecasters, dynamic_forecasters).simulate()


if __name__ == '__main__':
    main()