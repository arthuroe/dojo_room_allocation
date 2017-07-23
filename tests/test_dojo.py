import unittest
import sys
import os
sys.path.append('..')
from models.dojo import Dojo


class DojoTestCase(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_initial_room_check(self):
        self.assertEqual(self.dojo.rooms, [])

    def test_create_room_successfully(self):
        initial_room_count = len(self.dojo.rooms)
        blue_office = self.dojo.create_room()
        self.assertTrue(blue_office)
        new_room_count = len(self.dojo.rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_room_if_room_already_exists(self):
        self.assertNotIn(self.dojo.create_room(), rooms)

    def test_create_multiple_rooms(self):
        self.assertEqual(self.dojo.create_room(), self.dojo.rooms)

    def test_create_unknown_room_type(self):
        self.assertEqual(self.dojo.create_room(),
                         'Unknown room', msg='Unknown room')

    def test_initial_add_person_check(self):
        self.assertEqual(self.dojo.people, [])

    def test_add_person_successfully(self):
        initial_people_count = len(self.dojo.people)
        john_staff = self.dojo.add_person()
        self.assertTrue(john_staff)
        new_room_count = len(self.dojo.people)
        self.assertEqual(new_people_count - initial_people_count, 1)

    def test_add_person_when_person_already_exists(self):
        self.assertNotIn(self.dojo.add_person(), self.dojo.people)

    def test_add_unknown_person_type(self):
        self.assertEqual(self.dojo.add_person(),
                         'Unknown room', msg='Unknown room')
