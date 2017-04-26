from room import Room

class Dojo(object):
    "Dojo Class has-a relationship with Room class"
    def __init__(self):
        self.room = Room()        

class Office(Room):
    pass
    
    
class LivingSpace(Room):
    pass


class Person(object):
    pass        
    
class Fellow(Person):
    def __init__(self):
        pass
    
    
class Staff(Person):
    pass
    
'''
********************************************************************
print_unallocated....Take care to notice everyone is allocated....
you can't add a person without allocating them space
====================================================================
  
pen = Person('pen') 
room = Room()
#print(room.create_room('living', 'maverick'))
print(room.create_room('office', 'maverick', 'nana'))
#print (room.living_space_people_counter)
print (pen.office_people_counter)
#print (room.office_people_counter)
''' 
