"""
Script for training added words
"""
import os
import random
import time
import pyttsx3

from db_repo.db_handle import get_allinfo_db
from db_repo.db_handle import get_specific_words

from toolkit.select2learn import Select2Learn
from toolkit.sents_similarity import sents_similarity
from toolkit.get_sents import get_sents
from toolkit.translate_tool import translate_tool


from trainings.t_word_designer import t_word_designer
from trainings.t_word_eng2rus import t_word_eng2rus
from trainings.t_word_rus2eng import t_word_rus2eng
from trainings.t_word_engwrite import t_word_engwrite

# function for clearing terminal window
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

# number_words to learn
number_words = 5

while True:
    print("Training starts. Go ahead, improve your English!")
    # get words learning stat
    
    while True:
        # selection words to learn
        w_stat = get_allinfo_db('w_stat')
        learning = Select2Learn(number_words, w_stat)
        words = learning.action('select words to learn')[0]
        
        # get info about words from dictionary
        dict_info = get_specific_words('w_dictionary',('word_eng', 'definition', 'syns', 'antons', 'example'), tuple(words))
        print('definitions\n')

        for word in dict_info:
            print(word[0], ' ', word[1], '\n')
        print('-----------------------------------------------------')
        print('synonyms\n')
        for word in dict_info:
            print(word[0], ' ', word[2], '\n')

        print('-----------------------------------------------------')
        print('antonyms\n')
        for word in dict_info:
            print(word[0], ' ', word[3], '\n')

        print('-----------------------------------------------------')
        print('examples\n')
        for word in dict_info:
            print(word[0], ' ', word[4], '\n')
        print('-----------------------------------------------------')
        while True:
            cont = input("Let's exercise? [y/n] ")
            if cont.lower() == 'y' or cont.lower() == 'n':
                break
            else:
                print("Please, choose y or n")
                continue
        if cont == 'y':
            clearConsole()
            for word in words:
                t_word_designer(word)
                time.sleep(2)
                clearConsole()
                t_word_eng2rus(word)
                time.sleep(2)
                clearConsole()
                t_word_rus2eng(word)
                time.sleep(2)
                clearConsole()
                t_word_engwrite(word)
                learning = Select2Learn(number_words, w_stat, word=word)
                learning.action('update stat in database')
                print(f"""Congrats! The word "{word}" is learned successfully!""")
                time.sleep(2)
        break
    
    while True:
        cont = input("Would you like to continue learning a new banch of words? [y/n] ")
        if cont.lower() == 'y' or cont.lower() == 'n':
            break
        else:
            print("Please, choose y or n")
            continue
    
    if cont == 'y':
        continue
    else:
        break

number_sents = 5

ask_user = input("Would you like to train your words with sentences?  [y/n] ")
while True:
    if ask_user.lower() == 'y' or ask_user.lower() == 'n':
        break
    else:
        print("Please choose y or n")
        continue
if ask_user == 'y':
    while True:
        print("Training with sentances starts. Go ahead, improve your English!")
        # get words learning stat

        while True:
            w_stat = get_allinfo_db('w_stat')
            learning = Select2Learn(number_words, w_stat)
            words = learning.action('select words to learn')[1]

            # code to train sentences
            for word in words:
                sents = random.sample(get_sents(word), number_sents)
                for sent in sents:
                    while True:
                        rus_translated = translate_tool(sent)
                        print(f"Word yo have to use - {word}")
                        print("Write translation into English:")
                        pyttsx3.speak(rus_translated[1])
                        print(rus_translated[1])
                        user_sent = input("---> ")
                        print(f'The right translation: {rus_translated[0]}')
                        print(f"Similarity with right answer is {sents_similarity(sent, user_sent)}")
                        ask_user = input("Continue? [y/n] ")
                        while True:
                            if ask_user.lower() == 'y' or ask_user.lower() == 'n':
                                break
                            else:
                                print("Please choose y or n")
                                continue
                        if ask_user == 'y':
                            break
                        else:
                            continue
                learning = Select2Learn(number_words, w_stat, word=word)
                learning.action('update stat in database')        
            break
        
        while True:
            cont = input("Would you like to continue training with sentences? [y/n] ")
            if cont.lower() == 'y' or cont.lower() == 'n':
                break
            else:
                print("Please, choose y or n")
                continue
        
        if cont == 'y':
            continue
        else:
            break





