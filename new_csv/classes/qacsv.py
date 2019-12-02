#!/usr/bin/python2.7

import csv

from record import Record, CsvKeys



class BaseClass(object):
    def __init__(self, text_file):
        with open(text_file) as read_file:
            self.r_csv_file = csv.DictReader(read_file)
            self.list = []
            for row in self.r_csv_file:
                self.list.append(Record(row))


class ReadCSV(BaseClass):

    def formatting_person_text(self, person):
        text = "Numele: {} {}\nDepartmentu: {}\nPozitia: {}\nVirsta: {}\nProiectele: {}".format(person.name, person.family, person.department, person.position, person.age, person.projects)
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
            _id = args[0]
            if _id in (person.family, person.name):
                key_name = args[1]
                val = args[2]

                # check_keys:
                if key_name == CsvKeys.name:
                    person.name = val
                elif key_name == CsvKeys.family:
                    person.family = val
                elif key_name == CsvKeys.department:
                    person.department = val
                elif key_name == CsvKeys.age:
                    person.age = int(val)
                elif key_name == CsvKeys.position:
                    person.position = val
                elif key_name == CsvKeys.projects:
                    person.projects = val
                # person.change_key_val(key=key_name, val=val)
                mod_list.append(person)
            else:
                mod_list.append(person)
        return mod_list

    def add_modif_in_file(self, args):
        with open(self.text_file, 'w') as w_file:
            fields = self.list[0].list_key()
            w = csv.DictWriter(w_file, fields)
            w.writeheader()
            for x in self.modif_data_person(args):
                w.writerow(x.record)
        print "Modified!!"


class AddPersonCSV(BaseClass):

    def __init__(self, text_file):
        super(AddPersonCSV, self).__init__(text_file)
        self.text_file = text_file

    def new_person(self, person_data):
        list_key = self.list[0].list_key()
        person_dict = dict(zip(list_key, person_data))
        return person_dict

    def add_person_to_csv(self, person_data):
        if len(person_data) == 6:
            with open(self.text_file, 'w') as w_file:
                fields = self.list[0].list_key()
                w = csv.DictWriter(w_file, fields)
                w.writeheader()
                for x in self.list:
                    w.writerow(x.record)
                w.writerow(self.new_person(person_data))
            print "Added!!"
        else:
            print "Too much or too little data"


class DeletePersonCSV(BaseClass):

    def __init__(self, text_file):
        super(DeletePersonCSV, self).__init__(text_file)
        self.text_file = text_file

    def del_person(self, person_id):
        employees = self.list
        mod_list = []
        for person in employees:
            if person_id != person.name:
                mod_list.append(person)
        return mod_list

    def add_modif_in_file(self, person_identifier):
        with open(self.text_file, 'w') as w_file:
            fields = self.list[0].list_key()
            w = csv.DictWriter(w_file, fields)
            w.writeheader()
            for x in self.del_person(person_identifier):
                w.writerow(x.record)
        print "Deleted!!"


