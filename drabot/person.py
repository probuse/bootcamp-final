from room import Room

room = Room()
class Person(object):
    "class Person takes in one positional argument names"
    def __init__(self, name):
        self.name = name
        self.office_people_counter = room.office_people_counter
        
    
        
per = Person('pen')
print (per.office_people_counter)
