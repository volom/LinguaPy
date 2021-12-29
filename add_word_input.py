#https://deep-translator.readthedocs.io/en/latest/usage.html

"""
Script for adding English word to the dictionary 
by entering a value to the terminal
"""

from threading import Thread
import time
from datetime import datetime
from toolkit.translate_tool import translate_tool
from toolkit.dict_api import get_dict_info
from db_repo.db_handle import add2db
import re


def add_dict_info(word):
    add2db('w_dictionary', ('word_eng', 'definition', 'syns', 'antons', 'example'), (get_dict_info(word)))
    time.sleep(5)

def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))

while True:
    try:
        word = input("Enter the word you want to add ")

        if not has_cyrillic(word):
            copied_word_ru, ext_trans = translate_tool(word)[1], translate_tool(word)[2]
            print(f'{word}: ', copied_word_ru, ext_trans)

            while True:
                check = input(f"""Add to the dictionary "{word}"? [y/n] """)
                if check.lower() != 'y' and check.lower() != 'n':
                    print("""please, choose "y" or "n" """)
                    continue
                else:
                    break

            if check.lower() == 'y':
                word = re.sub(r'\s+', ' ', word).strip()

                add2db('w_translated', ('word_eng', 'word_rus', 'word_rus_ext', 'time_added'), (word, copied_word_ru, ext_trans, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                add2db('w_stat', ('word_eng', 'count_learned'), (word, 0))
                
                thread = Thread(target=add_dict_info, args=(word,), daemon=True)
                thread.start()

                print('----------')
                print(f"""-->new word: "{word}" added to dictionary!""")
                print('----------')
            else:
                continue
        else:
            word_en, ext_trans = translate_tool(word, source='ru', target='en')[1], translate_tool(word, source='ru', target='en')[2]

            print(f'{word}: ',word_en, ext_trans)

            while True:
                check = input(f"""Add to the dictionary "{word}"? [д/н] """)
                if check.lower() != 'д' and check.lower() != 'н':
                    print("""please, choose "д" or "н" """)
                    continue
                else:
                    break

            if check.lower() == 'д':
                word = re.sub(r'\s+', ' ', word).strip()
                word_en = re.sub(r'\s+', ' ', word_en).strip()
                add2db('w_translated', ('word_eng','word_rus', 'word_rus_ext', 'time_added'), (word_en, word, ext_trans, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                add2db('w_stat', ('word_eng', 'count_learned'), (word_en, 0))
                
                thread = Thread(target=add_dict_info, args=(word_en,), daemon=True)
                thread.start()

                print('----------')
                print(f"""-->new word: "{word}" added to dictionary!""")
                print('----------')
            else:
                continue
            
    except Exception as e:
        print(e)
        pass
