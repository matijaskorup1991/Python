
import datetime
# class Car:
#     runs = True

#     def start(self, name):
#         self.name = name
#         if self.runs:
#             print(f"{self.name} car is started")
#         else:
#             print(f"{self.name} car is broken")


# # print(Car.runs)
# my_car = Car()

# print(my_car.start("Subaru"))
# print(my_car.name)

# # promjene koje iz istance klase radimo na klasi koja je blueprint od te instance se odnose samo na tu instanu
# my_car.runs = False
# print(my_car.start("Subaru"))

# another_car = Car()
# print(another_car.start("mustang"))

class Car:
    runs = True
    number_of_wheels = 4

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My car the{self.name} currently {self.runs}"

    def __repr__(self):
        return f"Car({self.name})"

    def start(self):
        if self.runs:
            print(f"{self.name} car is started")
        else:
            print(f"{self.name} car is broken")

    @classmethod
    def get_number_of_wheels(cls):
        return cls.number_of_wheels


# print(Car.runs)
my_car = Car("subaru")
# print(my_car.start())
# print(my_car.get_number_of_wheels())

# # class methods mozemo pozvati direktno na klasu
# print(Car.get_number_of_wheels())
# print(dir(Car))

# now = datetime.datetime.now()
# print(now)

# print(str(my_car))
# print(repr(my_car))
