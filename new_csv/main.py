#! /usr/bin/python2

import os
import argparse
from classes.qacsv import ReadCSV, ModifyCSV, AddPersonCSV, DeletePersonCSV

path = os.path.abspath(__file__)
path = path.replace('main.py', '')
_csv_file_path = path + 'file/data.csv'


def exec_function():
    parser = argparse.ArgumentParser(description='Process the task')
    parser.add_argument('-g', '--afisa', default=None, type=str, required=False, nargs='?', const="empty",
                        help='Afiseaza un anumit angajat')
    parser.add_argument('-m', '--modifica', nargs='+', type=str, default=None, required=False,
                        help='Modifica datele unui anumit angajat')
    parser.add_argument('-a', '--adding', nargs='+', type=str, default=None, required=False,
                        help='Adaugarea unui angajat (first_name,last_name,departament,position,age,projects)')
    parser.add_argument('-d', '--delete', type=str, default=None, required=False,
                        help='Sterge un anumit angajat')

    args = parser.parse_args()
    print args
    if args.afisa is "empty":
        r = ReadCSV(_csv_file_path)
        r.show_person(args.afisa)
    elif args.afisa is not None:
        g = ReadCSV(_csv_file_path)
        g.show_person(args.afisa)

    if args.modifica is not None:
        m = ModifyCSV(_csv_file_path)
        m.add_modif_in_file(args.modifica)

    if args.adding is not None:
        a = AddPersonCSV(_csv_file_path)
        a.add_person_to_csv(args.adding)

    if args.delete is not None:
        d = DeletePersonCSV(_csv_file_path)
        d.add_modif_in_file(args.delete)


exec_function()
