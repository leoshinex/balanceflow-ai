import streamlit as st

st.set_page_config(page_title="Intervention Engine", page_icon="⚡", layout="wide")

st.title("⚡ Intervention Engine")
st.caption("Purpose: Deliver personalized recommendations to optimize demand-supply alignment.")
st.markdown("---")

card1, card2 = st.columns(2)

with card1:
    st.markdown("### 🚗 Card 1: Ride Pool")
    st.success("💰 **Save 15,000 VND** | ⏱️ **Pickup 3 mins faster**")
    deploy_btn = st.button("Deploy Intervention", key="btn_c1", type="primary")

with card2:
    st.markdown("### 🏃‍♂️ Card 2: Flexible Pickup")
    st.info("🚶‍♂️ **Walk 80m** | 💰 **Save 10,000 VND**")
    st.button("Deploy Intervention", key="btn_c2")

st.markdown("---")
if deploy_btn:
    st.markdown("### 🚀 Deployment Live Result")
    res1, res2 = st.columns(2)
    res1.metric(label="Users Targeted", value="2,000 Users")
    res2.metric(label="Expected Acceptance", value="34%", delta="Target Met")