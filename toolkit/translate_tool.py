"""
Script contains tools for translation tools
"""

from deep_translator import GoogleTranslator
from deep_translator import LingueeTranslator
from deep_translator import PonsTranslator


def translate_tool(word, source='en', target='ru'):
    word_ru = GoogleTranslator(source=source, target=target).translate(word)

    try:
        word_ru_LT = LingueeTranslator(source=source, target=target).translate(word, return_all=True)
    except:
        word_ru_LT = ''

    try:
        word_ru_pons = PonsTranslator(source=source, target=target).translate(word, return_all=True)
    except:
        word_ru_pons = ''
    
    ext_res = ', '.join(word_ru_LT)+', '.join(word_ru_pons)

    return word, word_ru, ext_res

#print(f'{word}: ',word_ru,', ',', '.join(word_ru_LT),', '.join(word_ru_pons))
