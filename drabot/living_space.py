from room import Room

class LivingSpace(Room):
    def __init__(self):
        super(LivingSpace, self).__init__()
        
    def allocate_space(self, position):
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
