class Room(object):
    def __init__(self):
        self.office_room_names = []
        self.living_room_names = []
        
    def create_room(self, room_type, *room_name):
        """Creates a room in the Dojo. 
        Can create as many rooms as specified by room_name"""
        if room_type.lower() == 'office':
            for i in room_name:
                self.office_room_names.append(i)
        elif room_type.lower() == 'living space':
            for i in room_name:
                self.living_room_names.append(i)
        else:
            return "Room Type not in the Dojo"
