# Import the required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
# %matplotlib inline is for Jupyter notebooks and should be omitted in a standard Python script


telco_base_data=pd.read_csv('Churn_Modelling.csv')

telco_base_data.head(5)

telco_new = telco_base_data[['Geography','Gender','Exited']]
telco_new.head(5)

telco_new.Exited.value_counts()
telco_new.Exited.value_counts()/len(telco_new)*100


# Univariate Analysis

for i, predictor in enumerate(telco_new.drop(columns=['Exited'])):
    plt.figure()
    sns.countplot(data=telco_new, x=predictor,hue='Exited')


# Bivariate Analysis
sns.histplot(x='Gender',hue='Geography',data=telco_new,stat="count",multiple="dodge")

telco_new_target1=telco_new.loc[telco_new["Exited"]==1]

sns.histplot(x='Gender',hue='Geography',data=telco_new_target1,stat="count",multiple="dodge")



# numerical Analysis
# Correlation : It ranges from -1 to +1.
# +1 -> Positive correlation
# -1 -> Negative correlation
# 0  -> No correlation


telco_base_data.dtypes

telco_base_data.corr()

