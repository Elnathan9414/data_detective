import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


#loaad data
data = st.session_state["filtered_data"]
#variables

min_sales =   min_delta=pd.to_numeric(data["Sales"]).min()
avg_sales =   avg_delta=pd.to_numeric(data["Sales"]).mean()
max_sales =   max_delta=pd.to_numeric(data["Sales"]).max()
min_satisfaction =   min_delta=pd.to_numeric(data["Satisfaction"]).min()
avg_satisfaction =   avg_delta=pd.to_numeric(data["Satisfaction"]).mean()
max_satisfaction =   max_delta=pd.to_numeric(data["Satisfaction"]).max()
min_discount =   min_delta=pd.to_numeric(data["DiscountPercent"]).min()
avg_discount =   avg_delta=pd.to_numeric(data["DiscountPercent"]).mean()
max_discount =   max_delta=pd.to_numeric(data["DiscountPercent"]).max()


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
        label="customer Orders",
        value=f"{data['Customers'].count()}",
        border=True,
        delta=f"min : {data['Customers'].min()} max : {data['Customers'].max()}",
        delta_color="inverse"

    )

with col4:
    st.metric(
        label="Discount Rate",
        value=f"{avg_discount:.2f}%",
        border=True,
        delta=f"min : {min_discount:.2f}% max : {max_discount:.2f}%"
    )

st.subheader("Sales Analysis")

#line chart

class_sales = data.groupby(
    ["year", "month", "day"]
)["Sales"].sum().reset_index()

with st.container(border=True):

    selected_years = st.multiselect(
        "Year",
        options=sorted(class_sales["year"].unique()),
        default=[class_sales["year"].unique()[0]]
    )

    filtered_sales = class_sales[
        class_sales["year"].isin(selected_years)
    ]

    fig = px.bar(
        filtered_sales,
        x="day",
        y="Sales",
        color="month",
        title="Sales Over Time"
    )

    st.plotly_chart(fig, use_container_width=True)

  
# all_sales = data.groupby("year")["Sales"].sum().reset_index()
# all_sales["year"] = all_sales["year"].astype(str)
# fig = px.line(all_sales, x="year", y="Sales", title="Total Sales Over Time")
# st.plotly_chart(fig, use_container_width=True)
col1, col2, col3 = st.columns(3)
with col1:
    all_sales = data.groupby("ProductCategory")["Sales"].sum().reset_index()
    fig = px.bar(all_sales, x="ProductCategory", y="Sales", title="Total Sales by Category")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    #sales by city
    city_sales = data.groupby("City")["Sales"].sum().reset_index()
    fig = px.bar(city_sales, x="City", y="Sales", title="Total Sales by City")
    st.plotly_chart(fig, use_container_width=True)

with col3:
    #sales by store
    store_sales = data.groupby("Store")["Sales"].sum().reset_index()
    fig = px.bar(store_sales, x="Store", y="Sales", title="Total Sales by Store")
    st.plotly_chart(fig, use_container_width=True)

#sales by Customer
customer_sales = data.groupby("Customers")["Sales"].count().reset_index()
fig = px.bar(customer_sales, x="Customers", y="Sales", title="Total Sales by Customer")
st.plotly_chart(fig, use_container_width=True)

#Discount Percent Distribution per product category

col1, col2 = st.columns(2)

# Average Discount by Product Category
discount_product = (
    data.groupby("ProductCategory")["DiscountPercent"]
    .mean()
    .reset_index()
)

with col1:
    fig1 = px.bar(
        discount_product,
        x="ProductCategory",
        y="DiscountPercent",
        title=" Average Discount by Product Category"
    )
    st.plotly_chart(fig1, use_container_width=True)

# Discount Distribution by Product Category
with col2:
    fig2 = px.box(
        data,
        x="ProductCategory",
        y="DiscountPercent",
        title=" Discount Distribution by Product Category"
    )
    st.plotly_chart(fig2, use_container_width=True)
    
