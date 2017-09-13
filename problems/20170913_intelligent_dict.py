import re


class IntelligentDict:
    def __init__(self):
        self.dictionary = dict()

    def __setitem__(self, key, value):
        self.dictionary.__setitem__(key, value)

    def __getitem__(self, key):
        self.dictionary.__getitem__(key)

    def _find_anagram(self, key):
        pattern = sorted(set(key.lower()))

    def _find_additionl(self, key):
        pattern = r"".join(["".join(['[', letter, '|.]']) for letter in key])

    def _find_closest(self, key):
        pattern = r"".join(["".join(['[', letter, '|.]?']) for letter in key])
