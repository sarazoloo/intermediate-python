import streamlit as st

import pandas as pd
import numpy as np

import plotly.express as px
import matplotlib.pyplot as plt
import statistics
import seaborn as sns
import plotly.figure_factory as ff




st.title('Job - recommendation')
st.write('Please filter to your liking on the sidebar')

df = pd.read_csv('zangia_data.csv')


st.sidebar.header('Please filter here')

sectors = st.sidebar.multiselect (
    'Select the sector: ',
    options = df['Job Sector'].unique(),
    default = df['Job Sector'].unique()
)

company = st.sidebar.multiselect (
    'Select the company: ',
    options = df['Company_name'].unique(),
    default = df['Company_name'].unique()[1]
)


#salary = st.sidebar.slider ()
df_selection = df.query('`Job Sector` == @sectors & Company_name == @company ')

st.dataframe(df_selection)