class Display:
    def __int__(self,
                id,
                car_park,
                message="",
                is_on=False):
        self.id = id
        self.car_park = car_park
        self.message = message or []
        self.is_on = is_on or []

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")
    def __str__(self):
        return f"Display {self.id}: {self.message}"

