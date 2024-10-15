# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:51:26 2024

@author: Mencius
"""


import seaborn as sns
import matplotlib.pyplot as plt

# 创建数据
clair3_SNP = [[0.628116, 0.585492, 0.771143, 0.680721, 0.7756, 0.76456, 0.975285, 0.996817, 0.996835],
              [0.832026, 0.792765, 0.898322, 0.858473, 0.892551, 0.863281, 0.990362, 0.998295, 0.998052],
              [0.990883, 0.822574, 0.996941, 0.994377, 0.997966, 0.998168, 0.989705, 0.997527, 0.997951],
              [0.992926, 0.992043, 0.997621, 0.995912, 0.997731, 0.997749, 0.988499, 0.997924, 0.997942],
              [0.993302, 0.991983, 0.995331, 0.994259, 0.994821, 0.994963, 0.975409, 0.996774, 0.997074]
              ]

row_labels = ["R9G2", "R9G4FAST", "R9G4HAC", "R9G6FAST", "R9G6HAC", "R9G6SUP", "R10D0FAST", "R10D0HAC", "R10D0SUP"]
col_labels = ["R9G2", "R9G4HAC", "R9G5SUP", "R10D0HAC", "R10D0SUP"][::-1]


# 绘制热图
plt.figure(figsize=(12, 8))
plt.tight_layout()

ax = sns.heatmap(clair3_SNP, cmap = "Blues", vmin = 0.99, vmax = 1,
            annot=True, fmt = ".4f",
            square = True, linewidths=.15, linecolor="black",
            xticklabels = row_labels,
            yticklabels = col_labels)  

# ax.xaxis.tick_top()


plt.rcParams["font.family"] = "Arial" 
colorbar = ax.collections[0].colorbar
# colorbar.set_ticks([0.996, 0.997, 0.998, 0.999])
colorbar.set_label("F1-score")
colorbar.outline.set_visible(True)
colorbar.outline.set_linewidth(0.5) 

colorbar.ax.set_position([0.77, 0.24, 0.05, 0.52])

plt.title("Clair3 SNP calling", fontsize = 14)


plt.gca().set_xticklabels(row_labels, va = "center")
plt.gca().set_yticklabels(col_labels, va = "center")




# plt.tick_params(axis='x', pad=10)
plt.xlabel("Data", fontsize = 14)
plt.ylabel("Config", fontsize = 14)

# plt.gca().xaxis.set_label_position("top")

ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)

ax.set_aspect('equal')


plt.savefig("clair3_allmode_SNP.svg", dpi = 600, bbox_inches='tight')
# 显示图形
plt.show()
