import streamlit as st

st.set_page_config(page_title="AI Decision Timeline", page_icon="🏆", layout="wide")

st.title("🏆 AI Decision Timeline")
st.subheader("Final Demo Screen & Storytelling Journey")
st.markdown("---")

# Draw professional vertical timeline
st.markdown("""
<div style='margin-left: 20px; border-left: 4px solid #00cc96; padding-left: 20px;'>
    <h3 style='color:#ef5350;'>🕒 07:30 — Risk Detected</h3>
    <p>AI engine flags an imbalance crisis imminent in District 1.</p>
    <br>
    <h3 style='color:#002b36;'>🕒 07:35 — 2,000 Users Targeted</h3>
    <p>Flexible sub-segments mapped based on Adaptability Scores.</p>
    <br>
    <h3 style='color:#3b5998;'>🕒 07:40 — 684 Accepted Ride Pool</h3>
    <p>Real-time fleet optimization mitigates localized congestion.</p>
    <br>
    <h3 style='color:#00cc96;'>🕒 08:00 — DBS Improved (43 ➔ 61)</h3>
    <p>Supply and demand fully re-orchestrated across checkpoints.</p>
    <br>
    <h3 style='color:#00cc96;'>🎉 08:30 — Surge Pricing Avoided</h3>
    <p>Gridlock dissolved. City efficiency maximized seamlessly.</p>
</div>
""", unsafe_allow_html=True)