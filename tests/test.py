import unittest
from unittest import TestCase
from parking_lot.parking import Cars

class ParkingLotCarTest(TestCase):
    def setUp(self):
        pass

    def test_create_parking_lot(self):
        self.assertEqual("6", Cars.create_parking_lot(self, str(6)))
        self.assertEqual("0", Cars.create_parking_lot(self, str(0)))
        self.assertEqual("-1", Cars.create_parking_lot(self, str(-1)))

    def test_park(self):
        car = Cars()
        car.create_parking_lot( "2")
        self.assertEqual("MH-101-KHA", car.park("MH-101-KHA","Black"))
        self.assertEqual("KA-101-ABC", car.park("KA-101-ABC","White"))
        self.assertEqual(0, car.park("KA-101-ABC","White"))

    def test_leave(self):
        car = Cars()
        car.create_parking_lot("2")
        self.assertEqual(1, car.leave(1))

    def test_registration_numbers_for_cars_with_colour(self):
        car = Cars()
        car.create_parking_lot("2")
        car.park("MH-101-KHA","Black")
        self.assertEqual("MH-101-KHA", car.registration_numbers_for_cars_with_colour("Black"))

    def test_slot_numbers_for_cars_with_colour(self):
        car = Cars()
        car.create_parking_lot("2")
        car.park("MH-101-KHA","Black")
        car.park("KA-101-ABC","Black")
        self.assertEqual("1, 2", car.slot_numbers_for_cars_with_colour("Black"))

    def test_slot_number_for_registration_number(self):
        car = Cars()
        car.create_parking_lot("2")
        car.park("MH-101-KHA","Black")
        car.park("KA-101-ABC","Black")
        self.assertEqual(2, car.slot_number_for_registration_number("KA-101-ABC"))

    def test_status(self):
        car = Cars()
        car.create_parking_lot("2")
        car.park("MH-101-KHA","Black")
        car.park("KA-101-ABC","Black")
        self.assertEqual([1,2],car.status())

if(__name__=='__main__'):
    unittest.main()
