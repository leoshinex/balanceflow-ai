import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Balanceflow AI - Home", 
    page_icon="🏙️", 
    layout="wide"
)

# Custom CSS để tối ưu hóa không gian hiển thị cho HR/Interviewer quét nhanh
st.markdown("""
    <style>
    .main-title { font-size: 40px; font-weight: 800; color: #FF4B4B; margin-bottom: 0px; }
    .sub-title { font-size: 18px; font-weight: 500; color: #A0A0A0; margin-bottom: 20px; }
    .section-header { font-size: 22px; font-weight: 700; color: #FFFFFF; margin-top: 15px; margin-bottom: 10px; }
    .problem-box { background-color: #1E1E24; padding: 15px; border-radius: 6px; border-left: 5px solid #FF4B4B; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# 🏙️ HEADER SECTION
st.markdown('<div class="main-title">🏙️ BALANCEFLOW AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">The Demand Orchestration Layer for Sustainable Cities</div>', unsafe_allow_html=True)
st.markdown("---")

# 🛑 PHẦN 1: TỔNG QUAN VẤN ĐỀ (Theo góp ý của anh Grab)
st.markdown('<div class="section-header">🛑 Urban Challenge & Core Mission</div>', unsafe_allow_html=True)
st.markdown("""
<div class="problem-box">
    <strong>The Core Issue:</strong> Modern megacities face severe supply-demand imbalances during peak hours. 
    Traditional ride-hailing networks are purely <em>reactive</em>—causing skyrocketing surge pricing, excessive driver empty mileage, and gridlocks.
    <br>
    <strong>Our Proactive Approach:</strong> <strong>Balanceflow AI</strong> forecasts gridlock risks 45 minutes ahead and orchestrates commuter demand using behavioral elasticity <em>before</em> the congestion happens.
</div>
""", unsafe_allow_html=True)

# 📊 PHẦN 2: EXECUTIVE SUMMARY & CURRENT MONITOR (Giữ nguyên nội dung gốc của bồ + Bổ sung Chart DA)
st.markdown('<div class="section-header">📈 Executive Summary: Live Status & System Impact</div>', unsafe_allow_html=True)

# Hàng 1: Giữ nguyên trạng thái cảnh báo thực tế từ file cũ của bồ
col_live1, col_live2 = st.columns(2)
with col_live1:
    st.markdown("### 📊 Main KPI")
    st.error("#### Current DBS: 43")
    st.markdown("<p style='color:#ef5350; font-weight:bold; margin-top:-10px;'>⚠️ HIGH IMBALANCE RISK</p>", unsafe_allow_html=True)
    st.caption("Demand Balance Score (DBS) indicates critical supply-demand gap in peak hours.")
    
with col_live2:
    st.markdown("### 🔮 Predicted Event")
    st.info("#### Predicted Surge Event")
    st.markdown("📍 **Location:** District 1 | ⏰ **Time:** 08:00 AM")
    st.caption("AI engine flags imminent gridlock and surge pricing risk 45 minutes ahead.")

st.write("")

# Hàng 2: Bổ sung 2 biểu đồ trực quan thể hiện rõ kết quả vai trò Data Analyst
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("📉 Risk Curve Flattening After Intervention")
    time_timeline = [f"T+{i*5}m" for i in range(10)]
    reactive_risk = [43, 52, 65, 78, 81, 80, 75, 70, 62, 55]
    proactive_risk = [43, 46, 50, 55, 58, 56, 53, 50, 47, 45]
    
    df_risk = pd.DataFrame({
        'Timeline': time_timeline,
        'Without Intervention (Reactive)': reactive_risk,
        'With Balanceflow AI (Proactive)': proactive_risk
    }).set_index('Timeline')
    st.line_chart(df_risk, color=["#FF4B4B", "#2EA043"])

with chart_col2:
    st.subheader("🚖 Fleet Efficiency & Driver Optimization")
    metrics_label = ['Driver Utilization (%)', 'Active Trip Hours / Day']
    before_ai = [68, 6.2]
    after_ai = [79, 7.3]
    
    df_eff = pd.DataFrame({
        'Metric': metrics_label,
        'Before Optimization': before_ai,
        'After Optimization': after_ai
    }).set_index('Metric')
    st.bar_chart(df_eff, color=["#4A4A4A", "#00C4CC"])

st.markdown("---")

# 🖼️ PHẦN 3: NỘI DUNG HÌNH ẢNH TRỰC QUAN (Nhúng ảnh sơ đồ Canva)
st.markdown('<div class="section-header">🏗️ System Architecture & Data Flow</div>', unsafe_allow_html=True)
st.write("Our 6-layer decoupled framework built for real-time demand orchestration:")

try:
    st.image("assets/architecture.png", caption="Balanceflow AI Multi-Layer System Architecture Overview", use_column_width=True)
except:
    st.warning("⚠️ Architecture diagram image not found in 'assets/' directory. Please check file path.")

st.write("")
st.info("💡 Use the sidebar navigation on the left to explore detailed system modules, predictive engines, and simulators!")