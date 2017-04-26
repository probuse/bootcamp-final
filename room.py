import random

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
    
    def add_person(self, person_name, position, living_space='N'):
        "Adds a person to the system and allocates the person a random room"
        available_rooms = [] # will store available rooms for allocation.
        if position.lower() == "staff": # staff can only be allocated office
          
            flag = False
            for key in list(self.office_people_counter):
                if (6 - self.office_people_counter[key]) != 0:
                    available_rooms.append(key) # update our list of rooms to choose from
                    flag = True
                                                                    
            else:
                if flag is False :
                    return "All rooms in office are full. Please create new rooms"
                    
            assigned_room = available_rooms[random.randint(0, len(available_rooms)-1)]
            self.office_people_counter[assigned_room] += 1
            if assigned_room in self.people_in_office:
                self.people_in_office[assigned_room].append(person_name)
            else:
                self.people_in_office[assigned_room] = [name]
            person_name_list = person_name.split()
            result = "\
            Staff {} has been added successfully.\
            {} has been allocated the office {}".format(
                                        person_name, person_name_list[0], assigned_room)
            return result
            
        elif position.lower() == "fellow":
            available_rooms[:] = []
            if living_space == 'Y':
                # assigns fellow living room to fellow.
                flag = False
                for key in list(self.living_space_people_counter):
                    if (4 - self.living_space_people_counter[key]) != 0:
                        available_rooms.append(key) # update our list of rooms to choose from
                        flag = True
                else:
                    if flag is False :
                        return "All rooms for Living space full are full. Please create new rooms"
                        
                assigned_room_living = available_rooms[random.randint(0, len(available_rooms)-1)]
                self.living_space_people_counter[assigned_room_living] += 1
                if assigned_room_living in self.people_in_office:
                    # adds person name to list of assigned rooms
                    self.people_in_office[assigned_room_living].append(person_name)
                else:
                    self.people_in_office[assigned_room_living] = [person_name] # has name of assigned room and people in it
                
                # assigns fellow office
                available_rooms[:] = []
                flag = False
                for key in list(self.office_people_counter):
                    if (6 - self.office_people_counter[key]) != 0:
                        available_rooms.append(key) # update our list of rooms to choose from
                        flag = True
                                                                    
                else:
                    if flag is False :
                        return "All rooms in office are full. Please create new rooms"
                # assign fellow to office space    
                assigned_room_office = available_rooms[random.randint(0, len(available_rooms)-1)]
                self.office_people_counter[assigned_room_office] += 1
                if assigned_room_office in self.people_in_office:
                    self.people_in_office[assigned_room_office].append(person_name)
                else:
                    self.people_in_office[assigned_room_office] = [person_name]
                person_name_list = person_name.split()    
                
                result = """
                Fellow {0} has been added successfully.
                {1} has been allocated the office {2}
                {1} has been allocated the living space {3}""".format(
                                        person_name, 
                                        person_name_list[0], 
                                        assigned_room_office, assigned_room_living)
                return result
            
            elif living_space == 'N':
                flag = False
                for key in list(self.office_people_counter):
                    if (6 - self.office_people_counter[key]) != 0:
                        available_rooms.append(key) # update our list of rooms to choose from
                        flag = True
                                                                    
                else:
                    if flag is False :
                        return "All rooms in office are full. Please create new rooms"
                    
                assigned_room = available_rooms[random.randint(0, len(available_rooms)-1)]
                self.office_people_counter[assigned_room] += 1
                if assigned_room in self.people_in_office:
                    self.people_in_office[assigned_room].append(person_name)
                else:
                    self.people_in_office[assigned_room] = [person_name]
                person_name_list = person_name.split()
                result = "Fellow {} has been added successfully.\n{} has been allocated the office {}".format(
                                                                    person_name, 
                                                                    person_name_list[0], 
                                                                    assigned_room)
                return result
                
room = Room()
room.create_room('living space', 'maverick', 'complex', 'python')
room.create_room('office', 'maverick', 'nana')
print(room.add_person('nina', 'fellow'))
