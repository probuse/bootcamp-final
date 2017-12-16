from drabotApp._room import Room

class Person(object):
    "class Person takes in one positional argument names"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def check_age(self):
        if self.age >= 18:
            return True
