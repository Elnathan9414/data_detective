import streamlit as st
import plotly.express as px
import pandas as pd


#loaad data
data = st.session_state["filtered_data"]
#variables

min_sales =   min_delta=pd.to_numeric(data["Sales"]).min()
avg_sales =   avg_delta=pd.to_numeric(data["Sales"]).mean()
max_sales =   max_delta=pd.to_numeric(data["Sales"]).max()
min_satisfaction =   min_delta=pd.to_numeric(data["Satisfaction"]).min()
avg_satisfaction =   avg_delta=pd.to_numeric(data["Satisfaction"]).mean()
max_satisfaction =   max_delta=pd.to_numeric(data["Satisfaction"]).max()


st.title("Sales Analysis")
col1, col2, col3, col4 = st.columns(4)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Averarage Sales",
        value=f"${avg_sales:.2f}",
        border=True,
        delta=f"min : {min_sales:.2f}  sales: {max_sales:.2f}",
        delta_color="inverse"
       
    )

with col2:
    st.metric(
        label="Satisfaction Rate",
        value=f"{avg_satisfaction:.2f}",
        border=True,
        delta=f"min : {min_satisfaction:.2f} max : {max_satisfaction:.2f}",
        
    )

with col3:
    st.metric(
        label="Total Orders",
        value="8,561",
        border=True,
        delta="+27.4%"
    )

with col4:
    st.metric(
        label="Avg Order Value",
        value=pd.to_numeric(data["Sales"]).mean(),
        border=True,
        delta="-0.5%"
    )