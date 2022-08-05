import unittest

from datetime import datetime

from battery.spindler_battery import SpindlerBattery

from engine.model.calliope import Calliope_e, Calliope_b
from engine.model.glissade import Glissade_e, Glissade_b
from engine.model.palindrome import Palindrome_e, Palindrome_b
from engine.model.rorschach import Rorschach_e, Rorschach_b
from engine.model.thovex import Thovex_e, Thovex_b

current_date = datetime.today().date()

class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        
        last_service_date = current_date.replace(year=current_date.year - 3)

        car = Calliope_b(last_service_date, current_date)
        self.assertTrue(car.needs_service())


    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Calliope_e(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Glissade_b(last_service_date, current_date)
        self.assertTrue(car.needs_service())
    
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Glissade_e(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = current_date.replace(year=current_date.year - 5)
        warning_light_is_on = False

        car = Palindrome_b(last_service_date, current_date)
        self.assertTrue(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = Palindrome_e(last_service_date, warning_light_is_on)
        self.assertTrue(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        
        last_service_date = current_date.replace(year=current_date.year - 3)

        car = Rorschach_b(last_service_date, current_date)
        self.assertFalse(car.needs_service())


    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Rorschach_e(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        
        last_service_date = current_date.replace(year=current_date.year - 3)

        car = Thovex_b(last_service_date, current_date)
        self.assertFalse(car.needs_service())


    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Thovex_e(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())


if __name__ == '__main__':
    unittest.main()