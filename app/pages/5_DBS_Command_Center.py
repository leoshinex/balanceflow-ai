import streamlit as st

st.set_page_config(page_title="DBS Command Center", page_icon="📊", layout="wide")

st.title("📊 DBS Command Center")
st.caption("Purpose: Show clear bottom-line business impact.")
st.markdown("---")

st.markdown("### 📈 Main KPI Transformation")
st.info("#### Demand Balance Score (DBS): 43 ➔ 61")

st.markdown("---")
st.markdown("### 💼 Operational Business Metrics")

b1, b2, b3, b4 = st.columns(4)
b1.metric(label="Waiting Time", value="-12%", delta="Improved")
b2.metric(label="Empty Mileage", value="-9%", delta="Improved")
b3.metric(label="Driver Utilization", value="+11%", delta="Optimized")
b4.metric(label="Surge Events", value="-18%", delta="Prevented")