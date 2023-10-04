from abc import ABC, abstractmethod
from datetime import datetime, date


class Battery(ABC):
    @abstractmethod
    def need_service(self):
        pass


class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def need_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 4
        )
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False


class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def need_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 3
        )
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False
