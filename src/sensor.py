from abc import ABC, abstractmethod
import random

class Sensor(ABC):
    def __init__(self,
                 id,
                 car_park,
                 is_active=False):
        self.id = id
        self.car_park = car_park
        self.is_active = is_active

    def _scan_plate(self):
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def __str__(self):
        return f"Sensor {self.id} {"is active" if self.is_active else "is active"}'"

class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_vehicle(plate)
        print(f"Incoming vehicle detected. Plate: {plate}")


class ExitSensor(Sensor):
    def _scan_plate(self):
        return random.choice(self.car_park.plates)

    def update_car_park(self, plate):
        self.car_park.remove_vehicle(plate)
        print(f"Outgoing vehicle detected. Plate: {plate}")
