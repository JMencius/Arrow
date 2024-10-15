# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:52:10 2024

@author: Mencius
"""


import seaborn as sns
import matplotlib.pyplot as plt

# 创建数据
clair3_SNP = [[2.137, 4.431, 3.196, 5.235, 5.292, 2.576, 1.244],
              [1.072, 3.172, 1.904, 4.336, 4.656, 2.499, 1.204],
              [5.478, 7.719, 7.308, 6.55, 6.152, 1.575, 0.065],
              [5.443, 7.18, 7.002, 6.533, 6.122, 1.792, 0.439],
              [6.488, 6.981, 7.875, 4.344, 3.661, -4.011, -5.527],
              [6.192, 7.803, 7.8, 5.583, 5.142, -0.088, -1.33],
              [7.567, 2.532, 6.303, -1.021, -2.126, -8.34, -9.337] 
              ]
              

row_labels = ["R9G4FAST", "R9G4HAC", "R9G6FAST", "R9G6HAC", "R9G6SUP", "R10D0HAC", "R10D0SUP"]
col_labels = ["R9G4FAST", "R9G4HAC", "R9G6FAST", "R9G6HAC", "R9G6SUP", "R10D0HAC", "R10D0SUP"][::-1]

# 绘制热图
plt.figure(figsize=(10, 10))
ax = sns.heatmap(clair3_SNP, cmap = "RdBu", vmin = -10, vmax = 10,
            annot=True, fmt = ".3f",
            square = True, linewidths=.1, linecolor="black",
            cbar_kws={"shrink": 0.83},
            xticklabels = row_labels,
            yticklabels = col_labels)  

# ax.xaxis.tick_top()


plt.rcParams["font.family"] = "Arial" 
colorbar = ax.collections[0].colorbar
colorbar.set_ticks([-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
colorbar.set_label("Yak QV score shift")
colorbar.outline.set_visible(True)
colorbar.outline.set_linewidth(0.5) 

plt.title("Medaka polishing", fontsize = 14)


plt.gca().set_xticklabels(row_labels, va = "center")
plt.gca().set_yticklabels(col_labels, va = "center")

plt.tick_params(axis='x', pad=10)
plt.xlabel("Data", fontsize = 14)
plt.ylabel("Config", fontsize = 14)
# plt.gca().xaxis.set_label_position('top')



ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)

plt.savefig("Medaka_deltaQV.svg", dpi = 600, bbox_inches='tight')

plt.show()

