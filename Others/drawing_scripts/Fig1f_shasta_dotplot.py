# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 10:44:15 2024

@author: Mencius
"""

import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection



def log_NG50(in_list) -> list:
    log_list = list()
    for line in in_list:
        temp = list()
        for item in line:
            if item != 0:
                temp.append(math.log(item, 10))
            else:
                temp.append(0)
        log_list.append(temp)
    
    return log_list



N = 3
M = 3
ylabels = ["R10G6", "R9G6", "R10D0"][::-1]
xlabels = ["R9G4", "R9G6", "R10D0"]

x, y = np.meshgrid(np.arange(M), np.arange(N))


NG50 = [[34797443, 36731124, 470891],
        [34786517, 36713966, 468497],
        [0, 0, 10197749]]

NG50 = np.array(log_NG50(NG50))
print(NG50)

yak_QV = np.array([[32.661, 33.835, 34.358],
              [32.679, 35.458, 37.648],
              [0, 0, 39.549]
               ])

plt.figure(figsize=(8, 8))
fig, ax = plt.subplots()

R = NG50/NG50.max()/2
circles = [plt.Circle((j,i), radius=r/1.5, edgecolor = "black", linewidth = 2) for r, j, i in zip(R.flat, x.flat, y.flat)]
col = PatchCollection(circles, array = yak_QV.flatten(), cmap="Blues")
col.set_clim(vmin=30, vmax=40)  
ax.add_collection(col)

# ax.xaxis.tick_top()

ax.set(xticks=np.arange(M), yticks=np.arange(N),
       xticklabels=xlabels, yticklabels=ylabels)
ax.set_xticks(np.arange(M+1)-0.5, minor=True)
ax.set_yticks(np.arange(N+1)-0.5, minor=True)
plt.xlabel("Data")
plt.ylabel("Config")
plt.title("Shasta genome assembly", fontsize = 14)
plt.rcParams['font.family'] = "Arial"
ax.set_aspect('equal', adjustable='box')
ax.grid(which='minor')

# plt.gca().xaxis.set_label_position('top')
fig.colorbar(col)


fig.savefig("dotplot.svg", dpi = 600, bbox_inches='tight')
plt.show()