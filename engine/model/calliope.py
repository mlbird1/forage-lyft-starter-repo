from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class Calliope_b(SpindlerBattery):
   def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.battery_should_be_serviced()==True:
            return True
        else:
            return False



class Calliope_e(CapuletEngine):
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False

