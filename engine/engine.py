from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def need_service(self):
        pass


class CapuletEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def need_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: bool) -> None:
        self.warning_light_is_on = warning_light_is_on

    def need_service(self)->bool:
        if self.warning_light_is_on:
            return True
        else:
            return False


class WilloughbyEngine(Engine):
    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def need_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000
