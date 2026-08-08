
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures,StandardScaler
from sklearn.metrics import r2_score
from sklearn.pipeline import Pipeline


# Creating data
X=6*np.random.rand(200,1)-3
y=0.8*X**2+0.9*X+2+np.random.randn(200,1)
# y=2 + 0.9X + 0.8X^2 + random noise

plt.plot(X,y,'b.')
plt.xlabel("X")
plt.ylabel("y")
plt.show()


# Train test split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=3)


# Applying the linear regression model
lr=LinearRegression()
lr.fit(X_train,y_train)


y_pred=lr.predict(X_test)
r2_score_lr=r2_score(y_test,y_pred)
print(y_pred)
print('r2 score: ',r2_score_lr)
# r2 score is very low here
# since this data is a polynomial data, its not fit for linear regression model.


plt.plot(X_train,lr.predict(X_train),color='r')
plt.plot(X,y,'b.')
plt.xlabel("X")
plt.ylabel("y")
plt.show()



# Applying Polynomial Regression
poly=PolynomialFeatures(degree=2,include_bias=True)

X_train_trans=poly.fit_transform(X_train)
X_test_trans=poly.transform(X_test)


print(X_train[0]) # only 1 value
print(X_train_trans[0]) # 3 values X0,X1,X2

lr2=LinearRegression()
lr2.fit(X_train_trans,y_train)

y_pred2=lr2.predict(X_test_trans)

print('r2_score : ', r2_score(y_test,y_pred2))

# Coefficients
print(lr2.coef_) 

# Intercept B0
print(lr2.intercept_)

# New data points
X_new=np.linspace(-3,3,200).reshape(200,1)

X_new_poly=poly.transform(X_new)
y_new=lr.predict(X_new_poly)

plt.plot(X_new,y_new,"r-",linewidth=2,label='Predictions')
plt.plot(X_train,y_train,"b.",label="Training")
plt.plot(X_test,y_test,"g.",label="Test")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()


def polynomial_regression(degree):
    X_new=np.linspace(-3, 3, 100).reshape(100, 1)
    X_new_poly = poly.transform(X_new)

    polybig_features = PolynomialFeatures(degree=degree, include_bias=False)
    std_scaler = StandardScaler()
    lin_reg = LinearRegression()
    polynomial_regression = Pipeline([
            ("poly_features", polybig_features),
            ("std_scaler", std_scaler),
            ("lin_reg", lin_reg),
        ])
    polynomial_regression.fit(X, y)
    y_newbig = polynomial_regression.predict(X_new)
    plt.plot(X_new, y_newbig,'r', label="Degree " + str(degree), linewidth=2)

    plt.plot(X_train, y_train, "b.", linewidth=3)
    plt.plot(X_test, y_test, "g.", linewidth=3)
    plt.legend(loc="upper left")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.axis([-3, 3, 0, 10])
    plt.show()


polynomial_regression(2)
polynomial_regression(50)
polynomial_regression(100)

poly.powers_


# Visualize the data using a 3-d plot
# 3-D polynomial regression

X=7*np.random.rand(100,1)-2.8
y=7*np.random.rand(100,1)-2.8

z=X**2+y**2+0.2*X+0.2*y+0.1*X*y+2+np.random.rand(100,1)
# z=x^2+y^2+0.2x+0.2y+0.1xy+2


import plotly.express as px
df=px.data.iris()
fig=px.scatter_3d(df,x=X.ravel(),y=y.ravel(),z=z.ravel())
fig.show()