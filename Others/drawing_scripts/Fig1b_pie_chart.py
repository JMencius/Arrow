# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 15:04:09 2024

@author: Mencius
"""

import plotly.graph_objects as go


labels = ["only flowcell info", 
          "only basecaller info", 
          "with both info", 
          "no info"]

values = [10307 - 1346, 
          2713 - 1346, 
          1346, 
          181528 - 10307 - 2713 + 1346]

values = [i / sum(values) * 100 for i in values]
colors = ["#71ACD9",
          "#C2D5EE",
          "#5B709B",
          "lightgrey"]
          

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(values = values,
                             labels = labels,
                             direction = "clockwise",
                             sort = False,
                             marker = dict(colors = colors))])


fig.update_traces(showlegend = True,
                  textinfo = 'value', 
                  texttemplate = '%{value:.2f}%',
                  marker = dict(line = dict(color='white', width = 0.2)))

fig.update_layout(font = dict(family = "Arial, sans-serif", size = 18))

fig.update_layout(legend = dict(orientation = "h", yanchor = "bottom", y = -0.2, xanchor = "center", x = 0.5))

fig.write_image("fig1B.svg", scale = 3)