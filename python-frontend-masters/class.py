class Vehicle:

    number_of_wheels = 4

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def __str__(self):
        return f"i drive {self.make} {self.model}"


daily = Vehicle("Subaru", "Cross")
# print(daily)
# print(daily.number_of_wheels)


# print(f"i drive {daily.make} {daily.model}")

class GitHubRepo:
    def __init__(self, name, language, num_stars):
        self.name = name
        self.language = language
        self.num_stars = num_stars

    def __str__(self):
        return f"{self.name} {self.language} {self.num_stars}"


new_git_hub = GitHubRepo("Vue", "Javascript", 5)
print(str(new_git_hub))
