import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv("data-penumpang-bus-transjakarta-januari-desember-2021.csv")
data.set_index('bulan', inplace=True)
data = data.dropna(subset=['jenis'])
data['jenis'] = data['jenis'].astype(str)

st.title('Data Penumpang Bus TransJakarta')

month = st.slider(
    'Select Month',
    min_value=1,
    max_value=12,
    value=1,
    step=1
)

x = st.selectbox(
    'Select X-Axis',
    ['jenis', 'kode_trayek', 'trayek', 'jumlah_penumpang'],
    index=0
)

y = st.selectbox(
    'Select Y-Axis',
    ['jenis', 'kode_trayek', 'trayek', 'jumlah_penumpang'],
    index=1
)

fig = make_subplots()
filtered_data = data[data.index == month]
fig.add_trace(go.Scatter(x=filtered_data[x], y=filtered_data[y], mode='lines'))
fig.update_layout(
    title='Data Penumpang Bus TransJakarta - Bulan {}'.format(month),
    xaxis_title=x,
    yaxis_title=y
)

st.plotly_chart(fig)
