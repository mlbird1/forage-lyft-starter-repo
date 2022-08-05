from abc import ABC
from datetime import datetime
from car import Car

class SpindlerBattery(Car, ABC):
    def __init__(self, last_service_date, current_date):
        self.current_date = datetime.today().date()
        super().__init__(last_service_date)

    def battery_should_be_serviced(self):
        if self.current_date - self.last_service_date > 2:
            return True
        else:
            return False
