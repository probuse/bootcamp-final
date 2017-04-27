class Staff(Person):
    def __init__(self, name):
        super(Staff, self).__init__(self):
           
    def add_staff_to_room(self):
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
