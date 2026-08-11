import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Weather Analysis",
    page_icon="🌦️",
    layout="wide"
)

st.title("🌦️ Weather Analysis Dashboard")
st.write("Explore historical weather data and visualize important weather patterns.")

# Load dataset
df = pd.read_csv("weatherHistory.csv")

# Dataset preview
st.header("📊 Weather Dataset")

st.write("Number of rows:", df.shape[0])
st.write("Number of columns:", df.shape[1])

st.dataframe(df.head(10))

# Statistics
st.header("📈 Statistical Summary")
st.dataframe(df.describe())

# Column selection
numeric_columns = df.select_dtypes(include="number").columns.tolist()

if numeric_columns:
    column = st.selectbox(
        "Select a numerical column",
        numeric_columns
    )

    st.subheader(f"{column} Distribution")

    fig, ax = plt.subplots()
    ax.hist(df[column].dropna(), bins=30)
    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")
    ax.set_title(f"{column} Distribution")

    st.pyplot(fig)

# Correlation
st.header("🔗 Correlation Analysis")

if len(numeric_columns) >= 2:
    correlation = df[numeric_columns].corr()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.imshow(correlation, aspect="auto")

    ax.set_xticks(range(len(numeric_columns)))
    ax.set_yticks(range(len(numeric_columns)))

    ax.set_xticklabels(numeric_columns, rotation=90)
    ax.set_yticklabels(numeric_columns)

    ax.set_title("Correlation Matrix")

    st.pyplot(fig)

st.success("Weather analysis completed successfully! 🌤️")