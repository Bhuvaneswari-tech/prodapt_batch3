#Defina a class
from exception import OwnerAlreadyExistsError
from utils import log_action
class Car:
    def __init__(self, brand, model, year, owner=None):
        self.brand = brand
        self.model = model
        self.year = year
        self.__owner = owner  # Encapsulation - Private attribute to store the owner of the car

    @log_action
    def start_engine(self):
        print(f"The engine of the {self.brand} {self.model} is starting.")
    
    def show_info(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}")
    
    #Abstraction - Public methods to set and get the owner of the car   
    def set_owner(self, owner):
        if not self.__owner: #Check if no owner is set
            self.__owner = owner  # Set the owner of the car
        else:
            #print(f"The car already has an owner: {self.__owner}. Cannot change owner.")
            raise OwnerAlreadyExistsError(self.__owner)

    def get_owner(self):
        return self.__owner  # Get the owner of the car