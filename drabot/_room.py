import random

class Room(object):
    def __init__(self):
        self.office_room_names = []
        self.living_room_names = []
        self.andelans = 0
        self.office_room_people = {}
        self.living_room_people = {}
        
    def create_room(self, room_type, *room_names):
        """Creates a room in the Dojo. 
        Can create as many rooms as specified by room_names"""
        if room_type.lower() == 'office':
            for room_name in room_names:
                if room_name in self.office_room_names:
                    return 'Room {} already created'.format(room_name)
                self.office_room_names.append(room_name)
                self.office_room_people[room_name] = []
                print("An office called {} has been successfully created".format(room_name))
        elif room_type.lower() == 'living_space':
            for room_name in room_names:
                if room_name in self.living_room_names:
                    return 'Room {} already created'.format(room_name)
                self.living_room_names.append(room_name)
                self.living_room_people[room_name] = []
                print("A Living space called {} has been successfully created".format(room_name))
        else:
            return "Room Type is either office or living_space"
            
    def add_person(self, person_name, position, accommodation='N'):
        "Adds person to the system"
        if position.lower() == "staff":
            try:
                office_name = self.room_allocator(person_name, 'office')
                self.office_room_people[office_name].append(person_name)
                short_name = person_name.split()    
                output = """\
                Staff {0} has been successfully added.
                {1} has been allocated the office {2}
                """.format(person_name, short_name[0], office_name)
                return output
            except KeyError:
                print('Can not add {}'.format(person_name))
                if office_name == 'in_room':
                    return '{} already exists in available office space'.format(
                        person_name)
                if office_name == 'room_full':
                    return 'No available space in office rooms.'
            
        elif position.lower() == "fellow":
            try:
                if accommodation == 'Y':
                    living_space_name = self.room_allocator(person_name, 'living_space')
                    if person_name in self.living_room_people[living_space_name]:
                        return '{} already exists in living room {}'.format(
                            person_name, living_space_name)
                    self.living_room_people[living_space_name].append(person_name)
                    office_name = self.room_allocator(person_name, 'office')
                    self.office_room_people[office_name].append(person_name)
                    short_name = person_name.split()
                    output = """\
                    Fellow {0} has been successfully added.
                    {1} has been allocated the office {2}
                    {1} has been allocated the livingspace {3}
                    """.format(person_name, short_name[0], office_name, living_space_name)
                    return output
       
                elif accommodation == 'N':
                    office_name = self.room_allocator(person_name, 'office')
                    if person_name in self.office_room_people[office_name]:
                        return '{} already exists in office {}'.format(
                            person_name, office_name)
                    self.office_room_people[office_name].append(person_name)
                    short_name = person_name.split()    
                    output = """\
                    Fellow {0} has been successfully added.
                    {1} has been allocated the office {2}
                    """.format(person_name, short_name[0], office_name)
                    return output
            except KeyError:
                print('Can not add {}'.format(person_name))
                if accommodation == 'Y': 
                    return 'No available space in living rooms.'
                return 'No available space in office rooms.'
            else:
                return "Wrong optional argument, argument should either be Y or N"
                
        else: 
            return "Only fellows and staff can be added to the system"
            
        
    def room_allocator(self, person_name, room_type):
        "allocates rooms"
        available_rooms = []
        if room_type == "office":
            self.andelans += 1
            for office_room_name in self.office_room_people.keys():
                room_full = True
                in_room = False
                if len(self.office_room_people[office_room_name]) < 6:
                    room_full = False
                    if person_name in self.office_room_people[office_room_name]:
                        in_room = True
                        continue
                    available_rooms.append(office_room_name)
            if room_full: return 'room_full'
            if in_room: return 'in_room'
            if len(available_rooms) > 0:
                office_name = available_rooms[random.randint(0, len(available_rooms)-1)]
                return office_name
            return 'All created rooms in for office space full. Please create a new room'
            
        elif room_type == "living_space":
            for living_room_name in self.living_room_names:
                if len(self.living_room_people[living_room_name]) < 4:
                    if person_name in self.office_room_people[living_room_name]:
                        continue
                    available_rooms.append(living_room_name)
            if len(available_rooms) > 0:
                living_space_name = available_rooms[random.randint(0, len(available_rooms)-1)]
                return living_space_name
            return 'All created rooms in for living space full. Please create a new room'
            
        else:
            return "Invalid room type, room type is either an office or living space."
            
    def get_office_allocation(self, room_name):
        "outputs names of people in a certain office room"
        if len(self.office_room_people[room_name]) > 0:
            print("Office {} has the following occupants: ".format(room_name))
            for office_name in self.office_room_people.keys():
                if room_name == office_name:
                    for person_name in self.office_room_people[office_name]:
                        print ('\t*' + person_name)
        else:
            print("No occupants in office {}".format(room_name))
            
    def get_living_space_allocation(self, room_name):
        "outputs names of people in a certain living room"
        if len(self.living_room_people[room_name]) > 0:
            print("Living room {} has the following occupants: ".format(room_name))
            for living_space_name in self.living_room_people.keys():
                if room_name == living_space_name:
                    for person_name in self.living_room_people[living_space_name]:
                        print ('\t*' + person_name)
        else:
            print("No occupants in Living space {}".format(room_name))
            
'''            
d4 = Room()
d4.create_room('office', 'blue')
d4.add_person('pro', 'staff')
d4.add_person('pro2', 'staff')
print(d4.add_person('pro2', 'staff'))
'''
