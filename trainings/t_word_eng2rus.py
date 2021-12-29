"""
Exercise for translation word from English to russian
"""
import re
import random
import pyttsx3
import sys
sys.path.append("../LinguaPy")
from db_repo.db_handle import get_columns_info_db
from db_repo.db_handle import get_specific_word

def t_word_eng2rus(word):
    while True:
        word_init = word

        print("Select proper translation [1-5]")
        print(word_init)
        pyttsx3.speak(word_init)
        # get info from dictionary
        all_words_rus = [x[0] for x in get_columns_info_db('w_translated', ('word_rus'))]
        right_translation = get_specific_word('w_translated', 'word_rus', word)[0][0]
        all_words_rus.remove(right_translation)
        banch_words = random.sample(all_words_rus, 4)
        banch_words.append(right_translation)
        random.shuffle(banch_words)
        indexs = ['1', '2', '3', '4', '5']
        choices = "".join("{0} - {1} | ".format(x,y) for x,y in zip(indexs, banch_words))
        print(choices)
        
        while True:
            try:
                number_input = input('---> ')
                re.match(r'[1-5]', number_input).group()
            except:
                print("Please, choice number from 1 to 5..")
                continue
            else:
                break

        if int(number_input) == banch_words.index(right_translation)+1:
            print("Congrats! You translated the word right!")
            break
        else:
            print("Wrong translation :( please, try again...")
            continue
