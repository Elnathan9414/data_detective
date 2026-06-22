import streamlit as st
import plotly.express as px

st.title("Store Performances")
col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        label="Best Store Revenue",
        value="$4,314,043",
        delta="+26.8%"
    )

with col2:
    st.metric(
        label="Worst Store Revenue",
        value="11.7%",
        delta="-0.3%"
    )

with col3:
    st.metric(
        label="Top Product Category",
        value="8,561",
        delta="+27.4%"
    )

with col4:
    st.metric(
        label="Average Discoun",
        value="$504",
        delta="-0.5%"
    )