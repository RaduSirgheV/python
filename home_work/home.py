import sys


class ReadFile(object):
    # with open('/home/rsirghe/my/python/lesson/text1.txt', 'r') as text_file:
    #     text = text_file.readlines()

    def __init__(self, text_file='/home/rsirghe/my/python/lesson/text3.txt'):
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

    def anagram(self):
        list_anagram = []
        for word in self.clean_words():
            word.encode('utf-8')
            if len(word) >= 2:
                if word.lower() == word[::-1].lower():
                    res_word = word
                    list_anagram.append(res_word)
        return list_anagram

    def anagram_res(self):
        return repr([x.encode(sys.stdout.encoding) for x in self.anagram()]).decode('string-escape')

    def anagram_cnt(self):
        return len(self.anagram())

    def title_word(self):
        upper_list = []
        for wordUp in self.clean_words():
            if wordUp[:1].isupper():
                upper_list.append(wordUp)
        return upper_list

    def title_res(self):
        return repr([x.encode(sys.stdout.encoding) for x in self.title_word()]).decode('string-escape')

    def title_cnt(self):
        return len(self.title_word())

    def show_anagram(self):
        return "Angram:\nCount: {}. Words: {}.\n".format(self.anagram_cnt(), self.anagram_res())

    def show_title(self):
        return "Title words:\nCount: {}. Words: {}.\n".format(self.title_cnt(), self.title_res())

    def results(self):
        list_res = (self.show_anagram(), self.show_title())
        for i in list_res:
            print i

r = ReadFile()
r.results()
