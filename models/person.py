class Person(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Room %s>" % self.name


class Staff(Person):

    job_type = "Staff"

    def __init__(self, name):
        super(Staff, self).__init__(name)

    def __repr__(self):
        return "<Staff %s>" % self.name


class Fellow(Person):

    job_type = "Fellow"

    def __init__(self, name):
        super(Fellow, self).__init__(name)

    def __repr__(self):
        return "Fellow %s>" % self.name
