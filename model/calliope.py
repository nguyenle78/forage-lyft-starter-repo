from factory import CarFactory
from engine.capulet_engine import CapuletEngine
from battery import SpindlerBattery


class CalliopeFactory(CarFactory):
    def __init__(self, ) -> None:
        super().__init__()
    def create_car(self, engine: CapuletEngine, battery: SpindlerBattery):
        service_threshold_date = self.last_service_date.replace(
            year=self.last_service_date.year + 2
        )
        if (
            service_threshold_date < datetime.today().date()
            or self.engine_should_be_serviced()
        ):
            return True
        else:
            return False
