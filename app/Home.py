import streamlit as st
import pandas as pd
import plotly.express as px

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

# 🛑 PHẦN 1: TỔNG QUAN VẤN ĐỀ
st.markdown('<div class="section-header">🛑 Urban Challenge & Core Mission</div>', unsafe_allow_html=True)
st.markdown("""
<div class="problem-box">
    <strong>The Core Issue:</strong> Modern megacities face severe supply-demand imbalances during peak hours. 
    Traditional ride-hailing networks are purely <em>reactive</em>—causing skyrocketing surge pricing, excessive driver empty mileage, and gridlocks.
    <br>
    <strong>Our Proactive Approach:</strong> <strong>Balanceflow AI</strong> forecasts gridlock risks 45 minutes ahead and orchestrates commuter demand using behavioral elasticity <em>before</em> the congestion happens.
</div>
""", unsafe_allow_html=True)

# 📊 PHẦN 2: EXECUTIVE SUMMARY & CURRENT MONITOR
st.markdown('<div class="section-header">📈 Executive Summary: Live Status & System Impact</div>', unsafe_allow_html=True)

# Hàng 1: Trạng thái cảnh báo thực tế nguyên bản của dự án
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

# Hàng 2: Khu vực chứa 2 biểu đồ Plotly cao cấp
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
    })
    
    fig_risk = px.line(
        df_risk, 
        x='Timeline', 
        y=['Without Intervention (Reactive)', 'With Balanceflow AI (Proactive)'],
        color_discrete_sequence=["#FF4B4B", "#2EA043"]
    )
    fig_risk.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
        margin=dict(l=20, r=20, t=10, b=50),
        xaxis_title=None,
        yaxis_title="Risk Index (%)"
    )
    st.plotly_chart(fig_risk, use_container_width=True)

with chart_col2:
    st.subheader("🚖 Fleet Efficiency Optimization (Impact)")

    df_eff = pd.DataFrame({
        "Metric": [
            "Active Trip Hours / Day",
            "Active Trip Hours / Day",
            "Driver Utilization (%)",
            "Driver Utilization (%)"
        ],
        "Status": [
            "After Optimization",
            "Before Optimization",
            "After Optimization",
            "Before Optimization"
        ],
        "Value": [
            7.3,
            6.2,
            79,
            68
        ]
    })

    fig_eff = px.bar(
        df_eff,
        y="Metric",
        x="Value",
        color="Status",
        orientation="h",
        barmode="group",
        color_discrete_map={
            "Before Optimization": "#4A4A4A",
            "After Optimization": "#00C4CC"
        },
        category_orders={
            "Status": [
                "After Optimization",
                "Before Optimization"
            ],
            "Metric": [
                "Driver Utilization (%)",
                "Active Trip Hours / Day"
            ]
        }
    )

    fig_eff.update_layout(
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=-0.30,
            xanchor="center",
            x=0.5
        ),
        margin=dict(
            l=20,
            r=20,
            t=10,
            b=50
        ),
        xaxis_title="Performance Metric Value",
        yaxis_title=None,
        bargap=0.55,
        legend_title_text=""
    )

    fig_eff.update_traces(
        width=0.16
    )

    st.plotly_chart(
        fig_eff,
        use_container_width=True
    )

st.markdown("---")

# 🖼️ PHẦN 3: NỘI DUNG HÌNH ẢNH TRỰC QUAN (Căn giữa và thu nhỏ ảnh Canva vừa vặn)
st.markdown('<div class="section-header">🏗️ System Architecture & Data Flow</div>', unsafe_allow_html=True)
st.write("Our 6-layer decoupled framework built for real-time demand orchestration:")

img_pad1, img_core, img_pad2 = st.columns([1, 3, 1])

with img_core:
    try:
        # Giữ width=450 giúp sơ đồ gọn gàng, sắc nét
        st.image("assets/architecture.png", caption="Balanceflow AI Multi-Layer System Architecture Overview", width=450)
    except:
        st.warning("⚠️ Architecture diagram image not found in 'assets/' directory. Please check file path.")

st.write("")
st.info("💡 Use the sidebar navigation on the left to explore detailed system modules, predictive engines, and simulators!")