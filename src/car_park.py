from display import Display
from sensor import Sensor
from pathlib import Path
from datetime import datetime
import json

class CarPark:
    def __init__(self,
                location,
                name,
                max_bays,
                plates=None,
                sensors=None,
                displays=None,
                log_file=Path("log.txt"),):
        self.location = location
        self.name = name
        self.max_bays = max_bays
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_vehicle(self, plate):
        self.plates.append(plate)
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_vehicle(self, plate):
        self.plates.remove(plate)
        self.update_displays()
        self._log_car_activity(plate, "exited")

    def update_displays(self):
        for display in self.displays:
            display.update({"Name": self.name,
                            "Available Bays": self.available_bays,
                            "Temperature": 30,}
                           )
            print(f"Updating: {display}")

    @property
    def available_bays(self):
        if len(self.plates) >= self.max_bays:
            return 0
        return self.max_bays - len(self.plates)

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as file:
            file.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def write_config(self):
        with open ("config.json", "w") as file:
            json.dump({"location":self.location,
                        "name":self.name,
                        "max_bays":self.max_bays,
                        "log_file":str(self.log_file)
                       }, file)

    @staticmethod
    def from_config(config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as file:
            config = json.load(file)
        return CarPark(config["location"], config["name"], config["max_bays"], log_file=config["log_file"])

    def __str__(self):
        return f"{self.name} at {self.location} with a capacity of {self.max_bays} bays"