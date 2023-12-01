import display
import sensor


class CarPark:
    def __int__(self,
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

    def __str__(self):
        return f"{self.name} at {self.location} with a capacity of {self.max_bays} bays"

    def register(self, component):
        if not isinstance(component, (sensor.Sensor, display.Display)):
            raise TypeError("Object must be a Sensor or Display")
        elif isinstance(component, sensor.Sensor):
            self.sensors.append(component)
        else:
            self.displays.append(component)


