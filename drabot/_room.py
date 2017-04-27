import random

class Room(object):
    def __init__(self):
        self.office_room_names = []
        self.living_room_names = []
        self.andelans = 0
        self.office_room_count = {}
        self.living_space_count = {}
        
    def create_room(self, room_type, *room_name):
        """Creates a room in the Dojo. 
        Can create as many rooms as specified by room_name"""
        #unique_room_name = set(room_name) - for unique names
        
        if room_type.lower() == 'office':
            for i in room_name:
                if i in self.office_room_names:
                    return 'Room {} already created'.format(i)
                self.office_room_names.append(i)
                self.office_room_count[i] = 0
                print("An office called {} has been successfully created".format(i))
        elif room_type.lower() == 'living_space':
            for i in room_name:
                if i in self.living_room_names:
                    return 'Room {} already created'.format(i)
                self.living_room_names.append(i)
                self.living_space_count[i] = 0
                print("A Living space called {} has been successfully created".format(i))
        else:
            return "Room Type not in the Dojo"
            
    def add_person(self, person_name, position, accommodation='N'):
        "Adds person to the system"
        if position.lower() == "staff":
            office_name = self.room_allocator('office')
            self.office_room_count[office_name] += 1
            short_name = person_name.split()    
            output = """\
            Staff {0} has been successfully added.
            {1} has been allocated the office {2}
            """.format(person_name, short_name[0], office_name)
            return output
            
        elif position.lower() == "fellow":
            if accommodation == 'Y':
                living_space_name = self.room_allocator('living_space')
                self.living_space_count[living_space_name] += 1
                office_name = self.room_allocator('office')
                self.office_room_count[office_name] += 1
                short_name = person_name.split()
                output = """\
                Fellow {0} has been successfully added.
                {1} has been allocated the office {2}
                {2} has been allocated the livingspace {3}
                """.format(person_name, short_name[0], office_name, living_space_name)
                return output
            elif accommodation == 'N':
                office_name = self.room_allocator('office')
                self.office_room_count[office_name] += 1
                short_name = person_name.split()    
                output = """\
                Fellow {0} has been successfully added.
                {1} has been allocated the office {2}
                """.format(person_name, short_name[0], office_name)
                return output
            else:
                return "Wrong optional argument, argument should either be Y or N"
                
        else: 
            return "Only Fellows and stuff can be added to the system"
            
        
    def room_allocator(self, room_type):
        "allocates rooms"
        available_rooms = []
        if room_type == "office":
            self.andelans += 1
            for i in self.office_room_names:
                if (6 - self.office_room_count[i]) != 0:
                    available_rooms.append(i)
            office_name = available_rooms[random.randint(0, len(available_rooms)-1)]
            return office_name
            
        elif room_type == "living_space":
            available_rooms[:] = []
            for i in self.living_room_names:
                if (4 - self.living_space_count[i]) != 0:
                    available_rooms.append(i)
            if len(available_rooms) > 0:
                living_space_name = available_rooms[random.randint(0, len(available_rooms)-1)]
                return living_space_name
            return 'All created rooms in for living space full. Please create a new room'
            
        else:
            return "Invalid room type, room type is either an office or living space."
