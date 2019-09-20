#!/usr/bin/python2.7
# coding=utf-8
import string
with open('/home/radumd/PycharmProjects/Less/text3.txt', 'r') as text_file:
    text = text_file.readlines()
    print 'have open the file for reading'
    print type(text)
    # print text
    # text_file.close()
# text_file = open('/home/radumd/PycharmProjects/Less/text2.txt', 'r')
# text_file = open('/home/radumd/PycharmProjects/Less/text3.txt', 'r')


def read_file(text_file):
    word_list = []
    for line in text_file:
        # print line
        for word in line.split():
            _word = word.decode('utf-8')
            # print _word
            word_list.append(_word)
    return word_list

# print read_file(text)
# readFile = read_file(text_file)
# print readFile
#
# def decode():
#     list = []
#     for word in readFile:
#         list.append(unicode(word, 'cp1251'))
#     return list
#
# print decode()
#
def clean_words(_list):
    # word_list = read_file(text_file)
    letters = string.ascii_letters
    cleaned_list = []
    for word in _list:
        for character in word:
            if character.isalpha():
                print '{} char is letter'.format(character.encode('utf-8'))
            else:
                print '{} is not a letter'.format(character)
                word = word.replace(character, '')
        print word
        cleaned_list.append(word)
    return cleaned_list

for w in clean_words(read_file(text)):
    print w
#
#
# cleaned_words = clean_words()
#
#
# def anagram():
#     words = cleaned_words
#     list_anagram = []
#     for word in words:
#         if len(word) >= 2:
#             if word.lower() == word[::-1].lower():
#                 list_anagram.append(word)
#     return "Count: {}; Words: {}".format(len(list_anagram), list_anagram)
#
#
# def upper_in_word():
#     wordsUp = cleaned_words
#     upper_list = []
#     for wordUp in wordsUp:
#         # print wordUp[:1]
#         if wordUp[:1].isupper():
#             upper_list.append(wordUp)
#     return "Count: {}; Words: {}".format(len(upper_list), upper_list)
#
#
# print "1. Anagram\n {}.\n\n2.First letter is uppercase\n {}".format(anagram(), upper_in_word())
