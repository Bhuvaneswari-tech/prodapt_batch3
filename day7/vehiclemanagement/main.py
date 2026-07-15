from vehiclemanagement.car import Car
from vehiclemanagement.ev import EV
from polymorphism import Overloading_demo
from vehiclemanagement.exception import VehicleError
from vehiclemanagement.report_export import export_vehicle_data
'''
#create object for the class
car1 = Car("Toyota", "Camry", 2020)
ev1 = EV("Tesla", "Model 3", 2021, 75)  # Example of creating an EV object

car1.set_owner("Alice")
print(car1.get_owner())  # Output: Alice

#car1.set_owner("Bob")  # This will raise an exception since the owner is already set
# Call methods on the objects

car1.start_engine()
car1.show_info()

ev1.show_info()  # Assuming EV inherits show_info from Car
ev1.start_engine()
ev1.charge_battery()

#ev2 = EV("Skoda", "Rapid", 2021, -50)
#ev2.charge_battery()  # This will raise an exception due to invalid battery capacity
Overloading_demo()  # Call the function to demonstrate method overloading

'''

def main():
    try:
        car1 = Car("Toyota", "Corolla", 2022)
        car2 = EV("Tesla", "Model 3", 2023, 75)

        car1.set_owner("Alice")
        car2.set_owner("Bob")

        vehicles = [car1, car2]

        print(car1.show_info(), car1.get_owner())
        print(car2.show_info(), car2.get_owner())

        print("\n--- Overloading Demo ---")
        Overloading_demo()
        
        car1.start_engine()

        print("\n--- Export Report ---")
        print(export_vehicle_data("vehicle_report.csv", vehicles))

    except VehicleError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()