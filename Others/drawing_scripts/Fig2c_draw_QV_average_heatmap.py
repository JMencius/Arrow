# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:59:49 2024

@author: Mencius
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np



# read csv file
df = pd.read_csv("draw_QV_average.csv")
df_cleaned = df.dropna()
drop_colums = ["Sample", "Config"] 
df_final = df_cleaned.drop(columns = drop_colums, axis = 1)
labels = df_final["Label"].values

X = df_final.drop("Label", axis = 1)
X = X.values


qv_sum = {i : [0 for i in range(90)] for i in set(labels)}
count = {i : 0 for i in set(labels)}



for i in range(len(labels)):
    label = labels[i]
    count[label] += 1
    
    qv = X[i]
    for j in range(90):
        qv_sum[label][j] += qv[j]


qv_average = dict()
for i in qv_sum.keys():
    qv_average[i] = [t / count[i] * 100 for t in qv_sum[i]]

    
# print(qv_average.keys())

input_matrix = [qv_average['R9_G2_NONE'],
              qv_average['R9_G4_FAST'],
              qv_average['R9_G4_HAC'],
              qv_average['R9_G6_FAST'],
              qv_average['R9_G6_HAC'],
              qv_average['R9_G6_SUP'],
              qv_average['R10_G6_FAST'],
              qv_average['R10_G6_HAC'],
              qv_average['R10_G6_SUP'],
              qv_average['R9_D0_FAST'],
              qv_average['R9_D0_HAC'],
              qv_average['R9_D0_SUP'],
              qv_average['R10_D0_FAST'],
              qv_average['R10_D0_HAC'],
              qv_average['R10_D0_SUP']]

ytick_labels = ['R9_G2_NONE',
                'R9_G4_FAST',
                'R9_G4_HAC',
                'R9_G6_FAST',
                'R9_G6_HAC',
                'R9_G6_SUP',
                'R10_G6_FAST',
                'R10_G6_HAC',
                'R10_G6_SUP',
                'R9_D0_FAST',
                'R9_D0_HAC',
                'R9_D0_SUP',
                'R10_D0_FAST',
                'R10_D0_HAC',
                'R10_D0_SUP']

data = np.array(input_matrix)

plt.figure(figsize=(14, 8))

data[data < 0] = 0  # 将所有小于0的值设为0，模拟非0的数据

# 创建掩码，将值为0的单元格设为True
mask = np.ma.masked_where(data == 0, data)

# 绘制热图，并指定mask对应的颜色为蓝色
ax = sns.heatmap(data, mask=mask.mask, cmap="Blues", cbar=True, cbar_kws={'label': 'Value'}, vmin = -1, vmax = 8)

colorbar = ax.collections[0].colorbar
colorbar.set_ticks([0, 1,2,3,4,5,6,7,8])
# ax = sns.heatmap(input_matrix, cmap='Blues', cbar=True, vmin = 0, vmax = 6)

ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)


# 指定要显示的 x 轴刻度值
xtick_indices = [0, 9, 19, 29, 39, 49, 59, 69, 79, 89]
xtick_labels = [1, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# 调整 x 轴刻度位置的偏移量，使标签居中对齐在格子的正中间
ax.set_xticks(np.array(xtick_indices) + 0.5)
ax.set_xticklabels(xtick_labels)
ax.set_yticklabels(ytick_labels, rotation=0)


plt.savefig("fig2C_heatmap.svg", dpi = 500)
plt.show()













