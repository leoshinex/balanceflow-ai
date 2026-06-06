import streamlit as st

st.set_page_config(page_title="Balanceflow AI - Home", page_icon="🏙️", layout="wide")

st.title("🏙️ BALANCEFLOW AI")
st.subheader("The Demand Orchestration Layer for Sustainable Cities")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📊 Main KPI")
    st.error("#### Current DBS: 43")
    st.markdown("<p style='color:#ef5350; font-weight:bold; margin-top:-10px;'>⚠️ HIGH IMBALANCE RISK</p>", unsafe_allow_html=True)
    st.caption("Demand Balance Score (DBS) indicates critical supply-demand gap in peak hours.")
    
with col2:
    st.markdown("### 🔮 Predicted Event")
    st.info("#### Predicted Surge Event")
    st.markdown("📍 **Location:** District 1")
    st.markdown("⏰ **Time:** 08:00 AM")
    st.caption("AI engine flags imminent gridlock and surge pricing risk 45 minutes ahead.")