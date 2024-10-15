# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:51:26 2024

@author: Mencius
"""


import seaborn as sns
import matplotlib.pyplot as plt

# 创建数据
clair3_SNP = [[0.067985, 0.231753, 0.387316, 0.88193],
              [0.199536, 0.635044, 0.799815, 0.796299],  
              [0.352299, 0.723378, 0.76281, 0.800324],
              [0.392592, 0.401098, 0.269323, 0.46136]
              ]
              

row_labels = ["R9G2", "R9G4", "R9G6", "R10D0"]
col_labels = ["R9G2", "R9G4", "R9G6", "R10D0"][::-1]

# 绘制热图
#plt.figure(figsize=(8, 8))
ax = sns.heatmap(clair3_SNP, cmap = "Blues", vmin = 0.2, vmax = 1,
            annot=True, fmt = ".4f",
            square = True, linewidths=.15, linecolor="black",
            xticklabels = ["R9G2", "R9G4", "R9G6", "R10D0"],
            yticklabels = ["R9G2", "R9G4", "R9G6", "R10D0"])  

# ax.xaxis.tick_top()


plt.rcParams["font.family"] = "Arial" 
colorbar = ax.collections[0].colorbar
colorbar.set_ticks([0.2, 0.4, 0.6, 0.8, 1.0])
colorbar.set_label("F1-score")
colorbar.outline.set_visible(True)
colorbar.outline.set_linewidth(0.5) 

plt.title("Clair3 INDEL calling", fontsize = 14)


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

plt.savefig("clair3_INDEL.svg", dpi = 600, bbox_inches='tight')

plt.show()
