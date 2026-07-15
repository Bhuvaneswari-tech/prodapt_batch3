import unittest
import os
from vehiclemanagement.car import Car
from vehiclemanagement.ev import EV
from vehiclemanagement.report_export import export_vehicle_data

class TestIntegration(unittest.TestCase):

    def setUp(self):
        self.car = Car("Toyota", "Corolla", 2022)
        self.ev = EV("Tesla", "Model 3", 2023, 75)
        self.car.set_owner("Alice")
        self.ev.set_owner("Bob")
        self.vehicles = [self.car, self.ev]
        self.filename = "vehicle_report.csv"

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_polymorphism_start_engine(self):
        self.assertEqual(self.car.start_engine(), "Toyota Corolla engine started!")
        self.assertEqual(self.ev.start_engine(), "Tesla Model 3 powers on silently!")

    def test_export_report_creates_file(self):
        msg = export_vehicle_data(self.filename, self.vehicles)
        self.assertTrue(os.path.exists(self.filename))
        self.assertIn("Report exported successfully", msg)

        # Check file contents
        with open(self.filename, "r") as f:
            content = f.read()
            self.assertIn("Toyota,Corolla,2022,Alice,", content)
            self.assertIn("Tesla,Model 3,2023,Bob,75", content)

if __name__ == "__main__":
    unittest.main()
