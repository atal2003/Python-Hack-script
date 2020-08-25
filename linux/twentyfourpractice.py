#! /usr/bin/python3


class AshanAtal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, {self.age}"

    def your_drink(self):
        if self.age < 21:
            return f"{self.name} you are not allow to drink"
        else:
            return "go and get yoru drink"


sharif = AshanAtal("ali", 22)
print(sharif.your_drink())


