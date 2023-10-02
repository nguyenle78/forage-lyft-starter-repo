from abc import ABC, abstractmethod
import engine
import battery


class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass


class CalliopeFactory(CarFactory):
    def __init__(self) -> None:
        self.engine = engine.CapuletEngine()
        self.battery = battery.SpindlerBattery()

    def create_car(self, engine, battery):
        pass
