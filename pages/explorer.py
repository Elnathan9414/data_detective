import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

data = st.session_state["filtered_data"]


st.title("Data Explorer: Uncover Insights from Your Data")
st.subheader("Explore your datasets with interactive visualizations and summary statistics.")

#st.line_chart(data['Sales'])
st.markdown("""### Summary Statistics""")
st.write(data.describe())

col1, col2 = st.columns(2)
with col1:
    st.markdown("""### Missing Values""")
    st.write(data.isnull().sum())
with col2:
    st.markdown("""### Drop ID Column""")
    data = data.drop(columns=["TransactionID"])
    st.write(data.describe())

st.markdown("""### Fill Missing Values """)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("Product categories")
    st.markdown(" Number of missing values in *ProductCategory*")
    st.write(data["ProductCategory"].isna().sum())
    st.write((data["ProductCategory"].isna().sum() / len(data)) * 100)
    st.markdown(" The missing values in product category is less than 10% of the total data, we can replace them with the most frequent category")
    most_frequent_category = data["ProductCategory"].mode()[0]
    data["ProductCategory"] = data["ProductCategory"].fillna(most_frequent_category)
    st.markdown(" Number of missing values in ProductCategory")
    st.write(data["ProductCategory"].isna().sum())
    st.bordered = True
with col2:
    
    st.markdown(" Number of missing values in *Sales*")
    st.markdown(" Number of missing values in *Sales*")
    st.write(data["Sales"].isna().sum())
    st.write((data["Sales"].isna().sum() / len(data)) * 100)
    st.markdown(" The missing values in sales is less than 10% of the total data, we can replace them with the most frequent category")
    most_frequent_sales = data["Sales"].mode()[0]
    data["Sales"] = data["Sales"].fillna(most_frequent_sales)
    st.markdown(" Number of missing values in *Sales*")
    st.write(data["Sales"].isna().sum())
with col3:
    st.markdown(" Number of missing values in *Satisfaction*")
    st.markdown(" Number of missing values in *Satisfaction*")
    st.write(data["Satisfaction"].isna().sum())
    st.write((data["Satisfaction"].isna().sum() / len(data)) * 100)
    st.markdown(" The missing values in satisfaction is less than 10% of the total data, we can replace them with the most frequent category")
    most_frequent_satisfaction = data["Satisfaction"].mode()[0]
    data["Satisfaction"] = data["Satisfaction"].fillna(most_frequent_satisfaction)
    st.markdown(" Number of missing values in *Satisfaction*")
    st.write(data["Satisfaction"].isna().sum())
    
    

st.markdown("""### Data overview visualizations""")
#Product Category,city and store
st.markdown("""### categorical data""")
col1, col2, col3 = st.columns(3)
with col1:
    
    fig = px.pie(
        data, 
        names="ProductCategory", 
        title="Product Category Distribution",
        hole=0.3 # donut chart
)

    fig.update_traces(textinfo="percent+label")

    st.plotly_chart(fig, use_container_width=True)
    
with col2:
     fig = px.pie(
        data, 
        names="City", 
        title="City Distribution",
        hole=0.3 # donut chart
)
     fig.update_traces(textinfo="percent+label")

     st.plotly_chart(fig, use_container_width=True)
with col3:
     fig = px.pie(
        data, 
        names="Store", 
        title="Store Distribution",
        hole=0.3 # donut chart
)

     fig.update_traces(textinfo="percent+label")

     st.plotly_chart(fig, use_container_width=True)


st.markdown("""### Numerical data""")
col1, col2 = st.columns(2)

with col1:
    
    fig = px.histogram(
        data,
        x="Sales",
        title="Sales Distribution",
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
  
    fig = px.histogram(
        data,
        x="Satisfaction",
        title="Satisfaction Distribution",
    )
    st.plotly_chart(fig, use_container_width=True)

col3, col4 = st.columns(2)
with col3:
   
    fig = px.histogram(
        data,
        x="DiscountPercent",
        title="Discount Percent Distribution",
    )
    st.plotly_chart(fig, use_container_width=True)
    
with col4:
    
    fig = px.histogram(
        data,
        x="Customers",
        title="Customers Distribution",
        
    )
    st.plotly_chart(fig, use_container_width=True)
col5, col6, col7, col8 = st.columns(4)
with col5:
    
    fig = px.box(
        data,
        x="DiscountPercent",
        title="Discount Percent Distribution",
    )
    st.plotly_chart(fig, use_container_width=True)
    
with col6:
    
    fig = px.box(
        data,
        x="Customers",
        title="Customers Distribution",
        
    )
    st.plotly_chart(fig, use_container_width=True)
with col7:
    
    fig = px.violin(
        data,
        x="Sales",
        title="Sales Distribution",
    )
    st.plotly_chart(fig, use_container_width=True)
with col8:
   
    fig = px.violin(
        data,
        x="Satisfaction",
        title="Satisfaction Distribution",
    )
    st.plotly_chart(fig, use_container_width=True)