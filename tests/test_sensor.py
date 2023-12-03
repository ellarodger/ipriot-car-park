import unittest
from sensor import *
from car_park import CarPark


class TestSensorTestCase(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", "CPP Moondalup", 100)
        self.entry_sensor = EntrySensor(1, self.car_park, True)
        self.exit_sensor = ExitSensor(2, self.car_park, True)

    def test_exit_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.exit_sensor, Sensor)
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertEqual(self.exit_sensor.car_park, self.car_park)
        self.assertEqual(self.exit_sensor.is_active, True)

    def test_entry_sensor_adds_vehicle(self):
        self.assertFalse(self.car_park.plates)
        self.entry_sensor.detect_vehicle()
        self.assertTrue(self.car_park.plates)

    def test_exit_sensor_removes_vehicle(self):
        self.entry_sensor.detect_vehicle()
        self.exit_sensor.detect_vehicle()
        self.assertFalse(self.car_park.plates)

    def test_entry_sensor_initialised_with_all_attributes(self):
        self.assertIsInstance(self.entry_sensor, Sensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.car_park, self.car_park)
        self.assertEqual(self.entry_sensor.is_active, True)

    def test_instantiating_sensor_raises_error(self):
        with self.assertRaises(TypeError):
            self.sensor = Sensor(1, self.car_park, True)
