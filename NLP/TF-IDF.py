
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

from sklearn.feature_extraction.text import TfidfVectorizer


corpus = [
    "Thor eating pizza, Loki is eating pizza, Ironman ate pizza already",
    "Apple is announcing new iphone tomorrow",
    "Tesla is announcing new model-3 tomorrow",
    "Google is announcing new pixel-6 tomorrow",
    "Microsoft is announcing new surface tomorrow",
    "Amazon is announcing new eco-dot tomorrow",
    "I am eating biryani and you are eating grapes"
]


v=TfidfVectorizer()
v.fit(corpus)
transform_output=v.transform(corpus)

print(v.vocabulary_)

i=v.vocabulary_.get('thor')
v.idf_[i]

# Print the idf of each word

all_feature_names=v.get_feature_names_out()

for word in all_feature_names:

    indx=v.vocabulary_.get(word)

    # get the score
    idf_score=v.idf_[indx]

    print(f"{word}: {idf_score}")


# Print the transformed output from tf-idf
print(transform_output.toarray())    



# Custom Use case
# E-commerce data
# 4 labels: Household, Electronics, Clothing & Books
# Task is to create a classification model that can predict a given description of a product and classify them as one of the labels using TfIdf vectorization technique

df=pd.read_csv('Ecommerce_data.csv')
df.head()

df.label.value_counts()

df.shape


df['label_num']=df['label'].map(
    {
        'Household': 0,
        'Electronics': 1,
        'Clothing & Accessories': 2,
        'Books': 3
    }
)

df.head()


# Train Test Split

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(df.Text,df.label_num,test_size=0.2)

len(X_train)
len(X_test)


# Tfidf Vectorizer

tf=TfidfVectorizer()
X_train_tf=tf.fit_transform(X_train)
X_test_tf=tf.transform(X_test)


# Classification Model

clf=DecisionTreeClassifier()
clf.fit(X_train_tf,y_train)

y_pred=clf.predict(X_test_tf)

print(classification_report(y_test,y_pred))


# Testing on a new data

#msg = ["Indira Designer Women's Art Mysore Silk Saree With Blouse Piece (Star-Red) This Saree Is Of Art Mysore Silk & Comes With Blouse Piece."]
msg = ["Satyajit's designer women art saree silk blouse piece, saree with pipili chandua work"]

msg_tf=tf.transform(msg)

clf.predict(msg_tf)
