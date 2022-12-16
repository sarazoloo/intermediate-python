import streamlit as st

import pandas as pd
import numpy as np

import plotly.express as px
import matplotlib.pyplot as plt
import statistics
import seaborn as sns



st.set_page_config(page_title = 'Multipage App', 
                   page_icon = ":bar_chart:", 
                   layout = 'wide')

st.title('Zangia - Job Listings')
st.write('This is a simple app that analysis job vacancies listed on "zangia.mn"')

df = pd.read_csv('zangia_data.csv')

#---Stats ---


total_jobs = len(df)
average_salary = round(df['Salary Range'].mean(),1)
total_company = len(pd.unique(df['Company_name']))


left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader('Total Jobs: ')
    st.subheader(total_jobs)

with middle_column:
    st.subheader('Average Job Salary: ')
    st.subheader(f" ₮ {average_salary} MNT")
    
with right_column:
    st.subheader('Total Companies: ')
    st.subheader(total_company)

st.markdown('---')

st.subheader('Salary analysis')

#salary histogram
st.markdown("#### Average median salaries")

fig, ax = plt.subplots(figsize =(16, 9))
ax.hist(df['Salary Range'], bins=10)
ax.set_xlabel("Average Salary Range", color = 'k')
st.pyplot(fig)


#sector by salary
st.markdown("#### Average salary by job sector")


fig1, ax1 = plt.subplots(figsize =(16, 9))
ax1.barh(df['Job Sector'], df['Salary Range'])
ax1.set_xlabel("Average Salary", color = 'k')
ax1.set_ylabel("Job Sector", color = 'k')

st.pyplot(fig1)
