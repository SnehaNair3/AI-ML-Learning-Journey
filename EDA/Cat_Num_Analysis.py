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


# telco_base_data.dtypes
# telco_base_data.corr()

telco_base_data.select_dtypes(include='number').corr()

plt.figure(figsize=(20,8))
telco_base_data.select_dtypes(include='number').corr()['Exited'].sort_values(ascending=False).plot(kind='bar')


plt.figure(figsize=(6,6))
sns.heatmap(telco_base_data.select_dtypes(include='number').corr(),cmap='Paired')
telco_base_data.head(5)

telco_base_data['Age'].value_counts().sort_index(ascending=True).plot()

telco_base_data1=telco_base_data.loc[telco_base_data['Exited']==1]
telco_base_data1['Age'].value_counts().sort_index(ascending=True).plot()

# Age by Churn
Tot=sns.kdeplot(telco_base_data.Age[(telco_base_data['Exited']==0)],color="Red",shade=True)
Tot=sns.kdeplot(telco_base_data.Age[telco_base_data['Exited']==1], color="Blue", shade=True)
Tot.legend(["No Churn","Churn"], loc='upper right')
Tot.set_ylabel('Density')
Tot.set_xlabel('Age')
Tot.set_title('Age by Churn')


# Tenure by Churn
Tot=sns.kdeplot(telco_base_data.Tenure[(telco_base_data['Exited']==0)],color="Red",shade=True)
Tot=sns.kdeplot(telco_base_data.Tenure[(telco_base_data['Exited']==1)],color="Blue",shade=True)
Tot.legend(["No Churn","Churn"],loc='upper right')
Tot.set_ylabel('Density')
Tot.set_xlabel('Tenure')
Tot.set_title('Tenure by Churn')


# Balance by Churn
Tot=sns.kdeplot(telco_base_data.Balance[(telco_base_data['Exited']==0)],color="Red",shade=True)
Tot=sns.kdeplot(telco_base_data.Balance[(telco_base_data['Exited']==1)],color="Blue",shade=True)
Tot.legend(["No Churn","Churn"],loc='upper right')
Tot.set_ylabel('Density')
Tot.set_xlabel('Tenure')
Tot.set_title('Balance by Churn')


