
import nltk
from nltk.tokenize import word_tokenize
from nltk import ngrams

nltk.download('punkt')

def generate_ngrams(text,n):
    tokens=word_tokenize(text)
    n_grams=list(ngrams(tokens,n))
    return n_grams


# Example text
txt = "N-Grams are a sequence of n items from a given sample of text or speech"

unigrams=generate_ngrams(txt,1)
bigrams=generate_ngrams(txt,2)
trigrams=generate_ngrams(txt,3)

print(unigrams)
print(bigrams)
print(trigrams)


