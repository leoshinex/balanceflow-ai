import streamlit as st

st.set_page_config(page_title="What-if City Simulator", page_icon="🎛️", layout="wide")

st.title("🎛️ What-if City Simulator")
st.markdown("---")

# User slider input
adoption_rate = st.slider("Select System Adoption Rate (%)", min_value=0, max_value=20, value=5, step=5)

st.markdown("### 🔮 Dynamic Projected Outputs")

# Calculate results on the fly matching user specs
if adoption_rate == 5:
    cong, co2, wait = "6%", "4%", "5%"
elif adoption_rate == 10:
    cong, co2, wait = "13%", "9%", "11%"
elif adoption_rate == 15:
    cong, co2, wait = "20%", "14%", "17%"
else: # 20%
    cong, co2, wait = "26%", "19%", "22%"

out1, out2, out3 = st.columns(3)
out1.metric(label="Congestion Reduction", value=cong)
out2.metric(label="CO₂ Emissions Reduced", value=co2)
out3.metric(label="Waiting Time Reduction", value=wait)