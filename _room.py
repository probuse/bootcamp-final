class Room(object):
    def __init__(self):
        self.office_room_names = []
        self.living_room_names = []
        
    def create_room(self, room_type, *room_name):
        """Creates a room in the Dojo. 
        Can create as many rooms as specified by room_name"""
        if room_type.lower() == 'office':
            for i in room_name:
                if i in self.office_room_names:
                    return 'Room {} already created'.format(i)
                self.office_room_names.append(i)
                print("An office called {} has been successfully created".format(i))
        elif room_type.lower() == 'living space':
            for i in room_name:
                if i in self.office_room_names:
                    return 'Room {} already created'.format(i)
                self.living_room_names.append(i)
                print("A Living space called {} has been successfully created".format(i))
        else:
            return "Room Type not in the Dojo"
