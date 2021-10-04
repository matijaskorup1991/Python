import random

my_data = "this,is,a,coma,seperated,string"
my_data.split(",")

new_data = ":".join(my_data)
# print(new_data)

# nums = [num * num for num in range(6)]

names = ["matija", "luka", "john"]
# names_1 = [("length", len(name))for name in names]
# print(names_1)

# print(", ".join([f"Name is {name}" for name in names]))

nums = [num * num for num in range(6) if num % 2 == 0]
# print(nums)

# nums_test = [num for num in range(6)]
# print(nums_test)
# print(", ".join([str(num) for num in nums_test]))

nums_test = [num for num in range(6)]
# print(sum(nums_test))
# print(sorted(nums_test, reverse=True))

# lottery_numbers_string = "4, 5, 134, 10"
# list_from_numbers = lottery_numbers_string.split(", ")
# print(max([int(num) for num in list_from_numbers]))

# some_sets = {num: num * num for num in range(11)}
# print(some_sets)

# print(set([len(name) for name in names]))

players = ["john", "jane", "alice"]
scores = [100, 57, 90]

# ovo je generator i generatore ne treba spremati u varijable, to je losa praksa, jer generatori nam stoje na raspolaganju samo jednom
zip_type = zip(players, scores)

# for item in zip_type:
#     print(item)


# for name, score in zip_type:
#     # print(type(name))
#     print({"name": name, "score": score})

# print(dict(zip_type))
# my_list = [num for num in range(100) if num % 2 == 0]
# print({num: random.randint(0, 100) for num in my_list})
