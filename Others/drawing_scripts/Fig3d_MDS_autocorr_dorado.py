# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:23:12 2024

@author: Mencius
"""

import pandas as pd
import math
import numpy as np
from sklearn.manifold import MDS
from sklearn.metrics import pairwise_distances
from matplotlib.patches import Ellipse
import matplotlib.pyplot as plt




def euclidean_distance(autocorr1 : list, autocorr2 : list) -> float:
    # print(len(autocorr1), len(autocorr2))
    assert len(autocorr1) == len(autocorr2)
    # print(autocorr1)
    # print(autocorr2)
    return math.sqrt(sum([(autocorr1[i] - autocorr2[i]) ** 2 for i in range(len(autocorr1))]))


df = pd.read_csv("autocorr_for_draw_dorado.csv")

df_cleaned = df.dropna()

drop_colums = ["Sample", "Config"] + ['A' + str(i) for i in range(21, 101)]

df_final = df_cleaned.drop(columns = drop_colums, axis = 1)

labels = df_final["Label"].values

X = df_final.drop("Label", axis = 1)
X = X.values

print(labels)


colors = ["#a02b93"]*12 + ["#002060"] * 12


markers = ['o', 's'] * 12



# 计算样本点之间的距离矩阵
distances = pairwise_distances(X, metric = euclidean_distance)

# 使用MDS进行降维
#mds = MDS(n_components = 2, dissimilarity = "precomputed")
mds = MDS(n_components = 2, dissimilarity = "precomputed", max_iter = 1000, n_init = 2, eps = 0.0001)
X_transformed = mds.fit_transform(distances)

plt.figure(figsize=(8, 8))

for i, c in enumerate(colors):
    plt.scatter(X_transformed[i, 0], X_transformed[i, 1], c = colors[i], marker = markers[i], s = 90)

    
    
    
plt.title('Multidimensional Scaling (MDS) with Euclidean Distance')
plt.xlabel('MDS Dimension 1')
plt.ylabel('MDS Dimension 2')



plt.savefig("MDS_dorado_autocorr.svg", dpi = 600)
plt.show()


