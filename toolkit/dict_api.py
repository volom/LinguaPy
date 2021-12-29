#https://dictionaryapi.dev/
"""
The script helps you to extract data from an online dictionary 
(https://dictionaryapi.dev/) with API
"""

import requests
import re

def get_dict_info(word):
    word_dict = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").json()  
    
    try:
        definition = word_dict[0]['meanings'][0]['definitions'][0]['definition']
        definition = re.sub(r"\[|\]|'", '', str(definition))
    except:
        definition = ''

    try:
        example = word_dict[0]['meanings'][0]['definitions'][0]['example']
        example = re.sub(r"\[|\]|'", '', str(example))
    except:
        example = ''
    try:
        syns = word_dict[0]['meanings'][0]['definitions'][0]['synonyms']
        syns = re.sub(r"\[|\]|'", '', str(syns))
    except:
        syns = ''
    try:
        antons = word_dict[0]['meanings'][0]['definitions'][0]['antonyms']
        antons = re.sub(r"\[|\]|'", '', str(antons))
    except:
        antons = ''
    return word, definition, syns, antons, example
