import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import folium as fl
from folium.plugins import MarkerCluster

st.title('DATA ANALYSIS MINI PROJECT')
st.markdown('''This is a mini project for data analysis using streamlit and plotly.
            Here we are using a dataset of universities and their rankings and we are going to analyse how the universities are ranked and what are the factors that are affecting the rankings of the universities.
            We can obtain analysis on female and male percentage in the universities and also the subject wise analysis of the universities.
            We are going to analyse the data and visualise it using plotly and streamlit.
            We will be using the following libraries for this project: Pandas, Numpy, Matplotlib, Streamlit, Plotly, Folium.
            ''')
st.subheader('ADMISSION IN UNIVERSITIES')
# Load data
df = pd.read_csv('dataset.csv')
# Show dataset
if st.sidebar.checkbox('Show Dataset'):
    st.write(df)

country_count = df.country.value_counts().reset_index()
country_count.columns = ['country','total_score']
country_top_20 = country_count.head(20)
fig1 = px.pie(country_top_20,'country','total_score',title='Country wise')
if st.sidebar.checkbox('Show Country Wise'):
    st.plotly_chart(fig1)

subject_count = df.subject.value_counts().reset_index()
subject_count.columns = ['subject','university_name']
fig2 = px.pie(subject_count,'subject','university_name',title='Subject Wise')
if st.sidebar.checkbox('Show Subject Wise'):
    st.plotly_chart(fig2)

fig3 = px.box(df,'subject',title='Subject')
if st.sidebar.checkbox('Show Box Plot'):
    st.plotly_chart(fig3)

fig4 = px.violin(df,'citations',title='Citations')
if st.sidebar.checkbox('Show Violin Plot'):
    st.plotly_chart(fig4)

fig5 = px.scatter(df,'world_rank','teaching',color='country',size='teaching',hover_data=['university_name'],title='World Rank vs Teaching')
fig6 = px.scatter(df,'world_rank','research',color='country',size='research',hover_data=['university_name'],title='World Rank vs Research')
if st.sidebar.checkbox('Show world rank vs teaching and research'):
    st.plotly_chart(fig5)
    st.plotly_chart(fig6)


fig8 = px.scatter(df,'female_percentage','subject',color='subject',title='FEMALE PERCENT')
if st.sidebar.checkbox('Show female percent'):
    st.plotly_chart(fig8)

fig9 = px.scatter(df,'male_percentage','subject',color='subject',title='MALE PERCENT')
if st.sidebar.checkbox('Show male percent'):
    st.plotly_chart(fig9)
    
    

