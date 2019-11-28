
class CsvKeys(object):

    name = 'first_name'
    family = 'last_name'
    age = 'age'
    department = 'departament'
    position = 'position'
    projects = 'projects'

    allowed_keys = 'first_name,last_name,departament,age,position,projects'.split(',')

class Record(object):

    def __init__(self, record):
        self._record = record

    def list_key(self):
        return self.record.keys()

    def change_key_val(self, key, val):
        if key in self.record:
            self._record[key] = val
        else:
            raise ValueError('Do not have such key defined in record {}'.format(self.record.keys()))

    @property
    def record(self):
        return self._record

    @property
    def name(self):
        return self._record[CsvKeys.name]

    @property
    def family(self):
        return self._record[CsvKeys.family]

    @property
    def departament(self):
        return self._record[CsvKeys.department]

    @property
    def position(self):
        return self._record[CsvKeys.position]

    @property
    def age(self):
        return self._record['age']

    @property
    def projects(self):
        return self._record['projects']

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._record['first_name'] = new_name
            print "have changed the name of Employee"
        else:
            raise ValueError('You have passed an invalid value for the name field: {}, expected str'.format(type(new_name)))

    @family.setter
    def family(self, new_family):
        if isinstance(new_family, str):
            self._record['last_name'] = new_family
            print "Have changed the failmy of Employee"
        else:
            raise ValueError('You have passed an invalid value for the family field: {}, expected str'.format(type(new_family)))

    @departament.setter
    def departament(self, new_departament):
        if isinstance(new_departament, str):
            self._record['departament'] = new_departament
            print "Have changed the departament of Employee"
        else:
            raise ValueError('You have passed an invalid value for the department field: {}, expected str'.format(type(new_departament)))

    @position.setter
    def position(self, new_position):
        if isinstance(new_position, str):
            self._record['position'] = new_position
            print "Have changed the position of Employee"
        else:
            raise ValueError('You have passed an invalid value for the position field: {}, expected str'.format(type(new_position)))

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            self._record['age'] = new_age
            print "Have changed the age of Employee"
        else:
            raise ValueError('You have passed an invalid value for the age field: {}, expected int'.format(type(new_age)))

    @projects.setter
    def projects(self, new_projects):
        if isinstance(new_projects, str):
            self._record['projects'] = new_projects
            print "Have changed the projects of Employee"
        else:
            raise ValueError('You have passed an invalid value for the projects field: {}, expected str'.format(type(new_projects)))