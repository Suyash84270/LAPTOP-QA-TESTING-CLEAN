import streamlit as st
import numpy as np

st.title("💻 Laptop Price Predictor (Demo)")

# Mock dropdown values (no need for DataFrame)
companies = ["Dell", "HP", "Lenovo", "Apple", "Asus"]
types = ["Ultrabook", "Gaming", "Notebook", "Workstation"]
cpus = ["Intel Core i5", "Intel Core i7", "AMD Ryzen 5", "AMD Ryzen 7"]
gpus = ["Intel", "Nvidia", "AMD"]
oses = ["Windows", "Linux", "Mac"]

# Brand
company = st.selectbox('Brand', companies)

# Type of laptop
laptop_type = st.selectbox('Type', types)

# RAM
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# Weight
weight = st.number_input('Weight of the Laptop (in kg)', min_value=0.5, max_value=5.0, step=0.1)

# Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS
ips = st.selectbox('IPS Display', ['No', 'Yes'])

# Screen size
screen_size = st.number_input('Screen Size (in inches)', min_value=10.0, max_value=20.0, step=0.1)

# Resolution
resolution = st.selectbox(
    'Screen Resolution',
    ['1920x1080', '1366x768', '1600x900', '3840x2160',
     '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440']
)

# CPU
cpu = st.selectbox('CPU', cpus)

# HDD
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

# SSD
ssd = st.selectbox('SSD (in GB)', [0, 128, 256, 512, 1024])

# GPU
gpu = st.selectbox('GPU', gpus)

# OS
os = st.selectbox('Operating System', oses)

# Predict Button
if st.button('Predict Price'):
    # Just generate a fake "predicted price"
    fake_price = np.random.randint(25000, 150000)
    st.success(f"💰 The predicted price of this configuration is Rs. {fake_price}")
