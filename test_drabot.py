import unittest
from _room import Room
from drabot import Office, LivingSpace, Person, Fellow, Staff

class TestCreateRoom(unittest.TestCase):
    def test_create_room_successfully(self):
        room1 = Room()
        initial_room_count = len(room1.office_room_names)
        python_room = room1.create_room('office', 'python')
        new_room_count = len(room1.office_room_names)
        self.assertEqual(new_room_count - initial_room_count, 1)
        
    def test_multiple_rooms_created_successfully(self):
        room2 = Room()
        initial_room_count = len(room2.office_room_names)
        many_rooms = room2.create_room('office', 'blue', 'black', 'red')
        new_room_count = len(room2.office_room_names)
        self.assertEqual(new_room_count - initial_room_count, 3)
    
    def test_living_room_created_successfully(self):
        room3 = Room()
        initial_room_count = len(room3.living_room_names)
        many_rooms = room3.create_room('living space', 'blue', 'black', 'red')
        new_room_count = len(room3.living_room_names)
        self.assertEqual(new_room_count - initial_room_count, 3)
    
    def test_add_person_successfully(self):
        room4 = Room()
        initial_room_count = len(room4.andelans)
        phillip = room4.add_person('Phillip', 'staff')
        new_room_count = len(room4.andelans)
        self.assertEqual(new_room_count - initial_room_count, 1)
        
    def test_person_exists_in_system(self):
        room5 = Room()
        pro = Fellow()
        pro = room5.add_person('Pro', 'fellow')
        self.assertIn('Pro', pro.fellow)
    
        
        

if __name__=="__main__":
    unittest.main()        
