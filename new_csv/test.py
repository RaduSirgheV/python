from classes.qacsv import BaseClass
x = BaseClass('file/data.csv')
print x.list

print x.list[0].name
x.list[0].name = 50
