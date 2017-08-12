from room import Office, LivingSpace
from person import Staff, Fellow
import sys
import random


class Dojo(object):
    def __init__(self):
        self.rooms = {}
        self.people = []
        self.offices = {}
        self.living_space = {}
        self.vacant_offices = []
        self.vacant_livingspaces = []

    def create_room(self, room_type, *room_names):
        room_name = list(room_names)
        for room in room_names:
            if room_type == 'office':
                self.offices[room] = []
            if room_type == 'living_space':
                self.living_space[room] = []
        for room in room_names:
            if room_type == 'office':
                if 'office' in self.rooms:
                    self.offices[room] = []
                    if room in self.rooms['office']:
                        return 'office already exists!'
                    else:
                        self.rooms['office'].append(room)
                else:
                    self.rooms['office'] = room_name
                return self.rooms
            elif room_type == 'living_space':
                if 'living_space' in self.rooms:
                    self.living_space[room] = []
                    if room in self.rooms['living_space']:
                        return 'living_space already exists!'
                    else:
                        self.rooms['living_space'].append(room)
                else:
                    self.rooms['living_space'] = room_name
                return self.rooms
            else:
                return 'Unknown Room Type'

    def check_vacant_rooms(self):
        for office in self.offices:
            if len(self.offices[office]) < Office.capacity and office not in self.vacant_offices:
                self.vacant_offices.append(office)
            elif len(self.offices[office]) >= Office.capacity and office in self.vacant_offices:
                self.vacant_offices.remove(office)
        for space in self.living_space:
            if len(self.living_space[space]) < LivingSpace.capacity and space not in self.vacant_livingspaces:
                self.vacant_livingspaces.append(space)
            elif len(self.living_space[space]) >= LivingSpace.capacity and space in self.vacant_livingspaces:
                self.vacant_livingspaces.remove(space)

    def allocate_room(self, room):
        self.check_vacant_rooms()
        if room == 'office':
            office_choice = random.choice(self.vacant_offices)
            return office_choice
        elif room == 'living_space':
            living_choice = random.choice(self.vacant_livingspaces)
            return living_choice
        else:
            return 'Room Type Not Considered'

    def add_person(self, name, position, living='N'):
        if living == 'N':
            if position == 'staff':
                if name in self.people:
                    return 'Person already exists'
                else:
                    new_person = Staff(name)
                    choice = self.allocate_room('office')
                    self.offices[choice].append(name)
                    print(name + ' has been allocated office ' + choice + ' !')
                    self.people.append(name)
            elif position == 'fellow':
                if name in self.people:
                    return 'Person already exists'
                else:
                    new_person = fellow(name)
                    choice = self.allocate_room('office')
                    self.offices[choice].append(name)
                    print(name + ' has been allocated office ' + choice + ' !')
                    self.people.append(name)
            elif position != 'staff' or position != 'fellow':
                return 'Unknown position'
        elif living == 'Y':
            if position == 'fellow':
                if name in self.people:
                    return 'Person already exists'
                else:
                    new_person = Fellow(name)
                    choice = self.allocate_room('office')
                    self.offices[choice].append(name)
                    print(name + ' has been allocated office ' + choice + ' !')
                    choice = self.allocate_room('living_space')
                    self.living_space[choice].append(name)
                    print(name + ' has been allocated living space ' + choice + ' !')
                    self.people.append(name)
            elif position != 'staff' or position != 'fellow':
                return 'Unknown position'
        return self.people

    def print_names(self, room):
        if room in self.offices:
            print('\n' + 'Office ' + room)
            return ', '.join(self.offices[room])
        elif room in self.living_space:
            print('\n' + 'Living Space ' + room)
            return ', '.join(self.living_space[room])
        else:
            return "Room doesn't exist"

    def reallocate_person(self, name, new_room):
        if name not in self.people:
            return "Person doesn't exist in the system"
        else:
            return 'Yay'

    def load_people(self):
        pass

    def print_allocations(self):
        with open('allocations.txt', 'w') as f:
            for office in self.offices:
                print('\n')
                print('Office ' + office + '')
                print(', '.join(self.offices[office]))
            for space in self.living_space:
                print('\n')
                print('Living space ' + space + '')
                print(', '.join(self.living_space[space]))

    def print_unallocated(self):
        unallocated = []
        for person in self.people:
            for room in self.offices:
                if person not in self.offices[room]:
                    unallocated.append(person)
                else:
                    return 'All people are allocted rooms'
            for room in self.living_space:
                if person not in self.living_space[room]:
                    unallocated.append(person)
                else:
                    return 'All people are allocted rooms'

        return unallocated


def main():
    dojo = Dojo()
    dojo.create_room('office', 'blue', 'black', 'green')
    dojo.create_room('living_space', 'blu', 'blac', 'gree')
    print(dojo.rooms)
    print(dojo.offices)
    print(dojo.living_space)
    print(Office.capacity)
    print(LivingSpace.capacity)
    dojo.check_vacant_rooms()
    print(dojo.vacant_livingspaces)
    print(dojo.vacant_offices)
    dojo.create_room('living_space', 'grey', 'blc', 'grim')
    dojo.check_vacant_rooms()
    print(dojo.vacant_livingspaces)
    print(dojo.vacant_offices)
    dojo.add_person('john me', 'fellow', 'Y')
    dojo.add_person('Wan chi', 'staff', 'N')
    dojo.add_person('lehn men', 'fellow', 'Y')
    dojo.add_person('hon mep', 'staff', 'N')
    dojo.add_person('not mwe', 'fellow', 'Y')
    dojo.add_person('ohn jop', 'fellow', 'Y')
    dojo.add_person('Wang chin', 'staff', 'N')
    dojo.add_person('nina so', 'fellow', 'Y')
    dojo.add_person('homp hex', 'staff', 'N')
    dojo.add_person('muko mi', 'fellow', 'Y')
    dojo.add_person('kimpi juni', 'staff')
    print(dojo.people)
    print(dojo.offices)
    print(dojo.living_space)
    print(dojo.vacant_livingspaces)
    print(dojo.vacant_offices)
    print(dojo.print_names('blue'))
    print(dojo.print_allocations())
    print(dojo.print_unallocated())


if __name__ == '__main__':
    main()
