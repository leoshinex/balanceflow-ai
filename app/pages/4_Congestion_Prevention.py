import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Congestion Prevention Simulator", page_icon="📉", layout="wide")

st.title("📉 Congestion Prevention Simulator")
st.markdown("---")

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("### 🔴 WITHOUT BALANCEFLOW")
    st.error("81% → 87% → 92%")
    st.markdown("<p style='color:#ef5350; font-weight:bold;'>🚨 SURGE TRIGGERED</p>", unsafe_allow_html=True)

with col_right:
    st.markdown("### 🟢 WITH BALANCEFLOW")
    st.success("81% → 72% → 63% → 58%")
    st.markdown("<p style='color:#00cc96; font-weight:bold;'>✅ SURGE AVOIDED</p>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("### ⚡ Real-Time Congestion Trajectory Simulation")

# Draw timeline charts comparison
fig = go.Figure()
fig.add_trace(go.Scatter(x=["T1", "T2", "T3", "T4"], y=[81, 87, 92, None], name="Without Balanceflow", line=dict(color="#ef5350", width=4)))
fig.add_trace(go.Scatter(x=["T1", "T2", "T3", "T4"], y=[81, 72, 63, 58], name="With Balanceflow", line=dict(color="#00cc96", width=4)))
fig.update_layout(title="Congestion Risk Timeline Simulation", xaxis_title="Timeline Checkpoints", yaxis_title="Risk Index (%)")
st.plotly_chart(fig, use_container_width=True)