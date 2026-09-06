
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Sample sentence
sentence = "This is a sample sentence, showing off the stop words filtration"

# Tokenize the Sentence
nltk.download('punkt')
nltk.download('stopwords')
words=word_tokenize(sentence)

# Filter out stopwords
new_sentence=[word for word in words if word.lower() not in stopwords.words('english')]


# Print the final sentence
print(sentence)
print(new_sentence)