import streamlit as st
import plotly.express as px
import pandas as pd



data = pd.read_csv("store_data_cleaned.csv")


top_store = data.groupby("Store")["Sales"].sum().sort_values(ascending=False).head(1)
top_product_category = data.groupby("ProductCategory")["Sales"].sum().sort_values(ascending=False).head(1)
Worse_product_category = data.groupby("ProductCategory")["Sales"].sum().sort_values(ascending=True).head(1)
worst_store = data.groupby("Store")["Sales"].sum().sort_values(ascending=True).head(1)
worst_city = data.groupby("City")["Sales"].sum().sort_values(ascending=True).head(1)



st.title("Store Performances")
col1, col2, col3, col4,col5,col6,col7,col8 = st.columns(8)


with col1:
    st.metric(
        label="Top Sales",
        value=f"${data['Sales'].max():,.2f}",
        delta="+26.8%"
    )

with col2:
    st.metric(
        label="Top store",
        value=f"{top_store.index[0]}",
        delta="-0.3%"
    )

with col3:
    st.metric(
        label="Top Product Category",
        value=f"{top_product_category.index[0]}",
        delta="+27.4%"
    )

with col4:
    st.metric(
        label="top city",
        value=f"{data['City'].mode()[0]}",
        delta="-0.5%"
    )


with col5:
   st.metric(
        label="worst store",
        value=f"{worst_store.index[0]}",
        delta="-0.3%"
    )
with col6:
    st.metric(
        label="worst Product Category",
        value=f"{Worse_product_category.index[0]}",
        delta="+27.4%"
    )
with col7:
    st.metric(
        label="worst city",
        value=f"{worst_city.index[0]}",
        delta="-0.5%"
    )
with col8:
    st.metric(
        label="worst Sales",
        value=f"${data['Sales'].min():,.2f}",
        delta="+26.8%"
    )
sales_store = (
    data.groupby("Store")["Sales"]
    .sum()
    .sort_values(ascending=True)
    .reset_index()
)

# # sales chart 
# period = st.segmented_control(
#     "📅 Time Period",
#     ["Year", "Month", "Day"],
#     default="Month"
# )

# if period == "Year":
#     sales_period = data.groupby("year")["Sales"].sum().reset_index()
#     sales_period["year"] = sales_period["year"].astype(str)
#     fig = px.line(
#         sales_period,
#         x="year",
#         y="Sales",
#         markers=True,
#         title="Sales Trend by Year"
#     )

# elif period == "Month":
#     sales_period = data.groupby("month")["Sales"].sum().reset_index()
#     sales_period["month"] = sales_period["month"].astype(str)

#     fig = px.line(
#         sales_period,
#         x="month",
#         y="Sales",
#         markers=True,
#         title="Sales Trend by Month"
#     )

# else:
#     sales_period = data.groupby("day")["Sales"].sum().reset_index()
#     sales_period["day"] = sales_period["day"].astype(str)
#     fig = px.line(
#         sales_period,
#         x="day",
#         y="Sales",
#         markers=True,
#         title="Sales Trend by Day"
#     )

# st.plotly_chart(fig, use_container_width=True)



# col1, col2, col3 = st.columns(3)

# with col1:
#     #bar chart for top product categories
#     sales_product_category = (
#         data.groupby("ProductCategory")["Sales"]
#         .sum()
#         .sort_values(ascending=True)
#         .reset_index()
#     )

#     fig = px.bar(
#         sales_product_category,
#         x="Sales",
#         y="ProductCategory",
#         orientation="h",
#         title=" Total Sales by Product Category",
#         text_auto=True
#     )

#     st.plotly_chart(fig, use_container_width=True)
# with col2:
#     #bar chart for top cities
#     sales_city = (
#         data.groupby("City")["Sales"]
#         .sum()
#         .sort_values(ascending=True)
#         .reset_index()
#     )

#     fig = px.bar(
#         sales_city,
#         x="Sales",
#         y="City",
#         orientation="h",
#         title=" Total Sales by City",
#         text_auto=True
#     )

#     st.plotly_chart(fig, use_container_width=True)
# with col3:
#     #bar chart for top stores
#     sales_store = (
#         data.groupby("Store")["Sales"]
#         .sum()
#         .sort_values(ascending=True)
#         .reset_index()
#     )

#     fig = px.bar(
#         sales_store,
#         x="Sales",
#         y="Store",
#         orientation="h",
#         title=" Total Sales by Store",
#         text_auto=True
#     )

#     st.plotly_chart(fig, use_container_width=True)
    
# fig = px.violin(
#         data,
#         x="Store",
#         y="Sales",
#         title="Sales Distribution by Store"
#     )

# st.plotly_chart(fig, use_container_width=True)

st.components.v1.html("""<iframe title="retail_data" width="100%" height="800" 
                      src="https://app.powerbi.com/view?r=eyJrIjoiMTQ2N2RlNjUtZWFmZS00NmFhLWJiYzgtMzdjNGMxYmM4ODdhIiwidCI6Ijk3ZTNiNTliLThmY2YtNDAzOC1iM2JmLWFkOWFiZmQ1NjM4MyJ9&pageName=2cb24480488220861d07" frameborder="0" allowFullScreen="true"></iframe>""", height=800)