# Special Character Removal

import re

# Input string
input_str="hello how are$ you!!"

# Using regular expressions to remove special characters
clean_str=re.sub(r"[^a-zA-Z0-9\s]","",input_str)

print(clean_str)

# re.sub(pattern,replacement,string) searches for a pattern in the given string and replaces it with a specified replacement string.


# Libaraies in the field of NLP

# Spacy - Natural language processing library in Python that can be used to tokenize and process textual data.
# nltk

import spacy

# Load the spacy model
nlp=spacy.load("en_core_web_sm")

# Input string
input_str="hello how are$ you!!"

# Function to clean the string
def clean_text(text):
    cleaned_text=''.join(char for char in text if char.isalpha() or char.isspace())
    doc=nlp(cleaned_text)
    return ' '.join(token.text for token in doc)


# Get the final output
clean_str=clean_text(input_str)
print(clean_str)



import nltk

nltk.download('punkt')

input_str = "hello how are$ you!!"

# Tokenize
tokens=nltk.word_tokenize(input_str)

# Remove the special characters
clean_tokens=[token for token in tokens if token.isalnum()]

clean_str=' '.join(clean_tokens)

print(clean_str)