

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Data={'Year' : [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2020],
      'Exchange Rate' : [65,69,71,64,62,59,72,71,75,78,81]}

print(Data)
type(Data)

df=pd.DataFrame(Data, columns=['Year','Exchange Rate'])
# OR
df=pd.DataFrame(Data)
df
type(df)
df.head()

df.plot(x='Year',y='Exchange Rate',kind='bar')
plt.show()

df.plot(x='Year',y='Exchange Rate',kind='area')
plt.show()

df.plot(x='Year',y='Exchange Rate',kind='line')
plt.show()

df.plot(x='Year',y='Exchange Rate',kind='barh')
plt.show()

df.plot(x='Year',y='Exchange Rate',kind='scatter')
plt.show()
# OR
plt.scatter(df['Year'],df['Exchange Rate'])
plt.show()


x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,86,87,6,76,3,45,67,98,23,45,87,16])
plt.scatter(x,y)
plt.show()

# Plot a pie chart
Data={'Tasks' : [100,500,300]}
df=pd.DataFrame(Data, columns=['Tasks'],index=['Pending','Completed','Ongoing'])
df
df.plot.pie(y='Tasks',figsize=(5,5))
plt.show()


churn_df=pd.read_csv("https://github.com/pik1989/PythonforDS/raw/refs/heads/main/Churn_Modelling.csv")
churn_df.head(5)

# select geography,count(*) from tablename group by geography
churn_df.Geography.value_counts().plot(kind='barh')
churn_df.Geography.value_counts()
churn_df.Geography.value_counts().plot()

churn_df.Exited.value_counts().plot(kind='bar')
churn_df.Exited.value_counts()
churn_df['Exited'].value_counts()/len(churn_df)*100

plt.bar(churn_df['Geography'],churn_df['EstimatedSalary'].mean(),color="cyan",edgecolor="orange")
plt.title('Geography vs Estimated Salary')
plt.show()

plt.bar(churn_df['Geography'],churn_df['EstimatedSalary'].max(), color="cyan",edgecolor="orange")
plt.title('Geography vs Estimated Salary',fontdict={"fontsize":20, "color":"Green"})
plt.show()