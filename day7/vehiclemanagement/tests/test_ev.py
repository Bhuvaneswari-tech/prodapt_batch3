import unittest
from vehiclemanagement.ev import EV
from vehiclemanagement.exception import VehicleError

class TestEV(unittest.TestCase):

    def setUp(self):
        self.ev = EV("Tesla", "Model 3", 2021, 75)

    def test_ev_initialization(self):
        self.assertEqual(self.ev.brand, "Tesla")
        self.assertEqual(self.ev.model, "Model 3")
        self.assertEqual(self.ev.year, 2021)
        self.assertEqual(self.ev.battery_capacity, 75)

    def test_invalid_battery_capacity_raises(self):
        with self.assertRaises(VehicleError):
            EV("Skoda", "Rapid", 2021, -50)

    def test_charge_battery(self):
        self.assertEqual(self.ev.charge_battery(), "Tesla Model 3 battery charged to 75 kWh.")

    def test_start_engine_override(self):
        self.assertEqual(self.ev.start_engine(), "Tesla Model 3 powers on silently!")

    def test_show_info_inherited(self):
        self.assertEqual(self.ev.show_info(), "2021 Tesla Model 3")

    def test_set_owner(self):
        self.ev.set_owner("Bob")
        self.assertEqual(self.ev.get_owner(), "Bob")

if __name__ == "__main__":
    unittest.main()
