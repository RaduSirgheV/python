#!/usr/bin/python2.7

import csv


class ReadCSV(object):

    def __init__(self, text_file):
        with open(text_file) as read_file:
            self.r_csv_file = csv.reader(read_file, delimiter=',')
            self.list = []
            for row in self.r_csv_file:
                self.list.append(row)

    def csv_dict_reader(self):
        list_person = self.list[1:]
        return list_person

    def show_person(self, person_identifier=None):
        employees_list = self.csv_dict_reader()
        displayed_person = []
        for person in employees_list:
            if person_identifier is None:
                displayed_person.append(person)
            elif person[0] == person_identifier:
                displayed_person.append(person)
        if len(displayed_person) > 0:
            for show_person in displayed_person:
                person = "Name:          {} {}\nDepartament:   {}\nPosition:      {}\nAge:           {}\nProjects:      {}"\
                    .format(show_person[0], show_person[1], show_person[2], show_person[3], show_person[4], show_person[5])
                print "="*50 + "\n" + person + "\n" + "="*50
        elif len(displayed_person) == 0:
            return "Not a person by name \'" + person_identifier + "\'"


class ModifyCSV(ReadCSV):

    def __init__(self, text_file):
        ReadCSV.__init__(self, text_file)
        self.text_file = text_file

    def modif_data_person(self, args, key_list):
        mod_list = []
        for person in self.csv_dict_reader():
            if person[0] == args[0]:
                person[key_list.index(args[1])] = str(args[2])
                mod_list.append(person)
            else:
                mod_list.append(person)
        return mod_list

    def add_modif_in_file(self, args):
        key_list = ["first_name", "last_name", "departament", "position", "age", "projects"]
        with open(self.text_file, 'w') as w_file:
            w = csv.writer(w_file)
            w.writerow(key_list)
            for x in self.modif_data_person(args, key_list):
                w.writerow(x)
        print "Modified!!"


class DeletePersonCSV(ReadCSV):

    def __init__(self, text_file):
        ReadCSV.__init__(self, text_file)
        self.text_file = text_file

    def del_person(self, person_id):
        mod_list = []
        for person in self.csv_dict_reader():
            if person[0] != person_id:
                mod_list.append(person)
        return mod_list

    def add_modif_in_file(self, person_identifier):
        key_list = ["first_name", "last_name", "departament", "position", "age", "projects"]
        with open(self.text_file, 'w') as w_file:
            w = csv.writer(w_file)
            w.writerow(key_list)
            for x in self.del_person(person_identifier):
                w.writerow(x)
        print "Deleted!!"


