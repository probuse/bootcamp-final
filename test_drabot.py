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
        
        
    def test_add_staff_successfully(self):
        room1 = Room()
        initial_count = room1.total_staff()
        staff1 = room1.add_person('Polly', 'staff')
        staff2 = room1.add_person('Penny', 'staff')
        new_count = room1.total_staff()
        self.assertTrue(staff1)
        self.assertTrue(staff2)
        self.assertTrue(new_count - initial_count, 2)
        
        

if __name__=="__main__":
    unittest.main()        
