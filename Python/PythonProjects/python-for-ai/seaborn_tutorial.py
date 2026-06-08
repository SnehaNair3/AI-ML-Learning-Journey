import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib

print("NumPy:", np.__version__)
print("Pandas:", pd.__version__)
print("Seaborn:", sns.__version__)
print("Matplotlib:", matplotlib.__version__)




import seaborn as sns

# Seaborn for plotting and styling
import seaborn as sns
df=sns.load_dataset('iris')
print(df.head())

len(df)

df.species.value_counts()
df.species.value_counts().plot(kind='barh')

print(df['sepal_length'].dtype)

sns.kdeplot(df['sepal_length'])
sns.kdeplot(df['sepal_length'], fill=True)

# KDE - Kernel Density Estimation
for col in ['sepal_length','sepal_width','petal_length','petal_width']:
    sns.kdeplot(df[col],shade=True)

# Histograms + KDE = Distplot
sns.distplot(df['sepal_length'])

sns.pairplot(df,hue='species',height=2.5)
sns.pairplot(df, hue='species', height=2.5, diag_kind='hist')


Data={'Year' : [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2020],
      'Exchange Rate' : [65,69,71,64,62,59,72,71,75,78,81]}

Data
type(Data)

import pandas as pd
df=pd.DataFrame(Data)
df.head(5)

sns.lineplot(x=df['Year'],y=df['Exchange Rate'])

# Heatmap
import matplotlib.pyplot as plt
import seaborn as sns
# Load the example flights dataset and convert to long-form
flights_long = sns.load_dataset("flights")
flights = (
    flights_long
    .pivot(index="month", columns="year", values="passengers")
)

flights

# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(flights, annot=True, fmt="d", linewidths=.5, ax=ax)
plt.show()

# Plotly























# VERSION FIX
import sys
import numpy as np

print(sys.executable)
print(np.__version__)

import seaborn as sns
import numpy as np
import matplotlib

print(np.__version__)
print(sns.__version__)
print(matplotlib.__version__)

import sys
print(sys.executable)

!{sys.executable} -m pip show numpy

import sys
!{sys.executable} -m pip install --upgrade numpy

import numpy as np
print(np.__version__)