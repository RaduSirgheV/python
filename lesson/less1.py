#!/usr/bin/python2.7

s1 = s2 = s3 = "String"

def reverse_one(s1):
    l = ""
    for i in s1:
        l = i + l
        # print (l)
    return l

def reverse_two(s2):
    return s2[::-1]

def reverse_three(s3):
    return ''.join(reversed(s3))

if __name__ == '__main__':
    test_str = raw_input('What is your str ?')
    print(reverse_one(test_str))

# print(("String One:   {};\nString Two:   {};\nString Three: {};").format(reverse_one(s1), reverse_two(s2), reverse_three(s3)))
