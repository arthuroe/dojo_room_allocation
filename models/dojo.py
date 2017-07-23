from room import *
from person import *


class Dojo(object):
    def __int__(self):
        self.rooms = []
        self.people = []
        self.offices = []
        self.livingspaces = []
        self.vacant_offices = []
        self.vacant_livingsapces = []
        self.rooms = []

    def create_room(self, room_type, *room_names):
        room_names = list(room_names)
        new = []
        for room_name in room_names:
            if room_name.lower() in self.rooms:
                return 'Room already exists!'

            if room_type.lower() == 'office':
                #new_room = Office(room_name)
                offices.append(room)
            elif room_type.lower() == 'living_space':
                #new_room = LivingSpace(room_name)
                livingspaces.append(room)
            else:
                return 'Unknown Room Type'
            self.rooms.append(room_name)
            new.append(room_name)
        for name in new:
            print(name + ' ' + room_type + ' has been successfully added!')
        return self.rooms


def main():
    dojo = Dojo()
    dojo.create_room('office', 'blue', 'black', 'green')


if __name__ == '__main__':
    main()
