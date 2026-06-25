import streamlit as st

# ==========================
# Configuration de la page
# ==========================
st.set_page_config(
    page_title="Data Detective App",
    page_icon="🔎",
    layout="wide",
)

# ==========================
# Style
# ==========================
st.markdown("""
<style>
[data-testid="stSidebarNav"] {
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ==========================
# Navigation
# ==========================
pg = st.navigation(
    [
        st.Page(
            "pages/home.py",
            title="Home",
            icon=":material/home:",
            default=True,
        ),
        st.Page(
            "pages/explorer.py",
            title="Data Explorer",
            icon=":material/table_view:",
        ),
        st.Page(
            "pages/analysis.py",
            title="Sales Analysis",
            icon=":material/analytics:",
        ),
        st.Page(
            "pages/performances.py",
            title="Store Performances",
            icon=":material/bar_chart:",
        ),
        st.Page(
            "pages/trends.py",
            title="Trend Analysis",
            icon=":material/show_chart:",
        ),
        st.Page(
            "pages/insights.py",
            title="Business Insights",
            icon=":material/insights:",
        ),
    ]
)

# ==========================
# Lancer l'application
# ==========================
pg.run()