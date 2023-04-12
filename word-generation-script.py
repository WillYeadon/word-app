import itertools
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words = set(nltk.corpus.stopwords.words('english'))

words = {}

for combination in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=3):
    word = ''.join(combination)
    
    # Check if the word is a valid English word and not a stop word
    if wordnet.synsets(word) and word not in stop_words:
        sorted_word = ''.join(sorted(word))
        
        if sorted_word in words:
            words[sorted_word].append(word)
        else:
            words[sorted_word] = [word]

for key, value in words.items():
    print(f"'{key}': {value},")
