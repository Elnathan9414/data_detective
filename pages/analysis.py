import streamlit as st

st.components.v1.html("""
<iframe
    title="retail_data"
    width="100%"
    height="800"
    src="https://app.powerbi.com/view?r=eyJrIjoiMTQ2N2RlNjUtZWFmZS00NmFhLWJiYzgtMzdjNGMxYmM4ODdhIiwidCI6Ijk3ZTNiNTliLThmY2YtNDAzOC1iM2JmLWFkOWFiZmQ1NjM4MyJ9"
    frameborder="0"
    allowfullscreen>
</iframe>
""", height=800)