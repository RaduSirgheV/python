#! /usr/bin/python2

import os,argparse
from classes.qacsv import ReadCSV, ModifyCSV, DeletePersonCSV

path = os.path.abspath(__file__)
path = path.replace('main.py', '')
_csv_file_path = path + 'file/data.csv'


def exec_function():
    parser = argparse.ArgumentParser(description='Process the task')
    parser.add_argument('-a', '--afisa', default=None, type=str, required=False,
                        help='Afiseaza un anumit angajat')
    parser.add_argument('-m', '--modifica', nargs='+', type=str, default=None, required=False,
                        help='Modifica datele unui anumit angajat')
    parser.add_argument('-d', '--delete', type=str, default=None, required=False,
                        help='Sterge un anumit angajat')

    args = parser.parse_args()
    print args

    if args.afisa is None:
        r = ReadCSV(_csv_file_path)
        return r.show_person(args.afisa)
    elif args.afisa is not None:
        r = ReadCSV(_csv_file_path)
        return r.show_person(args.afisa)

    if args.modifica is not None:
        m = ModifyCSV(_csv_file_path)
        return m.add_modif_in_file(args.modifica)

    if args.delete is not None:
        d = DeletePersonCSV(_csv_file_path)
        return d.add_modif_in_file(args.delete)


print(exec_function())
