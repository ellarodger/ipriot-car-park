from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

moondalup_car_park = CarPark("Moondalup",
                             "CPP Moondalup",
                             100,
                             log_file="moondalup.txt")
moondalup_entry_sensor = EntrySensor(1, moondalup_car_park, True)
moondalup_exit_sensor = ExitSensor(2, moondalup_car_park, True)
moondalup_display = Display(1, moondalup_car_park, "Welcome to Moondalup", True)

moondalup_car_park.register(moondalup_entry_sensor)
moondalup_car_park.register(moondalup_exit_sensor)
moondalup_car_park.register(moondalup_display)

moondalup_entry_sensor.detect_vehicle()
moondalup_entry_sensor.detect_vehicle()
moondalup_entry_sensor.detect_vehicle()
moondalup_entry_sensor.detect_vehicle()
moondalup_entry_sensor.detect_vehicle()
moondalup_entry_sensor.detect_vehicle()
moondalup_entry_sensor.detect_vehicle()
moondalup_entry_sensor.detect_vehicle()
moondalup_entry_sensor.detect_vehicle()
moondalup_entry_sensor.detect_vehicle()
moondalup_exit_sensor.detect_vehicle()
moondalup_exit_sensor.detect_vehicle()
