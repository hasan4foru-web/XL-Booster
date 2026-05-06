import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="XLBooster Pro", layout="wide")
st.title("🚀 XLBooster: Advanced Analytics")

file_input = st.sidebar.file_uploader("Excel file upload karein", type=["xlsx"])

if file_input is not None:
    df = pd.read_excel(file_input)
    st.sidebar.success("Data Loaded!")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Records", len(df))
    
    if 'Salary' in df.columns:
        col2.metric("Total Salary", f"₹{df['Salary'].sum():,.0f}")
        col3.metric("Avg Salary", f"₹{df['Salary'].mean():,.0f}")

    st.markdown("---")
    c1, c2 = st.columns(2)
    
    with c1:
        if 'Department' in df.columns:
            st.subheader("🏢 Dept Distribution")
            fig1 = px.pie(df, names='Department', hole=0.4)
            st.plotly_chart(fig1, use_container_width=True)

    with c2:
        if 'Department' in df.columns and 'Salary' in df.columns:
            st.subheader("💰 Salary by Dept")
            fig2 = px.bar(df, x='Department', y='Salary', color='Department')
            st.plotly_chart(fig2, use_container_width=True)

    st.subheader("📄 Raw Data Explorer")
    st.dataframe(df, use_container_width=True)

else:
    st.info("👈 Sidebar se Excel file select karein.")