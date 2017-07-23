class Room(object):
    def __init__(self, name):
        self.name = name

    @property
    def room_type(self):
        return self.__class__.__name__


class Office(Room):
    capacity = 6

    def __init__(self, name):
        super(Office, self).__int__(name)

    def __repr__(self):
        return 'Office %s' % self.name


class LivingSpace(Room):
    capacity = 4

    def __init__(self, name):
        super(LivingSpace, self).__int__(name)

    def __repr__(self):
        return 'LivingSpace %s' % self.name
