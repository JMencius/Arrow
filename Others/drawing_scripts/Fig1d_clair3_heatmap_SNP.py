# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:51:26 2024

@author: Mencius
"""


import seaborn as sns
import matplotlib.pyplot as plt

# 创建数据
clair3_SNP = [[0.832026, 0.898322, 0.892551, 0.998295],
              [0.990883, 0.996941, 0.997966, 0.997527],
              [0.992926, 0.997621, 0.997731, 0.997924],   
              [0.993302, 0.995331, 0.994821, 0.996774]
              ]

row_labels = ["R9G2", "R9G4", "R9G6", "R10D0"]
col_labels = ["R9G2", "R9G4", "R9G6", "R10D0"][::-1]

# 绘制热图
#plt.figure(figsize=(8, 8))
plt.tight_layout()

ax = sns.heatmap(clair3_SNP, cmap = "Blues", vmin = 0.99, vmax = 1,
            annot=True, fmt = ".4f",
            square = True, linewidths=.15, linecolor="black",
            xticklabels = ["R9G2", "R9G4", "R9G6", "R10D0"],
            yticklabels = ["R9G2", "R9G4", "R9G6", "R10D0"])  

# ax.xaxis.tick_top()


plt.rcParams["font.family"] = "Arial" 
colorbar = ax.collections[0].colorbar
# colorbar.set_ticks([0.996, 0.997, 0.998, 0.999])
colorbar.set_label("F1-score")
colorbar.outline.set_visible(True)
colorbar.outline.set_linewidth(0.5) 

plt.title("Clair3 SNP calling", fontsize = 14)


plt.gca().set_xticklabels(row_labels, va = "center")
plt.gca().set_yticklabels(col_labels, va = "center")




# plt.tick_params(axis='x', pad=10)
plt.xlabel("Data", fontsize = 14)
plt.ylabel("Config", fontsize = 14)
# plt.gca().xaxis.set_label_position('top')

ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)




plt.savefig("clair3_SNP.svg", dpi = 600, bbox_inches='tight')

plt.show()
