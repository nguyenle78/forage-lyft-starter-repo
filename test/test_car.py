import unittest
from datetime import datetime

import model.factory
import engine
import battery


# class TestCalliope(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0
#         car = model.factory.CalliopeFactory.create_car(
#             current_date=today,
#             last_service_date=last_service_date,
#             current_mileage=current_mileage,
#             last_service_mileage=last_service_mileage,
#         )

#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 1)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = model.factory.CalliopeFactory.create_car(
#             today, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30001
#         last_service_mileage = 0

#         car = model.factory.CalliopeFactory.create_car(
#             last_service_date, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30000
#         last_service_mileage = 0

#         car = model.factory.CalliopeFactory.create_car(
#             last_service_date, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertFalse(car.needs_service())


# class TestGlissade(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = model.factory.GlissadeFactory.create_car(
#             today, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 1)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = model.factory.GlissadeFactory.create_car(
#             today, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = model.factory.GlissadeFactory.create_car(
#             last_service_date, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = model.factory.GlissadeFactory.create_car(
#             last_service_date, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertFalse(car.needs_service())


# class TestPalindrome(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         warning_light_is_on = False

#         car = model.factory.PalindromeFactory.create_car(
#             today, last_service_date, warning_light_is_on
#         )
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         warning_light_is_on = False

#         car = model.factory.PalindromeFactory.create_car(
#             today, last_service_date, warning_light_is_on
#         )
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = True

#         car = model.factory.PalindromeFactory.create_car(
#             last_service_date, last_service_date, warning_light_is_on
#         )
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = False

#         car = model.factory.PalindromeFactory.create_car(
#             last_service_date, last_service_date, warning_light_is_on
#         )
#         self.assertFalse(car.needs_service())


# class TestRorschach(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = model.factory.RorschachFactory.create_car(
#             today, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = model.factory.RorschachFactory.create_car(
#             today, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = model.factory.RorschachFactory.create_car(
#             last_service_date, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = model.factory.RorschachFactory.create_car(
#             last_service_date, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertFalse(car.needs_service())


# class TestThovex(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = model.factory.ThovexFactory.create_car(
#             today, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = model.factory.ThovexFactory.create_car(
#             today, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30001
#         last_service_mileage = 0

#         car = model.factory.ThovexFactory.create_car(
#             last_service_date, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30000
#         last_service_mileage = 0

#         car = model.factory.ThovexFactory.create_car(
#             last_service_date, last_service_date, current_mileage, last_service_mileage
#         )
#         self.assertFalse(car.needs_service())


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
        last_service_date = today.replace(year=today.year - 3)
        car_battery = battery.SpindlerBattery(last_service_date, today)
        self.assertTrue(car_battery.need_service())

    def test_not_need_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        car_battery = battery.SpindlerBattery(last_service_date, today)
        self.assertFalse(car_battery.need_service())


if __name__ == "__main__":
    unittest.main()
