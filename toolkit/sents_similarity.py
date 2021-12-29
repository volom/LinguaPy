"""
The script consists algorithm for calculating sentences similarity
"""

import nltk
import re

# synonyms library
try:
    from nltk.corpus import wordnet
    syns = wordnet.synsets("simple")
except:
    try:
        syns = wordnet.synsets("simple")
    except:
        nltk.download('wordnet')
        syns = wordnet.synsets("simple")

# word tokenize library
try:
    from nltk.tokenize import word_tokenize
except:
    try:
        from nltk import word_tokenize
    except:
        nltk.download('punkt')
        from nltk import word_tokenize

# stopwords library
try:
    from nltk.corpus import stopwords
    stopwords.words('english')
except:
    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.words('english')

# function
def sents_similarity(sent1, sent2):    
    # tokenization
    sent1_list = word_tokenize(sent1) 
    sent2_list = word_tokenize(sent2)
    
    # sw contains the list of stopwords
    sw = stopwords.words('english') 

    vect1 = []
    vect2 = []
    
    # remove stop words from the string
    sent1_set = {w for w in sent1_list if not w in sw} 
    sent2_set = {w for w in sent2_list if not w in sw}
    
    # form a set containing keywords of both strings 
    united_set = sent1_set.union(sent2_set) 

    # extend united_set with synonyms
    a = set()
    for i in united_set:
        syns = wordnet.synsets(i)
        for j in syns:
            try:
                a.add(re.match(r"Synset\('(.*)\.\D", str(j)).group(1).replace('_', ' '))
            except:
                pass
    united_set = united_set.union(a)
    for w in united_set:
        if w in sent1_set: 
            vect1.append(1) # create a vector
        else: 
            vect1.append(0)
        if w in sent2_set: 
            vect2.append(1)
        else: 
            vect2.append(0)

    c = 0
    
    # cosine formula 
    for i in range(len(united_set)):
            c+= vect1[i]*vect2[i]
            
    cosine = c / float((sum(vect1)*sum(vect2))**0.5)
    return cosine
