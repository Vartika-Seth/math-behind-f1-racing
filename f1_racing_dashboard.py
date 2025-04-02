import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import matplotlib.animation as animation
import tempfile

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="F1 Racing Dashboard", layout="wide")

# --- CUSTOM STYLE ---
st.markdown("""
    <style>
        .main {
            background-color: #1E1E1E;
            color: white;
        }
        .sidebar .sidebar-content {
            background-color: #121212;
            color: white;
        }
        h1 {
            color: #E10600;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)

# --- DASHBOARD TITLE ---
st.title("🏎️ F1 Racing Dashboard – Fastest Lap Calculator")

# --- SIDEBAR: USER INPUTS ---
st.sidebar.header("🔧 Simulation Settings")
track = st.sidebar.selectbox("Select Track", ["Monza", "Silverstone", "Spa", "Suzuka"])
fuel_load = st.sidebar.slider("Fuel Load (kg)", min_value=10, max_value=110, step=5, value=50)
tire_wear = st.sidebar.slider("Tire Wear (%)", min_value=0, max_value=100, step=5, value=20)
weather = st.sidebar.selectbox("Weather Conditions", ["Sunny", "Cloudy", "Wet"])

# --- MAIN DASHBOARD SECTIONS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏁 Predicted Fastest Lap Time")
    lap_time_placeholder = st.empty()  # Placeholder for AI-predicted lap time (to be implemented)
    st.write("⏳ AI model will generate the lap time based on selected parameters.")

with col2:
    st.subheader("📊 Lap Time Comparison")
    st.write("🔹 Table comparing predicted lap time with real F1 records.")  # To be implemented

st.subheader("🚗 Animated Lap Simulation (Coming Soon)")
st.write("🏎️ Lap animation will be displayed here.")

st.subheader("🛠️ Pit Stop Impact Calculator (Coming Soon)")
st.write("⏱️ Graph showing time lost/gained due to pit stops.")

# --- RUN THE APP ---
# Save this file as `f1_dashboard.py` and run:
# streamlit run f1_dashboard.py

# Custom CSS for Full Background Image and Transparent Containers
st.markdown("""
    <style>
    body {
        background-image: url('f1_image2.jpg');
        background-size: cover;
        background-attachment: fixed;
    }
    .stApp {
        background: transparent;
    }
    .reportview-container .main .block-container{
        background: rgba(0, 0, 0, 0.6);
        padding: 20px;
        border-radius: 10px;
    }
    h1, h2, h3, h4, h5, h6, p, label {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Description
st.title("Math Behind F1 Racing: The Fastest Lap")
st.markdown("""
This interactive dashboard calculates the **fastest lap time** using mathematical models.  
**Choose a track and adjust parameters below!**
""")

# **Track Selection**
track_options = {
    "Monza (Italy)": {"length": 5793, "avg_speed": 260, "shape": "oval"},
    "Monaco (Monte Carlo)": {"length": 3337, "avg_speed": 160, "shape": "zigzag"},
    "Dubai (Yas Marina)": {"length": 5281, "avg_speed": 210, "shape": "circuit"},
    "Singapore (Marina Bay)": {"length": 5063, "avg_speed": 180, "shape": "complex"},
}

selected_track = st.sidebar.selectbox("Select an F1 Track", list(track_options.keys()))
track_length = track_options[selected_track]["length"]
avg_speed_kmh = track_options[selected_track]["avg_speed"]
track_shape = track_options[selected_track]["shape"]

# Sidebar for Custom Adjustments
st.sidebar.header("Adjust Parameters:")
custom_track_length = st.sidebar.slider("Track Length (meters)", 3000, 7000, track_length)
custom_avg_speed = st.sidebar.slider("Average Speed (km/h)", 150, 350, avg_speed_kmh)
acceleration = st.sidebar.slider("Acceleration (m/s²)", 2.0, 6.0, 4.0)
braking = st.sidebar.slider("Braking (m/s²)", 4.0, 8.0, 6.0)

# Convert km/h to m/s
avg_speed_ms = custom_avg_speed * (1000 / 3600)

# Lap Time Calculation
t_accel = avg_speed_ms / acceleration  
s_accel = 0.5 * acceleration * t_accel**2  
s_braking = (avg_speed_ms**2) / (2 * braking)  
s_constant = custom_track_length - (s_accel + s_braking)  
t_constant = s_constant / avg_speed_ms  
t_braking = avg_speed_ms / braking  
lap_time = t_accel + t_constant + t_braking

# Display Lap Time
st.markdown("<h2 style='color: #FF5757;'>Estimated Lap Time:</h2>", unsafe_allow_html=True)
st.markdown(f"<h1 style='color: #FFF700;'>{lap_time:.2f} seconds</h1>", unsafe_allow_html=True)

# **Animation of Lap Simulation**
num_frames = 100

def generate_track_shape(track_shape):
    if track_shape == "oval":
        theta = np.linspace(0, 2 * np.pi, num_frames)
        x = 100 * np.cos(theta)
        y = 50 * np.sin(theta)
    elif track_shape == "zigzag":
        x = np.linspace(-100, 100, num_frames)
        y = np.sign(np.sin(x / 20)) * 50
    elif track_shape == "circuit":
        theta = np.linspace(0, 2 * np.pi, num_frames)
        x = 80 * np.cos(theta) + np.random.uniform(-10, 10, num_frames)
        y = 80 * np.sin(theta) + np.random.uniform(-10, 10, num_frames)
    elif track_shape == "complex":
        x = np.linspace(-100, 100, num_frames)
        y = np.sin(x / 10) * 50 + np.random.uniform(-10, 10, num_frames)
    return x, y

x_track, y_track = generate_track_shape(track_shape)

def animate(i):
    ax.clear()
    ax.plot(x_track, y_track, 'gray', linewidth=2)
    ax.scatter(x_track[i], y_track[i], color='red', s=100, label="F1 Car")
    ax.set_xlim(-120, 120)
    ax.set_ylim(-120, 120)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"{selected_track} - Lap Simulation", color="white")
    ax.set_facecolor("black")

fig, ax = plt.subplots(figsize=(5, 5))

with tempfile.NamedTemporaryFile(delete=False, suffix=".gif") as tmpfile:
    ani = animation.FuncAnimation(fig, animate, frames=num_frames, interval=100)
    ani.save(tmpfile.name, writer='imagemagick')
    st.image(tmpfile.name)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center; color: #FFF700;'>🏎️ Simulating Lap on {selected_track}!</p>", unsafe_allow_html=True)

