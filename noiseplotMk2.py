from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go

from scipy.io.wavfile import read

fileName = 'whitenoise.wav'
wave = read(fileName)[1]
fs = read(fileName)[0]


f, Pxx_den = signal.periodogram(wave, fs)


fwin, Pxxwin_den = signal.welch(wave, fs, window='hann', nperseg=10000, scaling='density')

fig = px.line(x=f,y=Pxx_den, log_y=True)
fig.add_scatter(x=fwin, y=Pxxwin_den,mode="lines")

fig=go.Figure()
fig.add_trace(go.Scatter(x=f, y=Pxx_den,
                    mode='lines',
                    name='Raw Pxx'))
fig.add_trace(go.Scatter(x=fwin, y=Pxxwin_den,
                    mode='lines',
                    name='Windowed Pxx'))

fig.update_yaxes(type="log")
fig.update_xaxes(type="linear")

fig.update_layout(
    title=fileName + " Frequency Spectrum",
    yaxis_title="Ampltitude [V^2]",
    xaxis_title="Frequency [Hz]",
    legend_title="Legend",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    ))

plot(fig)
