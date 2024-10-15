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

# 自定义距离函数
def bhattacharyya_distance(x, y):
    # 这里是你的自定义距离计算逻辑
    BC = 0
    for i in range(len(x)):
        BC += math.sqrt(x[i] * y[i])
    
    
    return -math.log(BC, math.e)


df = pd.read_csv("QV_for_draw_guppy.csv")

df_cleaned = df.dropna()

drop_colums = ["Sample", "Config"]

df_final = df_cleaned.drop(columns = drop_colums, axis = 1)

labels = df_final["Label"].values
print(labels)

colors =  ["#43a2ca", "#a6d854", "#a6d854", "#fc8d59", "#fc8d59", "#fc8d59"] * 6 + ["#d53e4f", "#d53e4f", "#d53e4f"] * 6 
colors = colors[1:]

markers = ['^', '^', 'o', '^', 'o', 's'] * 6 + ['^', 'o', 's'] * 6 + ['^', 'o', 's'] * 6 
markers = markers[1:]

X = df_final.drop("Label", axis = 1)
X = X.values

# 计算样本点之间的距离矩阵
distances = pairwise_distances(X, metric = bhattacharyya_distance)

print(distances)

# 使用MDS进行降维
# mds = MDS(n_components = 2, dissimilarity = "precomputed", max_iter = 100, n_init = 2, random_state = 42, eps = 0.0001)
mds = MDS(n_components = 2, dissimilarity = "precomputed")
X_transformed = mds.fit_transform(distances)

plt.figure(figsize=(8, 8))
for i, c in enumerate(colors):
    plt.scatter(X_transformed[i, 0], X_transformed[i, 1], c = colors[i], marker = markers[i], s = 66)
    
    
    
# plt.title('Multidimensional Scaling (MDS) with Bhattacharyya Distance')
plt.xlabel('MDS Dimension 1')
plt.ylabel('MDS Dimension 2')



plt.savefig("MDS_guppy_QV.svg", dpi = 500)
plt.show()

