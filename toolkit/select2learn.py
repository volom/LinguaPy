"""
Tool is acting as words selector for learning and updating statistics
"""

import sys
sys.path.append("../LinguaPy")
from db_repo.db_handle import get_allinfo_db, update_w_stat

class Select2Learn:

    def __init__(self, number_words, w_stat, word='start'):
        self.number_words = number_words
        self.w_stat = w_stat
        self.word = word
        self.sorted = sorted
    def __get_words2learn(self, w_stat, number_words):
        result_s = sorted(w_stat, key=lambda x: x[1])[:number_words]
        result_s = [x[0] for x in result_s]

        result_l = sorted(w_stat, key=lambda x: x[1])[number_words-1:]
        result_l = [x[0] for x in result_l]
        return result_s, result_l
    
    def __update_w_stat(self, word):
        update_w_stat(word)

    def action(self, method):
        if method == 'select words to learn':
            return self.__get_words2learn(self.w_stat, self.number_words)
        elif method == 'update stat in database':
            return self.__update_w_stat(self.word)
