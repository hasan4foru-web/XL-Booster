import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="XLBooster Pro", layout="wide")
st.title("🚀 XLBooster: Advanced Analytics")

uploaded_file = st.sidebar.file_uploader("Excel file upload karein", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.success("File Uploaded!")

    # --- Yahan Metrics (Numbers) hain ---
    st.divider()
    m1, m2 = st.columns(2)
    with m1:
        st.metric("Total Records", len(df))
    
    # Sidebar selections
    all_cols = df.columns.tolist()
    num_cols = df.select_dtypes(include=['number']).columns.tolist()

    st.sidebar.header("Chart Settings")
    cat_select = st.sidebar.selectbox("Category:", all_cols, index=0)

    if num_cols:
        val_select = st.sidebar.selectbox("Value:", num_cols, index=0)
        
        with m2:
            st.metric(f"Total {val_select}", f"{df[val_select].sum():,.2f}")
        
        st.divider()

        # Charts
        c1, c2 = st.columns(2)
        with c1:
            st.plotly_chart(px.pie(df, names=cat_select, values=val_select, hole=0.4), use_container_width=True)
        with c2:
            st.plotly_chart(px.bar(df, x=cat_select, y=val_select, color=cat_select), use_container_width=True)
    else:
        st.error("No numeric columns found!")

    st.divider()
    st.subheader("Raw Data Explorer")
    st.dataframe(df)
else:
    st.info("👈 Sidebar se Excel file select karein.")
