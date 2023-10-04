from abc import ABC, abstractmethod


class Tire(ABC):
    @abstractmethod
    def need_service(self):
        pass


class CarriganTire(Tire):
    def __init__(self, sensor_read: list[float]) -> None:
        self.sensor_read = sensor_read

    def need_service(self) -> bool:
        if list(filter(lambda x: x >= 0.9, self.sensor_read)):
            return True
        return False


class OctoprimeTire(Tire):
    def __init__(self, sensor_read: list) -> None:
        self.sensor_read = sensor_read

    def need_service(self):
        return True if sum(self.sensor_read) >= 3 else False
