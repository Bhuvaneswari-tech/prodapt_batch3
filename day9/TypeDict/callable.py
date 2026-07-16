'''
Case Study: Food Delivery Application
Imagine you're developing a Food Delivery App.
The application can run in three environments:
Development
Testing
Production
'''
#Define Configuration classes
class DevConfig:
    database = "sqlite.db"
    debug = True
class TestConfig:
    database = "test.db"
    debug = True
class ProdConfig:
    database="mysql://food_app"
    debug = False
    

#Step2: Define a Configuration factory(Callable)
def get_config(environment):
    if environment == "dev":
        return DevConfig()
    elif environment == "test":
        return TestConfig()
    else:
        return ProdConfig()

#Step3: Use the factory
env = "dev"

config = get_config(env)

print(config.database)
print(config.debug)