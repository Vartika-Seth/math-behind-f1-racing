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
track = st.sidebar.selectbox(
    "Select Track", 
    ["Monza", "Silverstone", "Spa", "Suzuka"], 
    key="track_selection"  # Unique key to avoid duplication
)
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

st.subheader("🚗 Animated Lap Simulation ")
st.write("🏎️ Lap animation will be displayed")

st.subheader("🛠️ Pit Stop Impact Calculator ")
st.write("⏱️ Graph showing time lost/gained due to pit stops.")

# --- Function to Predict Lap Time ---
def predict_lap_time(fuel_load, tire_wear, weather, track):
    base_time = {"Monza": 80.0, "Silverstone": 90.0, "Spa": 100.0, "Suzuka": 95.0}
    lap_time = base_time[track] + (fuel_load * 0.1) + (tire_wear * 0.2)

    # Weather impact
    if weather == "Wet":
        lap_time += 5
    elif weather == "Cloudy":
        lap_time += 2
    
    return round(lap_time, 2)

# --- Dashboard UI ---
st.title("🏎️ F1 Racing Dashboard – Fastest Lap Calculator")

# Sidebar Inputs
st.sidebar.header("🔧 Simulation Settings")track = st.sidebar.selectbox(
    "Select Track", 
    ["Monza", "Silverstone", "Spa", "Suzuka"], 
    key="track_selection"  # Unique key to avoid duplication
)
fuel_load = st.sidebar.slider("Fuel Load (kg)", min_value=10, max_value=110, step=5, value=50)
tire_wear = st.sidebar.slider("Tire Wear (%)", min_value=0, max_value=100, step=5, value=20)
weather = st.sidebar.selectbox("Weather Conditions", ["Sunny", "Cloudy", "Wet"])

# Placeholder for Lap Time Prediction
lap_time_placeholder = st.empty()


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

import time

# --- Function to Simulate a Lap ---
def animate_lap(predicted_time):
    st.subheader("🏎️ Lap Simulation")

  # Simplified Track Coordinates (X, Y) for Visualization
track_layouts = {
    "Monza": {
        "x": [0, 1, 2, 2, 1, 0, -1, -2, -2, -1, 0],
        "y": [0, 1, 1.5, 2, 2.5, 3, 2.5, 2, 1.5, 1, 0]
    },
    "Silverstone": {
        "x": [0, 1, 1.5, 2, 1.8, 1.3, 0.8, 0.5, -0.5, -1, -1.5, -2, -1.5, -1, 0],
        "y": [0, 1, 1.2, 1.5, 1.8, 2, 2.2, 2.4, 2.5, 2.3, 2, 1.5, 1, 0.5, 0]
    },
    "Spa": {
        "x": [0, 1, 1.2, 1.5, 1.3, 1, 0.5, 0, -0.5, -1, -1.2, -1.5, -1.3, -1, 0],
        "y": [0, 1, 1.3, 1.7, 2, 2.3, 2.5, 2.6, 2.5, 2.3, 2, 1.7, 1.3, 1, 0]
    },
    "Suzuka": {
        "x": [0, 1, 2, 2.5, 2, 1.5, 1, 0.5, -0.5, -1, -1.5, -2, -2.5, -2, -1, 0],
        "y": [0, 0.5, 1, 1.5, 2, 2.2, 2.4, 2.6, 2.6, 2.4, 2.2, 2, 1.5, 1, 0.5, 0]
    }
}
import numpy as np
import matplotlib.pyplot as plt
import time
import streamlit as st

# --- Function to Animate a Lap on Real Track Layout ---
def animate_lap(predicted_time, track):
    st.subheader(f"🏎️ Lap Simulation on {track}")

    track_data = track_layouts[track]
    x = np.array(track_data["x"])
    y = np.array(track_data["y"])

    fig, ax = plt.subplots()
    ax.plot(x, y, 'gray', linewidth=2)  # Track outline
    car_dot, = ax.plot([], [], 'ro', markersize=8)  # Red dot = F1 Car

    ax.set_xlim(min(x) - 1, max(x) + 1)
    ax.set_ylim(min(y) - 1, max(y) + 1)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Lap Simulation - {track}")

    # Show animation frame by frame
    frame_time = predicted_time / len(x)  # Adjust speed based on lap time
    for i in range(len(x)):
        car_dot.set_data(x[i], y[i])
        ax.figure.canvas.draw()
        time.sleep(frame_time / 10)  # Adjust animation speed
        st.pyplot(fig)


    # Show animation frame by frame
    frame_time = predicted_time / len(theta)  # Adjust speed based on lap time
    for i in range(len(theta)):
        car_dot.set_data(x[i], y[i])
        ax.figure.canvas.draw()
        time.sleep(frame_time / 10)  # Reduce time for Streamlit compatibility
        st.pyplot(fig)

# --- Predict Lap Time When Button is Clicked ---
if st.sidebar.button("Simulate Lap"):
    predicted_time = predict_lap_time(fuel_load, tire_wear, weather, track)
    lap_time_placeholder.write(f"🏁 **Predicted Lap Time:** {predicted_time} seconds")

    # Run the new track animation
    animate_lap(predicted_time, track)

# Title and Description
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

