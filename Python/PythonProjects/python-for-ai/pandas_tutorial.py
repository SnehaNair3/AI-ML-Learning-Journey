import pandas as pd
import numpy as np

df=pd.read_csv("https://github.com/pik1989/PythonforDS/raw/refs/heads/main/Churn_Modelling.csv")
print(df)
# Top 5  records default
df.head()
# Top 10 records
df.head(10)
# Last records 5 -default
df.tail()
# Last 10 records
df.tail(10)

# Shows info about the dataframe
df.info()

# Describe the statistical information of the numerical columns
df.describe()

# Print all the columns of the dataframe
df.columns

# Transpose
df.T

# Sort values based on age
df.sort_values('Age')
# OR
new_df=df.sort_values('Age')
new_df.head()

# Print a specific column
df['Gender']
df.Balance
df['Surname']
df.Surname

# Create a new column
df['New Balance']=df['Balance']+1000
df.head(5)
df['Random Column']='Good Day'
df.head(5)

# How to access rows?
# access 10,11 and 12th rows
df[10:13]
# access 20 to 25 rows
df[20:26]

# Filter only age greater than 50
df[df.Age > 50]

ages=df[df.Age > 50]
len(ages)

# Filling null values
df['Age'].fillna(10)

# Remove columns
df.pop('Random Column')
df

df.drop('New Balance',axis=1)

df['Balance']
df['Balance'].apply(np.sqrt)

num=83807
np.sqrt(num)

df['SquareRoot_Balance']=df['Balance'].apply(np.sqrt)
df.head()

# Drop all the null values in Age column
df['Age'].dropna()

# Concat and Merging
df1=pd.DataFrame({'A':['A0','A1','A2','A3'],
                  'B':['B0','B1','B2','B3'],
                  'C':['C0','C1','C2','C3'],
                  'D':['D0','D1','D2','D3']     
                })

print(df1)

df2=pd.DataFrame({'E':['A4','A5','A6','A7'],
                  'F':['B4','B5','B6','B7'],
                  'C':['C0','C3','C6','C7'],
                  'G':['D4','D5','D6','D7']     
                })

print(df2)

merge_df1=pd.merge(df1,df2,on='C',how='outer')
print(merge_df1)

merge_df2=pd.merge(df1,df2,on='C',how='inner')
print(merge_df2)

# loc and iloc
s=pd.Series(list("abcdef"),index=[49,48,47,0,1,2])
s
s.loc[0] # value at index label 0

s.iloc[0] # value at index location 0

# s.loc[3] # error - no index label 3
s.iloc[3]

s.loc[0:1] # rows at index labels between 0 and 1 (inclusive)
s.iloc[0:1] # rows at index location between 0 and 1 (exclusive)

# What if you sort the series
s=s.sort_index()
s
s.iloc[0] # value at index location 0
s.loc[0] # value at index label 0

s.loc[0:1] # rows at index labels between 0 and 1 (inclusive)
s.iloc[0:1] # rows at index locaion between 0 and 1 (exclusive)