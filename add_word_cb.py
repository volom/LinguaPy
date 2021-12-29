#https://deep-translator.readthedocs.io/en/latest/usage.html

"""
Script for adding English word to the dictionary 
by copping value to clipboard
"""


from threading import Thread
import time
import pyperclip
from datetime import datetime
from toolkit.translate_tool import translate_tool
from toolkit.dict_api import get_dict_info
from db_repo.db_handle import add2db
import pyttsx3
import re
import os

words_list = []

try:
    words_list.append(pyperclip.paste())
except:
    words_list.append(1)
    
flag1 = True
flag2 = True

def add_dict_info(word):
    add2db('w_dictionary', ('word_eng', 'definition', 'syns', 'antons', 'example'), (get_dict_info(word)))
    time.sleep(5)

print("Go ahead! Improve your English!")
while True:
    try:
        if flag1:
            pyperclip.copy('None')
            pyperclip.waitForNewPaste()
        else:
            flag1 = True
        cb_value = pyperclip.paste()

        if cb_value != words_list[-1] and cb_value != 'None' and flag2:
            copied_word_en = cb_value
            copied_word_ru, ext_trans = translate_tool(copied_word_en)[1], translate_tool(copied_word_en)[2]

            print(f'{copied_word_en}: ',copied_word_ru, ext_trans)

            pyttsx3.speak(copied_word_ru)
            words_list.append(cb_value)
            words_list = [words_list[-1]]
        elif cb_value == words_list[-1] and cb_value != 'None' and not flag2:
            copied_word_en = cb_value
            copied_word_ru, ext_trans = translate_tool(copied_word_en)[1], translate_tool(copied_word_en)[2]

            print(f'{copied_word_en}: ',copied_word_ru, ext_trans)

            pyttsx3.speak(copied_word_ru)
            words_list.append(cb_value)
            words_list = [words_list[-1]]
            flag2 = True
        pyperclip.copy('None')
        pyperclip.waitForNewPaste()
        cb_value = pyperclip.paste()
        words_list.append(cb_value)
        if all([cb_value == words_list[-1], cb_value != 'None', cb_value == words_list[-2]]):
            words_list = [words_list[-1]]
            # database, your english words list (.txt file with ";" delimiter)
            copied_word_en = words_list[-1]
            copied_word_en = re.sub(r'\s+', ' ', copied_word_en).strip()
            copied_word_ru, ext_trans = translate_tool(copied_word_en)[1], translate_tool(copied_word_en)[2]

            add2db('w_translated', ('word_eng','word_rus', 'word_rus_ext', 'time_added'), (copied_word_en, copied_word_ru, ext_trans, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            add2db('w_stat', ('word_eng', 'count_learned'), (copied_word_en, 0))
            
            thread = Thread(target=add_dict_info, args=(copied_word_en,), daemon=True)
            thread.start()
    
            print('----------')
            print(f"""-->new word: "{copied_word_en}" added to dictionary!""")
            print('----------')
            continue
        else:
            flag1 = False
            flag2 = False
        
        words_list = [words_list[-1]]
    except Exception as e:
        print(e)
        continue
