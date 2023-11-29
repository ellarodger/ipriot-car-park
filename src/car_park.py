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
