
# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Reading the data
dataset=pd.read_csv('mall.csv')
dataset.head(5)

X=dataset.iloc[:,[3,4]].values
print(X)


from sklearn.cluster import MeanShift

# fitting the mean shift clustering to the mall dataset
ms=MeanShift(bandwidth=20)

# Adjust the bandwidth parameter to influence the number of clusters
ms.fit(X)
labels=ms.labels_
cluster_centers=ms.cluster_centers_

print(labels) # 0,1,2,3,4,5,6 clusters = 7 clusters

# Visualizing the clusters
n_clusters=len(np.unique(labels))
colors=['red','blue','green','yellow','cyan','purple','pink']

for i in range(n_clusters):
   cluster=X[labels == i]
   plt.scatter(cluster[:,0],cluster[:,1],s=100,c=colors[i],label=f'Cluster {i+1}')

plt.title('Cluster of Clients')
plt.xlabel('Annual Income')
plt.ylabel('Spending Score (0-100)')
plt.legend()
plt.show()   
