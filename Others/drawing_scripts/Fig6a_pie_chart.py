# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:04:09 2024

@author: Mencius
"""

import plotly.graph_objects as go


labels = ["R10_G6_FAST",
          "R9_G6_FAST",
          "R9_G6_HAC",
          "R9_G6_SUP",
          "R9_G4_FAST",
          "R9_G4_HAC",
          "R9_G2_NONE",
          "Others"
]

values = [266,
          354,
          822,
          1132,
          607,
          4759,
          418,
          110]

values = [i / sum(values) * 100 for i in values]
colors = ["#77bfa6",
          "#f39164",
          "#949ed0",
          "#f48377",
          "#f7b566",
          "#b3dc6c",
          "#f8cfe6",
          "#e0c596"]
          

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(values = values,
                             labels = labels,
                             direction = "clockwise",
                             sort = True,
                             marker = dict(colors = colors)
                             )])
                             #marker = dict(colors = colors))])


fig.update_traces(showlegend = True,
                  textinfo = 'value', 
                  texttemplate = '%{value:.2f}%',
                  marker = dict(line = dict(color='white', width=0.1)))

fig.update_layout(font = dict(family = "Arial, sans-serif", size = 18))

# fig.update_layout(legend = dict(orientation = "h", yanchor = "bottom", y = -0.2, xanchor = "center", x = 0.5))

fig.write_image("fig5B.svg", scale = 3)