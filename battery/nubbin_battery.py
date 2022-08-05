from abc import ABC
from datetime import datetime
from car import Car

class NubbinBattery(Car, ABC):
    def __init__(self, last_service_date, current_date):
        self.current_date = datetime.today().date()
        super().__init__(last_service_date)

    def battery_should_be_serviced(self):
        if self.current_date.year - self.last_service_date.year > 4:
            return True
        else:
            return False