class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                line = file.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    line = line.replace(j, '')
                words = line.split()
                all_words[i] = words
        return all_words

    def find(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_[name] = words.index(word.lower()) + 1
        return dict_

    def count(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            dict_[name] = words.count(word.lower())
        return dict_
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))