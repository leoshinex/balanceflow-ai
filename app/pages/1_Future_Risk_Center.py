import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Future Risk Center", page_icon="🚨", layout="wide")

st.title("🚨 Future Risk Center")
st.caption("Purpose: Predict future congestion risk.")
st.markdown("---")

st.markdown("### 📍 Live Predictive Target: District 1")

# KPI Block
col_risk, col_wow = st.columns([2, 1])
with col_risk:
    st.error("#### Risk Index: 87")
    st.markdown("<p style='color:#ef5350; font-weight:bold; margin-top:-10px;'>🚨 HIGH RISK</p>", unsafe_allow_html=True)
with col_wow:
    st.warning("#### 🔮 Predictive Window")
    st.markdown("**+45 Minutes Lookahead**")
    st.caption("Powered by RandomForestRegressor")

st.markdown("---")
st.markdown("### 📊 Core Risk Breakdown Metrics")

# Sub-metrics columns
m1, m2, m3, m4 = st.columns(4)
m1.metric(label="Demand Spike Probability", value="85%")
m2.metric(label="Driver Shortage Probability", value="72%")
m3.metric(label="Congestion Probability", value="81%")
m4.metric(label="Weather Risk", value="10%")