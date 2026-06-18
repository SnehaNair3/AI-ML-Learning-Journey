# OUTLIERS

# 3- Sigma Technique (Standard Deviation)

import numpy as np
import matplotlib.pyplot as plt
import statistics
import pandas as pd

data=pd.read_csv('raw_sales2.csv')

data.head(5)
type(data)

# Function to detect outlier in one-dimensional datasets.
def find_anomalies(data):
    # define a list to accumulate anomalies
    anomalies=[]

    # Set upper and lower limit to 3 standard deviation
    random_data_std=statistics.stdev(data)
    random_data_mean=statistics.mean(data)

    # 3-standard deviation
    anomaly_cut_off=random_data_std*3

    lower_limit=random_data_mean-anomaly_cut_off
    upper_limit=random_data_mean+anomaly_cut_off

    # Generate outliers
    for outlier in data:
        if outlier > upper_limit or outlier < lower_limit:
            anomalies.append(outlier)
    return anomalies    

data.price

list_1=find_anomalies(data['price'])
len(list_1) # 461
len(data)   # 29580
# (461/29580)*100=1.55
# 1.55 % of data is outlier 
# Its not a normally distributed data
# If the data was normally ditributed, then the outlier would have been 0.3%.


# check whether the data is skewed or not
data.price.skew()
# 4.31 which means that the data is rigth-skewed (positive skewness)

# Plotting
import seaborn as sns

sns.kdeplot(data.price)

# Transformation
data['price_transformed']=np.log(data.price)
data.price_transformed.skew()

list_2=find_anomalies(data.price_transformed)
len(list_2)  # 266
len(data)    # 29580
# (266)/29580)*100=0.9% - less outlier - better

sns.kdeplot(data.price_transformed)

# Double logarithmic tranformation
data['price_transformed_double']=np.log(data.price_transformed)
data['price_transformed_double'].skew()
list_3=find_anomalies(data.price_transformed_double)
len(list_3)  # 251
len(data)    # 29580
# (251/29580)*100=0.8 % - better

# Anything below 40 or above 80 are considered outliers.




# Boxplots
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(data=data)
# It considers everything above 75 or below ~35 to be an outlier.


import pandas as pd
df=pd.DataFrame(data)
len(df)
df
df.describe()



# Inter Quartile Range
# IQR = Q3 - Q1
list1=[43,54,56,61,62,66,68,69,69,70,71,72,77,78,79,85,87,88,89,93,95,96,98,99,99]
len(list1)
max(list1)
min(list1)

import  statistics
statistics.mean(list1)
sorted(list1)

# To find the 90th percentile for these ordered scores, start by multiplying 90 percent times the total no of scores , which gives 90%*25=22.5(the index) .
# Rounding up to the nearest whole number , you get 23.
list2=sorted(list1)
list2
# 23rd element = 98.
# Hence , 98 is the 90th percentile for this dataset.


# If we wanna find the 20th percentile, start by  taking 0.20 *25=5(the index), this is a whole no, which tell you the 20th percentile is the average of the 5ht and 6th values in the ordered dataset (62 and 66).
# So 20th percentile= (62+66)/2 = 64

# The median (the 50th percentile) for the test score is the 13th score : 77.
