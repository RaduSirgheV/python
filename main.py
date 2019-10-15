#! /usr/bin/python2

import os, argparse
from csv.qacsv import ReadCSV, ModifyCSV, DeletePersonCSV


path = os.path.abspath(__file__)
path = path.replace('main.py','')
print path
_csv_file_path = path + 'csv/data.csv'

def exec_function():
    parser = argparse.ArgumentParser(description='Process the task')
    parser.add_argument('-a','--afisa', type=str, default=None, required=False, help='Afiseaza un anumit angajat sau pe toti')
    # parser.add_argument('--sum', dest='accumulate', action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print args
    if args.afisa is None:
        r = ReadCSV(_csv_file_path)
        return r.show_person()
    else:
        r=ReadCSV(_csv_file_path)
        return r.show_person(args.afisa)
    # elif exec_arg == "-m":
    #     m = ModifyCSV(_csv_file_path)
    #     return m.add_modif_in_file()
    # elif exec_arg == "-d":
    #     d = DeletePersonCSV(_csv_file_path)
    #     return d.add_modif_in_file()
    # else:
    #     return "Incorect argument"


print(exec_function())