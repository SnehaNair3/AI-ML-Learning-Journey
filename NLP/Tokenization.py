
import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
nltk.download('punkt')
# Sample text for tokenization
txt = "NLTK provides powerful tools for tokenization. It includes word tokenization and sentence tokenization"

# Word Tokenization
words=word_tokenize(txt)
print(words)

# Sentence Tokenization
sent=sent_tokenize(txt)
print(sent)
