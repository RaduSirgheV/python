#!/usr/bin/python2.7

import csv

from new_csv.classes.record import Record
from record import Record


class BaseClass(object):
    def __init__(self, text_file):
        with open(text_file) as read_file:
            self.r_csv_file = csv.DictReader(read_file)
            self.list = []
            for row in self.r_csv_file:
                self.list.append(Record(row))


class ReadCSV(BaseClass):

    def formatting_person_text(self, person):
        text = "Numele: {} {}\nDepartamentu: {}\nPozitia: {}\nVirsta: {}\nProiectele: {}".format(person.name, person.family, person.departament, person.position, person.age, person.projects)
        return text

    def show_person(self, person_identifier=None):
        employees_list = self.list
        displayed_person = []
        for person in employees_list:
            if person_identifier is "empty":
                displayed_person.append(person)
            elif person_identifier == person.name or person_identifier == person.family:
                displayed_person.append(person)
        print "=" * 50
        for person in displayed_person:
            print self.formatting_person_text(person)
            print "=" * 50


class ModifyCSV(BaseClass):

    def __init__(self, text_file):
        super(ModifyCSV, self).__init__(text_file)
        self.text_file = text_file

    def modif_data_person(self, args):
        mod_list = []
        employees = self.list
        for person in employees:
            if args[0] == person.name:
                column = args[1]
                person.column = str(args[2])
                mod_list.append(person)
            else:
                mod_list.append(person)
        return mod_list

    def add_modif_in_file(self, args):
        with open(self.text_file, 'w') as w_file:
            fields = ["first_name", "last_name", "departament", "position", "age", "projects"]
            w = csv.DictWriter(w_file, fields)
            w.writeheader()
            print self.modif_data_person(args)
            for x in self.modif_data_person(args):
                w.writerow(x)
        print "Modified!!"


class AddPersonCSV(ReadCSV):

    def __init__(self, text_file):
        ReadCSV.__init__(self, text_file)
        self.text_file = text_file

    def add_person_to_csv(self, argument):
        key_list = ["first_name", "last_name", "departament", "position", "age", "projects"]
        if len(argument) == 6:
            with open(self.text_file, 'w') as w_file:
                w = csv.writer(w_file)
                w.writerow(key_list)
                for x in self.del_header_row():
                    w.writerow(x)
                w.writerow(argument)
            print "Added!!"
        else:
            print "Too much or too little data"


class DeletePersonCSV(ReadCSV):

    def __init__(self, text_file):
        ReadCSV.__init__(self, text_file)
        self.text_file = text_file

    def del_person(self, person_id):
        mod_list = []
        for person in self.del_header_row():
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


