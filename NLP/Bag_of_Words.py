
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

df=pd.read_csv('spam.csv')
df.head(5)

df.Category.value_counts()
df.Category.value_counts()/len(df)*100

df['Spam']=df['Category'].apply(lambda x: 1 if x=='spam' else 0)
df.head()

new_df=pd.read_csv('spam.csv')
new_df['Category'].replace({'ham': 0, 'spam': 1},inplace=True)
new_df.head()

df.shape


# Train Test Split
X_train,X_test,y_train,y_test=train_test_split(df.Message,df.Spam,test_size=0.2)

X_train.shape
X_test.shape

X_train[:4]
y_train[:4]


# Create bag of words representation using CountVectorizer

v=CountVectorizer()
X_train_cv=v.fit_transform(X_train.values)
X_test_cv=v.transform(X_test)

X_train_cv

X_train_cv.toarray()[:2][0]
X_train_cv.shape

v.get_feature_names_out()[1771]
v.vocabulary_

X_train_np=X_train_cv.toarray()
X_train_np[0]

np.where(X_train_np[0]!=0)


# Naive Bayes Classifier
model=MultinomialNB()
model.fit(X_train_cv,y_train)

y_pred=model.predict(X_test_cv)

print(classification_report(y_test,y_pred))


# Test on a random datapoint

message = {"Upto 20% off on parking, exclusing offer just for you, click on the link below"}

message_cnt=v.transform(message)
model.predict(message_cnt)