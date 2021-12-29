#https://sentence.yourdictionary.com/

import requests
import re

def get_sents(word):
    sents = requests.get(f'https://sentence.yourdictionary.com/{word}').text
    sents = re.findall(r'sentence:"(\D*)",upvotes', sents)

    return sents
