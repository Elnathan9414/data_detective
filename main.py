import streamlit as st

st.set_page_config(
    page_title="data detective app",
    page_icon=":pie chart:",
    layout="wide",
)

st.markdown("""
<style>
[data-testid="stSidebarNav"] {
    font-size: 22px;
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
        st.Page("pages/performances.py", title="store performances", icon=":material/data_usage:"),
        st.Page("pages/analysis.py", title="Sales analysis", icon=":material/store:"),
        st.Page("pages/trends.py", title="Trend analysis", icon=":material/pie_chart:"),
        st.Page("pages/insights.py", title=" Business Insights", icon=":material/insights:"),
    ]
)
pg.run()