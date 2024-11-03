class WordsFinder:
    def __init__(self, *files_names):
        self.file_name = list(files_names)

    def get_all_words(self):
        all_worlds = {}
        for file_name in self.file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = file.read().lower()
                for puncts in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    words = words.replace(puncts, '')
                words = words.split()
                all_worlds[file_name] = words
        return all_worlds


    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word)
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('text'))

