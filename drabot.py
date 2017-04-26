class Dojo(object):
    "Dojo Class has-a relationship with Room class"
    def __init__(self):
        self.room = Room()


class Room(object):
    def __init__(self):
        self.office_people_counter = {}
        self.living_space_people_counter = {}
        self.people_in_office = {}
        self.people_in_living_spaces = {}
        
    def create_room(self, room_type, *args):
        "Creates room in the Dojo, can create as many rooms as we want by\
        specifying multiple <room_name> parameters"
        room_names = args   # store passed arguments for room names in room_names
        while len(room_names) > 0:
            if room_type.lower() == 'office':
                for name in room_names:
                    if name in self.office_people_counter.keys():
                        return "Room name {} already exists in office names".format(name)
                    print("An office called {} has been successfully created".format(name))
                    self.office_people_counter[name] = 0
                return
            elif room_type.lower() == 'living space':
                for name in room_names:
                    if name in list(self.office_people_counter.keys()):
                        return "Room name {} already exists in office names".format(name)
                    print("A Living space called {} has been successfully created".format(name))
                    self.living_space_people_counter[name] = 0
                return
            else: 
                return "Room type {} not in the Dojo".format(room_type)
            
    

class Office(Room):
    pass
    
    
class LivingSpace(Room):
    pass
    
    
class Person(object):
    "class Person takes in one positional argument names"
    def __init__(self, name):
        self.name = name
        
    
class Fellow(Person):
    pass
    
    
class Staff(Person):
    pass
    
'''
********************************************************************
print_unallocated....Take care to notice everyone is allocated....
you can't add a person without allocating them space
====================================================================
'''   
pen = Person('pen') 
room = Room()
#print(room.create_room('living', 'maverick'))
print(room.create_room('office', 'maverick', 'nana'))
#print (room.living_space_people_counter)
print (pen.office_people_counter)
#print (room.office_people_counter)
