# Sample Page

This is an attempt at writing some text.

There's an experiment for embedding a Plotly plot below.

import numpy as np

np.random.seed(42)
x = np.arange(10)
y = np.random.uniform(low=-10., high=10., size=x.shape[0])

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y)
ax.set_xlabel('stuff')
ax.set_ylabel('beans');

import plotly.offline

import plotly.graph_objects as go
import plotly.offline as ploff
from IPython.core.display import display, HTML

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=x,
    y=y,
    mode="markers"))

ploff.plot(fig, filename='images/testplot.html')
display(HTML('images/testplot.html'))

from IPython.core.display import display, HTML
display(HTML('images/testplot.html'))

Here's a test of citation {cite}`kumfts2019`

