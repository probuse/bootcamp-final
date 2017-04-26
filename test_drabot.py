import unittest
from drabot import Room, Office, LivingSpace, Person, Fellow, Staff

class TestCreateRoom(unittest.TestCase):
    def test_create_room_successfully(self):
        room1 = Room()
        initial_room_count = len(room1.office_rooms) + len(room1.living_space_rooms)
        orange = room1.create_room('office', 'Orange')
        blue = room1.create_room('office', 'Blue')
        self.assertTrue(orange)
        new_room_count = len(room1.office_rooms) + len(room1.living_space_rooms)
        self.assertEqual((new_room_count - initial_room_count), 2)

if __name__=="__main__":
    unittest.main()        
