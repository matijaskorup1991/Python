class Vehicle:
    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def is_eco_friendly(self):
        if self.fuel == "gas":
            return False
        return True


class Car(Vehicle):
    def __init__(self, make, model, fuel="gas", num_wheels=4):
        super().__init__(make, model, fuel)
        self.num_wheels = num_wheels


# my_vehicle = Vehicle("zoom", "goes_fast", "petrol")
# print(my_vehicle.fuel)

my_car = Car("subaru", "cross", "petrol", 2)

print(my_car.is_eco_friendly())
