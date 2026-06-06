import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Behavioral Intelligence", page_icon="🧠", layout="wide")

st.title("🧠 Behavioral Intelligence")
st.caption("Purpose: Find flexible users within the ecosystem.")
st.markdown("---")

# Main KPI
st.metric(label="Flexible Users Identified", value="2,000 Users")

st.markdown("### 🔝 Top Behavioral Segments")
s1, s2, s3 = st.columns(3)

with s1:
    st.info("#### 💰 Budget Saver\n**Adaptability Score = 82**")

with s2:
    st.success("#### 🌱 Eco Conscious\n**Adaptability Score = 76**")

with s3:
    # Đã sửa từ st.help sang st.warning để đồng bộ giao diện hộp màu
    st.warning("#### ⚡ Convenience Seeker\n**Adaptability Score = 61**")

st.markdown("---")
st.markdown("### 📉 Adaptability Score Distribution (Visualization)")

# Load real users data to draw distribution chart
try:
    df_users = pd.read_csv("data/users.csv")
    fig = px.histogram(
        df_users, x="adaptability_score", 
        nbins=30, title="User Adaptability Score Distribution",
        color_discrete_sequence=["#00cc96"], labels={"adaptability_score": "Adaptability Score"}
    )
    st.plotly_chart(fig, use_container_width=True)
except:
    st.warning("Please ensure data/users.csv exists to render the interactive chart.")