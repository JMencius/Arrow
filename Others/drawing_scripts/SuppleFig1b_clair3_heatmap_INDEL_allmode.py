# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:51:26 2024

@author: Mencius
"""


import seaborn as sns
import matplotlib.pyplot as plt

# 创建数据
clair3_INDEL = [[0.076218, 0.069391, 0.260955, 0.103317, 0.41537, 0.452292, 0.64935, 0.866365, 0.903652],
                [0.067985, 0.056593, 0.231753, 0.090371, 0.387316, 0.442923, 0.702155, 0.88193, 0.902032],
                [0.199536, 0.16021, 0.635044, 0.338343, 0.799815, 0.854914, 0.630442, 0.796299, 0.832446],
                [0.352299, 0.319729, 0.723378, 0.542729, 0.76281, 0.766844, 0.576664, 0.800324, 0.806801],
                [0.392592, 0.388571, 0.401098, 0.317383, 0.269323, 0.296178, 0.258338, 0.46136, 0.520609]]

row_labels = ["R9G2", "R9G4FAST", "R9G4HAC", "R9G6FAST", "R9G6HAC", "R9G6SUP", "R10D0FAST", "R10D0HAC", "R10D0SUP"]
col_labels = ["R9G2", "R9G4HAC", "R9G5SUP", "R10D0HAC", "R10D0SUP"][::-1]


# 绘制热图
plt.figure(figsize=(12, 8))
plt.tight_layout()

ax = sns.heatmap(clair3_INDEL, cmap = "Blues", vmin = 0, vmax = 1,
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

plt.title("Clair3 INDEL calling", fontsize = 14)


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

ax.set_aspect('equal')


plt.savefig("clair3_allmode_INDEL.svg", dpi = 600, bbox_inches='tight')
# 显示图形
plt.show()
