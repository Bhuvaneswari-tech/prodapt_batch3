class Overloadingdemo:
    def show_details(self, *args):
        if len(args) == 1:
            print(f"Car Brand: {args[0]}")
        elif len(args) == 2:
            print(f"Car Brand: {args[0]}, Model: {args[1]}")
        elif len(args) == 3:
            print(f"Car Brand: {args[0]}, Model: {args[1]}, Year: {args[2]}")
        else:
            print("Invalid number of arguments. Please provide 1 to 3 arguments.")

def Overloading_demo():
    demo = Overloadingdemo()
    demo.show_details("Toyota")
    demo.show_details("Honda", "Civic")
    demo.show_details("Ford", "Mustang", 2020)
    demo.show_details("Chevrolet", "Camaro", 2021, "Extra Argument")  # Invalid case