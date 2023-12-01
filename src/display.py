class Display:
    def __int__(self,
                id,
                car_park,
                message="",
                is_active=False):
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_active

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")
    def __str__(self):
        return f'Display {self.id} is {"is active" if self.is_on else "is active"}'

