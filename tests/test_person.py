import sys
sys.path.append('/home/probuse/dev/Python/drabot/bootcampFinal')
import unittest
from drabotApp.person import Person

class PersonTestCase(unittest.TestCase):
    "Tests to test person object"

    def setUp(self):
        self.person = Person("etwin", 21)
    
    def tearDown(self):
        pass

    def test_person_has_name_and_age(self):
        "Tests person object has name and age properties"
        self.assertEqual(self.person.name, "etwin")
        self.assertEqual(self.person.age, 21)

    def test_person_age_is_above_18(self):
        "Tests age is greater than 18 for a person object"
        self.assertEqual(self.person.check_age(), True)