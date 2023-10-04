import unittest
from datetime import datetime

import engine
import battery
import tire


class TestWilloughbyEngine(unittest.TestCase):
    def test_need_service(self):
        current_mileage = 60001
        last_service_mileage = 0
        car_engine = engine.WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(car_engine.need_service())

    def test_not_need_service(self):
        current_mileage = 60000
        last_service_mileage = 0
        car_engine = engine.WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(car_engine.need_service())


class TestCapuletEngine(unittest.TestCase):
    def test_need_service(self):
        current_mileage = 30001
        last_service_mileage = 0
        car_engine = engine.CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(car_engine.need_service())

    def test_not_need_service(self):
        current_mileage = 30000
        last_service_mileage = 0
        car_engine = engine.CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(car_engine.need_service())


class TestSternmanEngine(unittest.TestCase):
    def test_need_service(self):
        warning_light_is_on = True
        car_engine = engine.SternmanEngine(warning_light_is_on)
        self.assertTrue(car_engine.need_service())

    def test_not_need_service(self):
        warning_light_is_on = False
        car_engine = engine.SternmanEngine(warning_light_is_on)
        self.assertFalse(car_engine.need_service())


class TestNubbinBattery(unittest.TestCase):
    def test_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        car_battery = battery.NubbinBattery(last_service_date, today)
        self.assertTrue(car_battery.need_service())

    def test_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        car_battery = battery.NubbinBattery(last_service_date, today)
        self.assertFalse(car_battery.need_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        car_battery = battery.SpindlerBattery(last_service_date, today)
        self.assertTrue(car_battery.need_service())

    def test_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        car_battery = battery.SpindlerBattery(last_service_date, today)
        self.assertFalse(car_battery.need_service())


class TestCarriganTire(unittest.TestCase):
    def test_need_service(self):
        read = [0, 0.9, 0, 0]
        car_tire = tire.CarriganTire(read)
        self.assertTrue(car_tire.need_service())

    def test_not_need_service(self):
        read = [0, 0.8, 0.8, 0.5]
        car_tire = tire.CarriganTire(read)

        self.assertFalse(car_tire.need_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_need_service(self):
        read = [1, 1, 1, 0]
        car_tire = tire.OctoprimeTire(read)
        self.assertTrue(car_tire.need_service())

    def test_not_need_service(self):
        read = [0, 0.5, 0.8, 0.5]
        car_tire = tire.OctoprimeTire(read)
        self.assertFalse(car_tire.need_service())

        pass


if __name__ == "__main__":
    unittest.main()
