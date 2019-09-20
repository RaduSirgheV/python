#!/usr/bin/python2.7
# coding=utf-8
import sys
# text file range 1-3
with open('/home/rsirghe/my/python/lesson/text1.txt', 'r') as text_file:
    text = text_file.readlines()


def read_file(text_file):
    word_list = []
    for line in text_file:
        for word in line.split():
            _word = word.decode('utf-8')
            word_list.append(_word)
    return word_list


def clean_words(_list):
    cleaned_list = []
    for word in _list:
        for character in word:
            if character.isalpha():
                pass
            else:
                word = word.replace(character, '')
        cleaned_list.append(word)
    return cleaned_list


word_list = read_file(text)


def anagram(_list):
    list_anagram = []
    for word in _list:
        word.encode('utf-8')
        if len(word) >= 2:
            if word.lower() == word[::-1].lower():
                res_word = word
                list_anagram.append(res_word)
    return list_anagram


cleaned_words = clean_words(word_list)


def anagram_count(cnt):
    return len(cnt)


anagram_words = anagram(cleaned_words)
show_anagram_words = repr([x.encode(sys.stdout.encoding) for x in anagram_words]).decode('string-escape')
anagram_count = anagram_count(anagram_words)


def show_anagram(cnt, word):
    return 'Count: {}. Words list: {}.\n'.format(cnt, word)


print show_anagram(anagram_count, show_anagram_words)


def title_word(upper_word):
    upper_list = []
    for wordUp in upper_word:
        if wordUp[:1].isupper():
            upper_list.append(wordUp)
    return upper_list


def title_word_count(cnt):
    return len(cnt)


upper_words = title_word(cleaned_words)
words_title = repr([x.encode(sys.stdout.encoding) for x in upper_words]).decode('string-escape')
title_word_count = title_word_count(upper_words)


def show_title_words(cnt, word):
    return 'Count: {}. Words list: {}.\n'.format(cnt, word)


print show_title_words(title_word_count, words_title)
