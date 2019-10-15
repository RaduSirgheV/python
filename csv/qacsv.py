#!/usr/bin/python2.7

import csv


class BaseClass(object):
    def __init__(self, text_file='/home/noction/CSV/python/csv/data.csv'):
        with open(text_file) as read_file:
            self.r_csv_file = csv.DictReader(read_file)
            print self.r_csv_file

class ReadCSV(BaseClass):


    def csv_dict_reader(self):
        list_person = []
        reader = csv.DictReader(self.r_csv_file, delimiter=',')
        for line in reader:
            list_person.append(line)
        return list_person

    def show_person(self, person_identifier=None):
        employees_list = self.csv_dict_reader()
        if person_identifier is None:
            return employees_list
        else:
            displayed_person = []
            for person in employees_list:
                if person['first_name'] == person_identifier:
                    displayed_person.append(person)
            if len(displayed_person) > 0:
                for show_person in displayed_person:
                    return "Name: {} {}\nDepartament: {}\nPosition: {}\nAge: {}\nProjects: {}".format(show_person['first_name'], show_person['last_name'], show_person['departament'], show_person['position'], show_person['age'], show_person['projects'])
            elif len(displayed_person) == 0:
                return "Not a person by name \'" + person_identifier + "\'"


class ModifyCSV(ReadCSV):

    # def __init__(self, text_file='/home/noction/CSV/python/csv/data.csv'):
    #     super(ModifyCSV, self).__init__(text_file)
    #     self.text_file_to_write = text_file
    #     self.column_arg = sys.argv[3]
    #     self.content_arg = sys.argv[4]

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


class DeletePersonCSV(ReadCSV):

    def __init__(self, text_file='/home/noction/CSV/python/csv/data.csv'):
        super(DeletePersonCSV, self).__init__(text_file)
        self.text_file_to_write = text_file

    def del_person(self):
        mod_list = []
        for person in self.csv_dict_reader():
            if person['first_name'] != self.name_arg:
                mod_list.append(person)
        return mod_list

    def add_modif_in_file(self):
        key_list = ["first_name", "last_name", "departament", "position", "age", "projects"]
        with open(self.text_file_to_write, 'w') as w_file:
            w = csv.DictWriter(w_file, key_list)
            w.writeheader()
            for x in self.del_person():
                w.writerow(x)
        return "Deleted!!"




# https://stackoverflow.com/questions/29725932/deleting-rows-with-python-in-a-csv-file