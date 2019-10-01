#!/usr/bin/python2.7

import csv
import sys

read_arg = sys.argv[1]
# name_arg = sys.argv[2]


class ReadCSV(object):

    def __init__(self, text_file='/home/rsirghe/my/python/csv/data.csv'):
        with open(text_file) as text_file:
            self.csv_file = text_file.readlines()
            self.read_arg = read_arg
            self.name_arg = name_arg

    def csv_dict_reader(self):
        """
        Read a CSV file using csv.DictReader
        """
        list_person = []
        reader = csv.DictReader(self.csv_file, delimiter=',')
        for line in reader:
            list_person.append(line)
        return list_person

    def show_person(self):
        if self.read_arg is not None:
            for person in self.csv_dict_reader():
                if person['first_name'] == self.name_arg:
                    print
            # print self.csv_dict_reader()


t = ReadCSV()
t.show_person()

# if __name__ == "__main__":
#     with open("data.csv") as f_obj:
#         csv_dict_reader(f_obj)
