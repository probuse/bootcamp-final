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
        room2 = Room()
        initial_room_count = len(room2.room_names)
        many_rooms = room.create_room('office', 'blue', 'black', 'red')
        new_room_count = len(room2.room_names)
        self.assertEqual(new_room_count - initial_room_count, 3)
    
    def test_living_room_created_successfully(self):
        room3 = Room()
        initial_room_count = len(room3.room_names)
        many_rooms = room.create_room('living space', 'blue', 'black', 'red')
        new_room_count = len(room3.room_names)
        self.assertEqual(new_room_count - initial_room_count, 3)
        
    
        
        

if __name__=="__main__":
    unittest.main()        
