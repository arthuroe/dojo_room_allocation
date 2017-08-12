import unittest
import sys
import os
sys.path.append('..')
from models.dojo import Dojo

sys.dont_write_bytecode = True


class DojoTestCase(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_initial_room_check(self):
        self.assertEqual(self.dojo.rooms, {})

    def test_create_room_successfully(self):
        initial_room_count = len(self.dojo.rooms)
        blue_office = self.dojo.create_room('office', 'blue')
        self.assertTrue(blue_office)
        new_room_count = len(self.dojo.rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)

    def test_create_room_if_office_already_exists(self):
        self.dojo.rooms = {'office': ['blue']}
        self.assertEqual(self.dojo.create_room('office', 'blue'),
                         'office already exists!', msg='office already exists!')

    def test_create_room_if_livingspace_already_exists(self):
        self.dojo.rooms = {'living_space': ['blue']}
        self.assertEqual(self.dojo.create_room('living_space', 'blue'),
                         'living_space already exists!', msg='living_space already exists!')

    def test_create_multiple_rooms(self):
        self.assertEqual(self.dojo.create_room(
            'office', 'blue', 'black', 'yellow'), self.dojo.rooms)

    def test_create_unknown_room_type(self):
        self.assertEqual(self.dojo.create_room('kitchen', 'green'),
                         'Unknown Room Type', msg='Unknown Room Type')

    def test_initial_add_person_check(self):
        self.assertEqual(self.dojo.people, [])

    def test_add_person_successfully(self):
        self.dojo.offices, self.dojo.living_space = {
            'blue': [], 'green': []}, {'yellow': [], 'grey': []}
        self.dojo.vacant_offices, self.dojo.vacant_livingspaces = [
            'blue', 'green'], ['yellow', 'grey']
        initial_people_count = len(self.dojo.people)
        john_staff = self.dojo.add_person('john', 'staff', 'N')
        self.assertTrue(john_staff)
        new_people_count = len(self.dojo.people)
        self.assertEqual(new_people_count - initial_people_count, 1)

    def test_add_staff(self):
        self.dojo.offices, self.dojo.living_space = {
            'blue': [], 'green': []}, {'yellow': [], 'grey': []}
        self.dojo.vacant_offices, self.dojo.vacant_livingspaces = [
            'blue', 'green'], ['yellow', 'grey']
        self.assertEqual(self.dojo.add_person('john me', 'staff', 'N'), self.dojo.people)

    def test_add_fellow(self):
        self.dojo.offices, self.dojo.living_space = {
            'blue': [], 'green': []}, {'yellow': [], 'grey': []}
        self.dojo.vacant_offices, self.dojo.vacant_livingspaces = [
            'blue', 'green'], ['yellow', 'grey']
        self.assertEqual(self.dojo.add_person('john me', 'fellow', 'Y'), self.dojo.people)

    def test_add_person_when_person_already_exists(self):
        self.dojo.offices, self.dojo.living_space = {
            'blue': [], 'green': []}, {'yellow': [], 'grey': []}
        self.dojo.vacant_offices, self.dojo.vacant_livingspaces = [
            'blue', 'green'], ['yellow', 'grey']
        self.dojo.people = ['john me']
        self.assertEqual(self.dojo.add_person('john me', 'fellow', 'Y'),
                         'Person already exists', msg='Person already exists')

    def test_add_unknown_person_type(self):
        self.assertEqual(self.dojo.add_person('john me', 'follow', 'Y'),
                         'Unknown position', msg='Unknown position')

    def test_person_office_allocation(self):
        pass

    def test_person_living_space_allocation(self):
        pass

    def test_vacant_space_reduction_after_allocation(self):
        pass

    def test_names_in_room_are_true(self):
        pass

    def test_allocations_written_to_text_file(self):
        pass

    def test_unallocated_names_written_to_text_file(self):
        pass

    def test_names_in_room_are_true(self):
        pass

    def test_allocations_written_to_text_file(self):
        pass

    def test_unallocated_names_written_to_text_file(self):
        pass
