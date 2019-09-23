import sys


class ReadFile(object):
    # with open('/home/rsirghe/my/python/lesson/text1.txt', 'r') as text_file:
    #     text = text_file.readlines()

    def __init__(self, text_file='/home/rsirghe/my/python/lesson/text1.txt'):
        with open(text_file, 'r') as text_file:
            self.text_file = text_file.readlines()

    def read_file(self):
        word_list = []
        for line in self.text_file:
            for word in line.split():
                _word = word.decode('utf-8')
                word_list.append(_word)
        return word_list

    def clean_words(self):
        cleaned_list = []
        for word in self.read_file():
            for character in word:
                if character.isalpha():
                    pass
                else:
                    word = word.replace(character, '')
            cleaned_list.append(word)
        return cleaned_list

r = ReadFile()
print r.clean_words()
