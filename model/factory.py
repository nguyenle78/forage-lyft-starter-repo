from abc import ABC, abstractmethod
import engine
import battery
from car import Car


class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass


class CalliopeFactory(CarFactory):
    @staticmethod
    def create_car(
        current_date, last_service_date, current_mileage, last_service_mileage
    ):
        car_engine = engine.CapuletEngine(current_mileage, last_service_mileage)
        car_battery = battery.SpindlerBattery(current_date, last_service_date)
        return Car(car_engine, car_battery)


class GlissadeFactory(CarFactory):
    @staticmethod
    def create_car(
        current_date, last_service_date, current_mileage, last_service_mileage
    ):
        car_engine = engine.WilloughbyEngine(current_mileage, last_service_mileage)
        car_battery = battery.SpindlerBattery(current_date, last_service_date)
        return Car(car_engine, car_battery)


class PalindromeFactory(CarFactory):
    @staticmethod
    def create_car(current_date, last_service_date, warning_light_is_on):
        car_engine = engine.SternmanEngine(warning_light_is_on)
        car_battery = battery.SpindlerBattery(current_date, last_service_date)
        return Car(car_engine, car_battery)


class RorschachFactory(CarFactory):
    @staticmethod
    def create_car(
        current_date, last_service_date, current_mileage, last_service_mileage
    ):
        car_engine = engine.WilloughbyEngine(current_mileage, last_service_mileage)
        car_battery = battery.NubbinBattery(current_date, last_service_date)
        return Car(car_engine, car_battery)


class ThovexFactory(CarFactory):
    @staticmethod
    def create_car(
        current_date, last_service_date, current_mileage, last_service_mileage
    ):
        car_engine = engine.CapuletEngine(current_mileage, last_service_mileage)
        car_battery = battery.NubbinBattery(current_date, last_service_date)
        return Car(car_engine, car_battery)
