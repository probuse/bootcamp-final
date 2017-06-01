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
                if room_name in self.office_room_people.keys():
                    print('An office room {} already created'.format(
                        room_name))
                else:
                    self.office_room_names.append(room_name)
                    self.office_room_people[room_name] = []
                    print("An office called {} has been successfully created".format(
                        room_name))
            
        elif room_type.lower() == 'living_space':
            for room_name in room_names:
                if room_name in self.living_room_people.keys():
                    print('Living room {} alredy created'.format(
                        room_name))
                else:
                    self.living_room_names.append(room_name)
                    self.living_room_people[room_name] = []
                    print("A Living space called {} has been successfully created".format(
                        room_name))
        else:
            return "Room Type is either office or living_space"
            
    def add_person(self, person_name, position, accommodation='N'):
        "Adds person to the system"
        if position.lower() == "staff":
            # if self.check_office_rooms_created():
            office_name = self.allocate_office_room(person_name)
            try:
                self.office_room_people[office_name].append(person_name)
            except KeyError:
                if office_name == 'Name Exists in office':
                    return 'Name Exists in available free office rooms'
                if office_name == 'Office Rooms Full':
                    return 'All Created Office rooms Full'
                if office_name == 'No Office Rooms':
                    return 'No Office Rooms Created Yet'
            else:
                short_name = person_name.split()    
                output = """\
                Staff {0} has been successfully added.
                {1} has been allocated the office {2}
                """.format(person_name, short_name[0], office_name)
                return output
           
        elif position.lower() == "fellow":
            office_name = self.allocate_office_room(person_name)
            try:
                self.office_room_people[office_name].append(person_name)
            except KeyError:
                if office_name == 'Name Exists in office':
                    return 'Name Exists in available free office rooms'
                if office_name == 'Office Rooms Full':
                    return 'All Created Office rooms Full'
                if office_name == 'No Office Rooms':
                    return 'No Office Rooms Created Yet'
            else:
                short_name = person_name.split()    
                output = """\
                Fellow {0} has been successfully added.
                {1} has been allocated the office {2}
                """.format(person_name, short_name[0], office_name)
            
                if accommodation == 'Y':
                    living_space_name = self.allocate_living_room(
                                            person_name)
                    try:
                        self.living_room_people[living_space_name].append(
                            person_name)
                    except KeyError:
                        if living_space_name == 'Name Exists in living':
                            return 'Name Exists in available free living rooms'
                        if living_space_name == 'Living Rooms Full':
                            return 'All Created Living Rooms Full'
                        if living_space_name == 'No Living Rooms':
                            return 'No Living Rooms Created Yet'
                    else:
                        short_name = person_name.split()
                        output = """\
                        Fellow {0} has been successfully added.
                        {1} has been allocated the office {2}
                        {1} has been allocated the livingspace {3}
                        """.format(person_name, short_name[0], 
                                    office_name, 
                                    living_space_name)
                return output
               
    def check_office_rooms_created(self):
        '''
        Checks if there are any rooms of type office created.
        '''
        if len(self.office_room_people) > 0:
            return True
        return False

    def check_living_rooms_created(self):
        '''
        Checks if there are any rooms of type living living_space created.
        '''
        if len(self.living_room_people) > 0:
            return True
        return False

    def check_office_rooms_free_space(self):
        '''
        Checks if there are free rooms of office room_type
        '''
        available_office_rooms = []
        if self.check_office_rooms_created():
            for room in self.office_room_people.keys():
                if len(self.office_room_people[room]) < 6:
                    available_office_rooms.append(room)
            if len(available_office_rooms) > 0:
                return available_office_rooms
            return 'Office Rooms Full'
        return 'No Office Rooms'

    def check_living_rooms_free_space(self):
        '''
        Checks if there are free rooms of living room_type
        '''
        available_living_rooms = []
        if self.check_living_rooms_created():
            for room in self.living_room_people.keys():
                if len(self.living_room_people[room]) < 6:
                    available_living_rooms.append(room)
            if len(available_living_rooms) > 0:
                return available_living_rooms
            return 'Living Rooms Full'
        return 'No Living Rooms'

    def check_person_name_in_office_room(self, person_name):
        '''
        Checks if person_name exists in available_office_rooms.
        '''
        office_rooms = self.check_office_rooms_free_space()
        if office_rooms != 'No Office Rooms':
            if office_rooms != 'Office Rooms Full':
                for office_room in self.office_room_people:
                    if person_name in self.office_room_people[office_room]:
                        office_rooms.remove(office_room)
                if len(office_rooms) > 0:
                    return office_rooms
                return 'Name Exists'
            return 'Office Rooms Full'
        return 'No Office Rooms'

    def check_person_name_in_living_room(self, person_name):
        '''
        Checks if person_name exists in available_living_rooms.
        '''
        living_rooms = self.check_living_rooms_free_space()
        if living_rooms != 'No Living Rooms':
            if living_rooms != 'Living Rooms Full':
                for living_room in self.living_room_people:
                    if person_name in self.living_room_people[living_room]:
                        living_rooms.remove(living_room)
                if len(living_rooms) > 0:
                    return living_rooms
                return 'Name Exists'
            return 'Living Rooms Full'
        return 'No Living Rooms'

    def allocate_office_room(self, person_name):
        '''
        Randomly allocates an office room.
        '''
        office_rooms_to_allocate = self.check_person_name_in_office_room(person_name)
        if office_rooms_to_allocate != 'No Office Rooms':
            if office_rooms_to_allocate != 'Name Exists':
                self.andelans += 1
                allocated_office_room = office_rooms_to_allocate[random.randint(
                    0, len(office_rooms_to_allocate)-1)]
                return allocated_office_room
            return 'Name Exists in office'
        return 'No Office Rooms'

    def allocate_living_room(self, person_name):
        '''
        Randomly allocates an living room.
        '''
        living_rooms_to_allocate = self.check_person_name_in_living_room(person_name)
        if living_rooms_to_allocate != 'No Living Rooms':
            if living_rooms_to_allocate != 'Name Exists':
                allocated_living_room = living_rooms_to_allocate[random.randint(
                    0, len(living_rooms_to_allocate)-1)]
                return allocated_living_room
            return 'Name Exists in living'
        return 'No Living Rooms'
  
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
            
    def print_allocations(self, filename=None):
        """
        Prints a list of allocations on the screen.
        if file name is not None, these allocations are saved to a text file.
        returns a tuple with a list of office room and living_space members.
        """
        office_room = []
        living_room = []
        for room_name in self.office_room_people.keys():
            print(room_name)
            print('-'*70)
            
            for member in self.office_room_people[room_name]:
                print(member, end=' ')
                office_room.append(member)
                print()
                
        for room_name in self.living_room_people.keys():
            print(room_name)
            print('-'*70)
            
            for member in self.living_room_people[room_name]:
                print(member, end=' ')
                living_room.append(member)
                print()
                
                
        return office_room, living_room       
if __name__ == "__main__":
                        
    d4 = Room()
    # d4.create_room('living_space', 'blue')
    d4.create_room('office', 'blue')
    print(d4.add_person('pro', 'fellow', 'Y'))
    d4.add_person('pro2', 'staff')
    # d4.add_person('pro3', 'fellow')
    # d4.add_person('pro21', 'fellow')
    # d4.add_person('pro20', 'fellow')
    # d4.add_person('pro223', 'fellow')
    # d4.add_person('pro212', 'fellow')
    print(d4.add_person('pro21', 'staff'))
    
