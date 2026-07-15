import unittest
from vehiclemanagement.car import Car
from vehiclemanagement.exception import VehicleError

class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car("Toyota", "Camry", 2020)

    def test_car_initialization(self):
        self.assertEqual(self.car.brand, "Toyota")
        self.assertEqual(self.car.model, "Camry")
        self.assertEqual(self.car.year, 2020)

    def test_set_owner_success(self):
        self.car.set_owner("Alice")
        self.assertEqual(self.car.get_owner(), "Alice")

    def test_set_owner_twice_raises(self):
        self.car.set_owner("Alice")
        with self.assertRaises(VehicleError):
            self.car.set_owner("Bob")

    def test_start_engine(self):
        self.assertEqual(self.car.start_engine(), "Toyota Camry engine started!")

    def test_show_info(self):
        self.assertEqual(self.car.show_info(), "2020 Toyota Camry")

if __name__ == "__main__":
    unittest.main()
