#!/usr/bin/python2.7

import csv
import sys

# exec_arg = sys.argv[1]
exec_arg = "-a"
# name_arg = sys.argv[2]
name_arg = "Radu"
# column_arg = sys.argv[3]
column_arg = "age"
# content_arg = sys.argv[4]
content_arg = "25"


class ReadCSV(object):

    def __init__(self, text_file='/home/radumd/project/python/csv/data.csv'):
        with open(text_file) as read_file:
            self.r_csv_file = read_file.readlines()
            self.read_arg = exec_arg
            self.name_arg = name_arg
        self.text_file_to_write = text_file
        self.column_arg = column_arg
        self.content_arg = content_arg

    def csv_dict_reader(self):
        list_person = []
        reader = csv.DictReader(self.r_csv_file, delimiter=',')
        for line in reader:
            list_person.append(line)
        return list_person

    def show_person(self):
        if self.read_arg is not None:
            for person in self.csv_dict_reader():
                if person['first_name'] == self.name_arg:
                    return "Name: {} {}\nDepartament: {}\nAge: {}\nProjects: {}".format(person['first_name'], person['last_name'], person['departament'], person['age'], person['projects'])


class ModifyCSV(ReadCSV):

    def __init__(self, text_file='/home/radumd/project/python/csv/data.csv'):
        super(ModifyCSV, self).__init__(text_file)
        self.text_file_to_write = text_file
        self.column_arg = column_arg
        self.content_arg = content_arg

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
        key_list = ["first_name", "last_name", "departament", "age", "projects"]
        with open(self.text_file_to_write, 'w') as w_file:
            w = csv.DictWriter(w_file, key_list)
            w.writeheader()
            for x in self.modif_data_person():
                w.writerow(x)
        return "Modified!!"


def res_function():
    if exec_arg == "-a":
        c = ReadCSV()
        print c.show_person()
        print "Read"
    elif exec_arg == "-m":
        c = ModifyCSV()
        print c.add_modif_in_file()
        print "Write"
    else: print "Incorect argument"
# t = ModifyCSV()
# print t.add_modif_in_file()
