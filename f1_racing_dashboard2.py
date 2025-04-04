import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ----- Lap Time Calculator -----
def calculate_fastest_lap(distance, speed):
    if speed == 0:
        return "Invalid speed!"
    lap_time = distance / speed
    return round(lap_time, 2)

# ----- Track Layouts -----
track_layouts = {
    "Monza": "monza.png",
    "Silverstone": "Silverstone.png",
    "Spa": "Spa.png",
    "Suzuka": "Suzuka.png"
}

# ----- Streamlit UI Setup -----
st.set_page_config(page_title="F1 Fastest Lap Calculator", layout="wide")

# Sidebar
st.sidebar.title("🏎️ Select F1 Track")
selected_track = st.sidebar.radio("Choose a Track:", list(track_layouts.keys()))

# Title
st.title("🏁 F1 Fastest Lap Calculator")
st.image(track_layouts[selected_track], caption=f"{selected_track} Track Layout", use_container_width=True)

# Inputs
st.subheader("🔢 Enter Lap Details")
distance = st.number_input("Enter Track Distance (in km)", min_value=0.1, value=5.0, step=0.1)
speed = st.number_input("Enter Average Speed (in km/h)", min_value=1, value=200, step=1)

# Calculate
if st.button("🚀 Calculate Fastest Lap"):
    result = calculate_fastest_lap(distance, speed)
    st.success(f"🏁 Fastest Lap Time: {result} minutes")

    # ----- Show Static Lap Simulation -----
    st.subheader("🏎️ Lap Simulation Snapshot")

    # Compute one point on the circular track
    progress_ratio = min(result / 2, 1)  # Simulate car's position based on lap time
    angle = 2 * np.pi * progress_ratio
    x = np.cos(angle)
    y = np.sin(angle)

    # Plot
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    track_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linewidth=2)
    ax.add_patch(track_circle)
    ax.plot(x, y, 'ro', markersize=10)  # Red dot = car position
    ax.set_aspect('equal')
    ax.axis('off')
    st.pyplot(fig)
