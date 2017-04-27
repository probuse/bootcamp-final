from room import Room

#room = Room()
#room.create_room('office', 'mommm')

class Office(Room):
    def __init__(self):
        super(Office, self).__init__()
        
    def show_people_in_office(self):
        people_in_office = room.people_in_office
        print (people_in_office)
        
off = Office()
off.show_people_in_office()
