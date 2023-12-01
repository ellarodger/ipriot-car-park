class Display:
    def __init__(self,
                id,
                car_park,
                message="",
                is_active=False):
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_active = is_active

    def update(self, data):
        for key, value in data.items():
            setattr(self, f"{key}", value)
            print(f"{key}: {value}")
    def __str__(self):
        return f'Display {self.id} is {"is active" if self.is_on else "is active"}'

