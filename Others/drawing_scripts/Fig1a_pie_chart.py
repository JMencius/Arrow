# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:26:39 2024

@author: Mencius
"""

import plotly.graph_objects as go


labels = ["with raw data", "without raw data"]
values = [10973, 673620 - 10973]

values = [i / sum(values) * 100 for i in values]
colors = ["#8E2D30", "lightgrey"]
          

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

fig.write_image("fig1A.svg", scale = 3)

