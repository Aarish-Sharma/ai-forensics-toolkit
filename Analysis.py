import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time

st.set_page_config(page_title="Cybercrime Forensics Dashboard", layout="wide")
st.title("🧠 Cybercrime Forensics Intelligence")

# File upload
uploaded_file = st.file_uploader("D:\prrr\payload_timeline.csv", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, parse_dates=['Timestamp'])
    df['Hour'] = df['Timestamp'].dt.hour

    st.success("✅ File loaded successfully!")
    
    # Live metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Payloads", len(df))
    col2.metric("High Severity", len(df[df['Severity'] == 'High']))
    col3.metric("Missed Threats", len(df[df['Status'] == 'Missed']))
    col4.metric("Unique Payloads", df['Payload_Type'].nunique())

    st.markdown("----")
    st.subheader("📊 Payload Frequency")
    st.bar_chart(df['Payload_Type'].value_counts())

    st.subheader("🕒 Timeline of Attacks")
    hourly = df.groupby('Hour')['Payload_Type'].count()
    fig, ax = plt.subplots()
    hourly.plot(kind='line', marker='o', ax=ax)
    ax.set_title("Payloads by Hour of Day")
    st.pyplot(fig)

    st.subheader("🚨 High Severity Threats (Not Blocked)")
    st.dataframe(df[(df['Severity'] == 'High') & (df['Status'] != 'Blocked')])

else:
    st.info("Awaiting file upload...")
