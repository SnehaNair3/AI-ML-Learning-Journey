
import pandas as pd
from sklearn.linear_model import LogisticRegression


data= {
    'Age' : [22, 25, 18, 45, 12, 43, 23, 33],
    'Gender' : ['F','F','M','M','F','M','M','M'],
    'Smoker' : ['N','S','S','N','S','S','S','S'],
    'Disease' : [1,1,0,0,0,1,0,1]
}


df=pd.DataFrame(data)
print(data)

# Convert categorical data to dummy variables
df=pd.get_dummies(df,columns=['Gender','Smoker'])
df.head()


# Seperate the features (X) and target (y) variable
X=df.drop('Disease',axis=1)
y=df['Disease']

#Fit the logistic regression model
model=LogisticRegression()

model.fit(X,y)


# Get the regression coefficients and the intercept
coef=model.coef_[0]
intercept=model.intercept_[0]

# Print the coefficients and the intercept
print('Regression coefficients (m1,m2,m3,m4,m5) : ',coef)
print('Intercept is : ',intercept)


