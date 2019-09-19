class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_person(self):
        print "My name is {} {}".format(self.first_name, self.last_name)


class Cars(object):
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model

    def print_car(self):
        print "Car: {} {}".format(self.mark, self.model)

