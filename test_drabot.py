import unittest
from drabot import Room, Office, LivingSpace, Person, Fellow, Staff

class TestCreateRoom(unittest.TestCase):
    def test_create_room_successfully(self):
        room1 = Room()
        initial_room_count = len(room1.room_names)
        python_room = room1.create_room('office', 'orange')
        new_room_count = len(room1.room_names)
        self.assertEqual(new_room_count - initial_room_count, 1)
        
    def test_multiple_rooms_created_successfully(self):
        room = Room()
        initial_room_count = len(room.room_names)
        many_rooms = room.create_room('office', 'blue', 'black', 'red')
        new_room_count = len(room.room_names)
        self.assertEqual(new_room_count - initial_room_count, 3)
        
        
    
        
        

if __name__=="__main__":
    unittest.main()        
