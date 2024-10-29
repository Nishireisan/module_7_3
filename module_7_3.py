class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list()
        for i in file_names:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        k = ''
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                stroka = file.read()
                stroka_lower = stroka.lower()
                punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ' '\n']
                for j in punctuation:
                    stroka_lower = stroka_lower.replace(j, ' ')
                words = stroka_lower.split()
                all_words.update({i: words})
        return all_words

    def find(self, word):
        h_dict = {}
        w = word.lower()
        for i, words in self.get_all_words().items():
            # print(i, words)
            k = 0
            # return {i: words.index(w)+1}
            while k < len(words):
                if words[k] != w:
                    k += 1
                elif words[k] == w:
                    k += 1
                    h_dict.update({i: k})
                    break
            if k == len(words):
                h_dict.update({i: 'Такого слова нет'})
            words.clear()
        return h_dict

    def count(self, word):
        h_dict = {}
        w = word.lower()
        for i, words in self.get_all_words().items():
            k = 0
            for j in words:
                if j == w:
                    k += 1
                else:
                    continue
            if k == 0:
                h_dict.update({i: 'Такого слова нет'})
            else:
                h_dict.update({i: k})
        return h_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TExT')) # 3 слово по счёту
print(finder2.count('texT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder1 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
