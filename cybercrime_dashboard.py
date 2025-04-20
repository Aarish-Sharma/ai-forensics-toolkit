import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("payload_timeline.csv", parse_dates=['Timestamp'])
df['Hour'] = df['Timestamp'].dt.hour

# Page setup
st.set_page_config(page_title="Cybercrime Payload Detection", layout="wide")
st.title("🔍 Cybercrime Payload Detection Dashboard")

# Metrics
total_payloads = len(df)
unique_payloads = df['Payload_Type'].nunique()
high_severity = len(df[df['Severity'] == 'High'])
missed = len(df[df['Status'] == 'Missed'])

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Payloads", total_payloads)
col2.metric("Unique Payload Types", unique_payloads)
col3.metric("High Severity Threats", high_severity)
col4.metric("Missed Payloads", missed)

st.markdown("---")

# Payload distribution
st.subheader("📊 Payload Type Distribution")
fig1, ax1 = plt.subplots()
df['Payload_Type'].value_counts().plot(kind='bar', color='crimson', ax=ax1)
ax1.set_ylabel("Count")
ax1.set_xlabel("Payload Type")
ax1.set_title("Payload Frequency by Type")
st.pyplot(fig1)

# Severity breakdown
st.subheader("🛡️ Detection Results by Severity")
grouped = df.groupby(['Severity', 'Status']).size().unstack().fillna(0)
st.bar_chart(grouped)

# Timeline analysis
st.subheader("🕒 Payload Activity Timeline")
hourly = df.groupby('Hour')['Payload_Type'].count()
fig2, ax2 = plt.subplots()
hourly.plot(kind='line', marker='o', color='teal', ax=ax2)
ax2.set_ylabel("Payload Count")
ax2.set_xlabel("Hour of Day")
ax2.set_title("Payload Detection Over Time")
st.pyplot(fig2)

# Critical Incidents Table
st.subheader("🚨 High Severity Threats NOT Blocked")
critical = df[(df['Severity'] == 'High') & (df['Status'] != 'Blocked')]
st.dataframe(critical[['Timestamp', 'Source_IP', 'Payload_Type', 'Severity', 'Status']])
