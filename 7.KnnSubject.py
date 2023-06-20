from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('data 1.csv')
x1 = np.array(dataset['A'])
x2 = np.array(dataset['B'])
x3 = np.array(dataset['Subject'])

X = np.array(list(zip(x1, x2)))
colors = ['b', 'g', 'r']
markers = ['o', 'v', 's']
plt.ylabel('Variable B')


kmeans = KMeans(n_clusters=2).fit(X)
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1], 
            s = 200, c = 'red', label = 'Centroids')
for i, l in enumerate(kmeans.labels_):
    plt.plot(x1[i], x2[i], color=colors[l], marker=markers[l])
    plt.text(x1[i]+0.1, x2[i]+0.1, f'{x3[i]}')
plt.xlabel('Variable A')
plt.legend()
plt.show()