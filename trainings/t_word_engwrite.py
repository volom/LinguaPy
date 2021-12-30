"""
Exercise for writing English word which is sounded
"""
import pyttsx3
import sys
sys.path.append("../LinguaPy")
from db_repo.db_handle import get_specific_word

def t_word_engwrite(word):
    while True:
        word_init = re.sub(r'\s+', ' ', word).strip()

        print("Write the word in English")
        # get info from dictionary
        right_translation = get_specific_word('w_translated', 'word_rus', word)[0][0]
        print(right_translation)
        pyttsx3.speak(right_translation)
        
        user_input = input('---> ')

        if user_input.lower() == re.sub(r'\s+', ' ', word).strip().lower():
            print("Congrats! You write the word right!")
            break
        else:
            print("Wrong writing :( please, try again...")
            continue