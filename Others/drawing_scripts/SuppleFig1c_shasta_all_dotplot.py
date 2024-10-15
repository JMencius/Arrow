# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 19:28:43 2024

@author: Mencius
"""

import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection

matplotlib.rcParams['font.size'] = 6

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
M = 8
ylabels = ["R10", "R9G6", "R10D0"][::-1]
xlabels = ["R9G4FAST", "R9G4HAC", "R9G6FAST", "R9G6HAC", "R9G6SUP", "R10D0FAST", "R10D0HAC", "R10D0SUP"]

x, y = np.meshgrid(np.arange(M), np.arange(N))


NG50 = [[25700415, 34797443, 31462641, 34497500, 36731124, 12529106, 930619, 470891],
        [25673661, 34786517, 31420453, 34480960, 36713966, 12208230, 930507, 468497],
        [0, 0, 0, 0, 0, 0, 4145796, 10197749]]

NG50 = np.array(log_NG50(NG50))
print(NG50)

yak_QV = np.array([[23.940, 32.679, 29.364, 33.282, 33.835, 29.115, 34.062, 34.358],
                   [23.667, 32.661, 28.960, 34.820, 35.458, 29.908, 37.075, 37.648],
                   [0, 0, 0, 0, 0, 0, 38.724, 39.549]])

plt.figure(figsize=(16, 4))
fig, ax = plt.subplots()

R = NG50/NG50.max()/2
circles = [plt.Circle((j,i), radius=r/1.5, edgecolor = "black", linewidth = 2) for r, j, i in zip(R.flat, x.flat, y.flat)]
col = PatchCollection(circles, array = yak_QV.flatten(), cmap="Blues")
col.set_clim(vmin=20, vmax=40)  
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


fig.savefig("shata_all_dotplot.png", dpi = 600, bbox_inches='tight')
plt.show()