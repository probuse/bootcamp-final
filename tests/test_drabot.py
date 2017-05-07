import unittest
import sys

sys.path.append('../drabot')
from _room import Room
from person import Person


class TestCreateRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room()
    
    def test_create_room_successfully(self):
        office_name = self.room.create_room('office', 'havana')
        initial_room_count = len(self.room.office_room_names)
        python_room = self.room.create_room('office', 'python')
        new_room_count = len(self.room.office_room_names)
        self.assertEqual(new_room_count - initial_room_count, 1)
        
    def test_multiple_rooms_created_successfully(self):
        initial_room_count = len(self.room.office_room_names)
        many_rooms = self.room.create_room('office', 'blue', 'black', 'red')
        new_room_count = len(self.room.office_room_names)
        self.assertEqual(new_room_count - initial_room_count, 3)
    
    def test_living_room_created_successfully(self):
        initial_room_count = len(self.room.living_room_names)
        many_rooms = self.room.create_room('living_space', 'blue', 'black', 'red')
        new_room_count = len(self.room.living_room_names)
        self.assertEqual(new_room_count - initial_room_count, 3)
    
    def test_add_person_successfully(self):
        office_name = self.room.create_room('office', 'blue')
        initial_andelan_count = self.room.andelans
        phillip = self.room.add_person('Phillip', 'staff')
        new_andelan_count = self.room.andelans
        self.assertEqual(new_andelan_count - initial_andelan_count, 1)
        
    def test_person_is_above_18(self):
        person = Person('probuse', 40)
        self.assertTrue(person.check_age())
        
    def test_false_if_person_is_below_18(self):
        person = Person('Nuwa', 12)
        self.assertFalse(person.check_age())
        
    def test_name_is_alpha(self):
        person = Person('Ray', 23)
        self.assertTrue(person.name.isalpha())
        
    def test_show_room_allocation(self):
        blue = self.room.create_room('office', 'blue')
        brain = self.room.add_person('brain', 'staff')
        self.assertListEqual(['brain'], self.room.office_room_people['blue'])
        
    def test_number_of_people_in_office_less_or_equal_6(self):
        orange = self.room.create_room('office', 'orange')
        simon = self.room.add_person('simon', 'fellow')
        peter = self.room.add_person('peter', 'staff')
        shyla = self.room.add_person('shyla', 'staff')
        bruce = self.room.add_person('bruce', 'fellow')
        david = self.room.add_person('david', 'staff')
        sam = self.room.add_person('sam', 'staff')
        pro = self.room.add_person('pro', 'staff')
        self.assertEqual(len(self.room.office_room_people['orange']), 6)
        
   
if __name__=="__main__":
    unittest.main()         
