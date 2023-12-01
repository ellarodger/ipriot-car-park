from display import Display
from sensor import Sensor


class CarPark:
    def __init__(self,
                location,
                name,
                max_bays,
                plates=None,
                sensors=None,
                displays=None):
        self.location = location
        self.name = name
        self.max_bays = max_bays
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []


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

    def remove_vehicle(self, plate):
        self.plates.remove(plate)
        self.update_displays()

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

    def __str__(self):
        return f"{self.name} at {self.location} with a capacity of {self.max_bays} bays"