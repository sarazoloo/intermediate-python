import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px
import matplotlib.pyplot as plt
import statistics
import seaborn as sns
import plotly.figure_factory as ff

st.set_page_config(layout="wide")
st.title('Zangia - Data')
st.markdown('## The following job data was scraped from zangai.mn')
n = '\n'
description = (f""" 
    Dataframe columns: {n}
    Job Title: job position {n}
    Job Description: The expectations of the job {n}
    Job Sector: the industry sector {n}
    Salary Range: median of the minimum and maximum salary listed --> dtype is an integer {n}
    Date Published: the published date of the job opening --> dtype is datetime %Y-%m-%d {n}
    Contact : contact number of company {n}
    Company_name : Name of the company """)

st.write(description)
df = pd.read_csv('zangia_data.csv')
st.dataframe(df)

