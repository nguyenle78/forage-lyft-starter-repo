from abc import ABC, abstractmethod
from battery import Battery
from engine import Engine


class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> None:
        pass


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        if self.engine.need_service or self.battery.need_service():
            return True
        return False
