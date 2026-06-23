import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="data detective app",
    page_icon=":pie chart:",
    layout="wide",
)

st.markdown("""
<style>
[data-testid="stSidebarNav"] {
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

#navigation
pg = st.navigation(
    [
        st.Page(
            "pages/home.py",
            title="Home",
            icon=":material/house:",
            default=True,
        ),
        st.Page("pages/explorer.py", title="Data explorer", icon=":material/menu_book:"),
        st.Page("pages/analysis.py", title="Sales analysis", icon=":material/store:"),
        st.Page("pages/performances.py", title="store performances", icon=":material/data_usage:"),
        st.Page("pages/trends.py", title="Trend analysis", icon=":material/pie_chart:"),
        st.Page("pages/insights.py", title=" Business Insights", icon=":material/insights:"),
    ]
)
st.set_page_config(
    page_title="Data Detective App",
    page_icon="📊",
    layout="wide",
)

# load data
data = pd.read_csv("store_data.csv")

# Sidebar
st.sidebar.title("🔍 Filters")

selected_city = st.sidebar.multiselect(
    "City",
    data["City"].unique(),
    default=data["City"].unique()
)

selected_store = st.sidebar.multiselect(
    "Store",
    data["Store"].unique(),
    default=data["Store"].unique()
)
selected_category = st.sidebar.multiselect(
    "Product Category",
    data["ProductCategory"].unique(),
    default=data["ProductCategory"].unique()
)
selected_year = st.sidebar.multiselect(
    "Year",
    data["year"].unique(),
    default=data["year"].unique()
)
selected_month = st.sidebar.multiselect(
    "month",    
    data["month"].unique(),
    default=data["month"].unique()
)
selected_day = st.sidebar.multiselect(
    "Day",
    data["day"].unique(),
     default=data["day"].unique()
)

# Stockage global
st.session_state["filtered_data"] = data[
    (data["City"].isin(selected_city))
    & (data["Store"].isin(selected_store))
    & (data["ProductCategory"].isin(selected_category))
    & (data["year"].isin(selected_year))
    & (data["month"].isin(selected_month))
    & (data["day"].isin(selected_day))
]
pg.run()