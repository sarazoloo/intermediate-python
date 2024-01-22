import streamlit as st

import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup

st.title('Zangia Job Listings')

st.markdown(f""" ## Zangia data scaped and loaded""")

baseurl = 'https://www.zangia.mn/'


def scrape_links(a):
    '''
    This function scrapes through a to b number of pages in the zangai job listings.
    a and b both must be an integer.
    
    '''
    for i in range(0,a):
        url = requests.get("https://www.zangia.mn/job/list/pg.(i)")
        soup = BeautifulSoup(url.text, 'html.parser')
        rows = soup.find('div', class_ = 'list')
    
        row = rows.find_all('div', class_ = 'ad')
        links = []
        for item in row:
            for link in item.find_all('a', href=True):
                links.append(baseurl + link['href'])
    return links

def scrape_listing(joblinks):
    job_result = []
    for b in joblinks:
        url1 = requests.get(b)
        soup1 = BeautifulSoup(url1.text, 'html.parser')
        jobs = soup1.find('div', class_ = 'job-holder')
    
        if jobs is not None: # some of the jobs don't has a none type so I made an if statement
            for item in jobs.find_all('div', class_ = 'job-body'):
                title = item.find('h3').text.split("/",1)[0] # this is splitting the string by "/" and getting the first element
                divs = item.find_all('div', class_ = 'section') # there are also a few divs with the same class so this makes it easier to choose which div to get
                description = divs[0].get_text().strip().replace('Гүйцэтгэх үндсэн үүрэг','').replace('\n',' ')
            
                details = item.find('div', class_ = 'details')
                spans = details.find_all('span')
                sector = spans[1].get_text().strip() #there are 4 different spans so this chooses the first one
                salary_range = spans[-1].get_text().strip().replace('Тохиролцоно','').replace(' -ааc дээш','') # this chose the last span
                job_dict = {'Job Title':title, 'Job Description':description, 'Job Sector':sector, 
                            'Salary Range': salary_range} 
                job_result.append(job_dict)
        
                data = pd.DataFrame(job_result)
    return data


st.write('Choose the number of job listings ')

pg_numb = st.slider("Job listings: ", 0, 500, step= 50 )


if st.button('Show Listings', key = 1):
    a = int(np.ceil(pg_numb / 50))
    listings = scrape_listing(scrape_links(a))
    st.write(listings)
    
    






