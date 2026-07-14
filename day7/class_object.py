'''
Use Case
Imagine you’re building a vehicle management system for a car rental 

company:
Each car can be represented as an object.
The class defines common attributes (brand, model, year) and behaviors 
(start engine, show info).
You can easily create multiple car objects and manage them without 
repeating code.
'''

#Defina a class
class Car:
    def __init__(self, brand, model, year, owner=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.__owner = owner  # Encapsulation - Private attribute to store the owner of the car

    def start_engine(self):
        print(f"The engine of the {self.brand} {self.model} is starting.")
    
    def show_info(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}")
    
    #Abstraction - Public methods to set and get the owner of the car   
    def set_owner(self, owner):
        if not self.__owner: #Check if no owner is set
            self.__owner = owner  # Set the owner of the car
        else:
            print(f"The car already has an owner: {self.__owner}. Cannot change owner.")
        
    def get_owner(self):
        return self.__owner  # Get the owner of the car
        
#create object for the class
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
print(car1.brand)  # Output: Toyota
#print(car1.__owner)
car1.set_owner("Alice")
print(car1.get_owner())  # Output: Alice

car1.set_owner("Bob")
print(car1.get_owner()) 

# Call methods on the objects
car1.start_engine()
car1.show_info()

car2.start_engine()
car2.show_info()

#Another way to call methods on the objects using a list of cars
cars = [car1, car2]

for car in cars:
    car.start_engine()
    car.show_info()
    