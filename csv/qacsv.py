#!/usr/bin/python2.7

import csv
import sys

exec_arg = sys.argv[1]


class ReadCSV(object):

    def __init__(self, text_file='/home/radu/Projects/python/csv/data.csv'):
        with open(text_file) as read_file:
            self.r_csv_file = read_file.readlines()
            self.name_arg = sys.argv[2]

    def csv_dict_reader(self):
        list_person = []
        reader = csv.DictReader(self.r_csv_file, delimiter=',')
        for line in reader:
            list_person.append(line)
        return list_person

    def show_person(self):
        for person in self.csv_dict_reader():
            if person['first_name'] == self.name_arg:
                return "Name: {} {}\nDepartament: {}\nPosition: {}\nAge: {}\nProjects: {}".format(person['first_name'],
                                                                                    person['last_name'],
                                                                                    person['departament'],
                                                                                    person['position'],
                                                                                    person['age'],
                                                                                    person['projects'])
            else:
                return "Not a person by name \'" + self.name_arg + "\'"


class ModifyCSV(ReadCSV):

    def __init__(self, text_file='/home/radu/Projects/python/csv/data.csv'):
        super(ModifyCSV, self).__init__(text_file)
        self.text_file_to_write = text_file
        self.column_arg = sys.argv[3]
        self.content_arg = sys.argv[4]

    def modif_data_person(self):
        mod_list = []
        for person in self.csv_dict_reader():
            if person['first_name'] == self.name_arg:
                person[self.column_arg] = self.content_arg
                mod_list.append(person)
            else:
                mod_list.append(person)
        return mod_list

    def add_modif_in_file(self):
        key_list = ["first_name", "last_name", "departament", "position", "age", "projects"]
        with open(self.text_file_to_write, 'w') as w_file:
            w = csv.DictWriter(w_file, key_list)
            w.writeheader()
            for x in self.modif_data_person():
                w.writerow(x)
        return "Modified!!"


def exec_function():
    if exec_arg == "-a":
        r = ReadCSV()
        return r.show_person()
    if exec_arg == "-m":
        m = ModifyCSV()
        return m.add_modif_in_file()
    else:
        return "Incorect argument"


print(exec_function())
