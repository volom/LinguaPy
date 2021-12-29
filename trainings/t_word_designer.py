"""
Exercise for designing word with given its letters in random order
"""
import random
import pyttsx3
from db_repo.db_handle import get_specific_word

def t_word_designer(word):
    while True:
        word_init = word
        word_shuffle = list(word)
        random.shuffle(word_shuffle)

        print("Design the word")
        translated_word = get_specific_word('w_translated', 'word_rus', word)[0][0]
        print(translated_word)
        pyttsx3.speak(word_init)
        print(' | '.join(word_shuffle))
        word_input = input('---> ')

        if word_input.lower() == word_init.lower():
            print("Congrats! You designed the word right!")
            break
        else:
            print("Wrong designing :( please, try again...")
            continue
