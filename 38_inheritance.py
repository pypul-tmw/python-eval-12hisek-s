class vehicle:
    def __init__(self,brand,wheels):
        self.brand = brand
        self.wheels = wheels

    def show_info(self):
        print(f"Brand: {self.brand}, Wheels: {self.wheels}")


#child class
class car(vehicle):
    def __init__(self,brand,seats):
        super().__init__(brand,wheels=4)
        self.seats = seats

    def car_info(self):
        print(f"{self.brand} car with {self.seats} seats")


# Child class 2
class bike(vehicle):
    def __init__(self, brand):
        super().__init__(brand, wheels=2)

    def bike_info(self):
        print(f"{self.brand} bike")

car1 = car("Toyota",5)
bike1 = bike("Bajaj")


car1.show_info()
bike1.show_info()