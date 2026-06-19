import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv("store_data.csv")


st.title("Data Explorer: Uncover Insights from Your Data")
st.subheader("Explore your datasets with interactive visualizations and summary statistics.")

#st.line_chart(data['Sales'])
st.markdown("""### Summary Statistics""")
st.write(data.describe())

st.markdown("""### empty values""")
st.write(data.isnull().sum())

st.markdown("""### Drop ID Column""")
data = data.drop(columns=["TransactionID"])
st.write(data.describe())
st.markdown("""### Product categories""")
st.markdown("""#### Number of missing values in ProductCategory""")
st.write(data["ProductCategory"].isna().sum())
st.write((data["ProductCategory"].isna().sum() / len(data)) * 100)
st.markdown(" The missing values in product category is less than 5% of the total data, we can replace them with the most frequent category")
most_frequent_category = data["ProductCategory"].mode()[0]
data["ProductCategory"] = data["ProductCategory"].fillna(most_frequent_category)
st.markdown(" Number of missing values in ProductCategory")
st.write(data["ProductCategory"].isna().sum())

st.markdown("### Sales Distribution")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Histogram of Sales")
    fig = px.histogram(
    data,
    x="Sales",
    title="Sales Distribution",
)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### Box Plot of Sales")

    fig = px.box(
    data,
    y="Sales",
    title="Sales Distribution"
)
    st.plotly_chart(fig, use_container_width=True)
    

#customer
st.markdown("""### customer""")
st.markdown("""#### Number of missing values customer""")
st.write(data["Customers"].isna().sum())
st.write((data["Customers"].isna().sum() / len(data)) * 100)
st.markdown(" The missing values in customers is equal to 5% of the total data, we can replace them with the most frequent category")
most_frequent_customer = data["Customers"].mode()[0]
data["Customers"] = data["Customers"].fillna(most_frequent_customer)
st.markdown(" Number of missing values in Customers")
st.write(data["Customers"].isna().sum())

st.markdown("### customers Distribution")


col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Histogram of Customers")
    fig = px.histogram(
    data,
    x="Customers",
    title="Customers Distribution",
)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### Box Plot of Customers")

    fig = px.box(
    data, 
    y="Customers", 
    title="Customers Distribution"
)
    st.plotly_chart(fig, use_container_width=True)
    
# satisfaction
st.markdown("""### satisfaction""")
st.markdown("""#### Number of missing values satisfaction""")
st.write(data["Satisfaction"].isna().sum())
st.write((data["Satisfaction"].isna().sum() / len(data)) * 100)
most_frequent_satisfaction = data["Satisfaction"].mode()[0]
data["Satisfaction"] = data["Satisfaction"].fillna(most_frequent_satisfaction)
st.markdown(" Number of missing values in Satisfaction")
st.write(data["Satisfaction"].isna().sum())

st.markdown("### satisfaction Distribution")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Histogram of Satisfaction")
    fig = px.histogram(
    data,
    x="Satisfaction",
    title="Satisfaction Distribution",
)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("#### Box Plot of Satisfaction")

    fig = px.box(
    data, 
    y="Satisfaction", 
    title="Satisfaction Distribution"
)

    st.plotly_chart(fig, use_container_width=True)

#Product Discount
st.markdown("""### Product Discount""")
col1, col2 = st.columns(2)
with col1:
    fig = px.histogram(
    data,
    x="DiscountPercent",
    title="Discount Percent Distribution",
)
    st.plotly_chart(fig, use_container_width=True)
with col2:
    st.markdown("#### Box Plot of Discount Percent")

    fig = px.box(
    data, 
    y="DiscountPercent", 
    title="Discount Percent Distribution"
)

    st.plotly_chart(fig, use_container_width=True)

#Product Category,city and store
st.markdown("""### Pie charts""")
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

