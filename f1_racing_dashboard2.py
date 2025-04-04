import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Simple Lap Time Calculator
def calculate_fastest_lap(distance, speed):
    if speed == 0:
        return "Invalid speed!"
    lap_time = distance / speed  # Time = Distance / Speed
    return round(lap_time, 2)  # Rounded to 2 decimal places

# Available Track Layouts (Images must be in the same folder as this script)
track_layouts = {
    "Monza": "monza.png",
    "Silverstone": "Silverstone.png",
    "Spa": "Spa.png",
    "Suzuka": "Suzuka.png"
}

# ---- Streamlit UI ----
st.set_page_config(page_title="F1 Fastest Lap Calculator", layout="wide")

# Sidebar - Track Selection
st.sidebar.title("🏎️ Select F1 Track")
selected_track = st.sidebar.radio("Choose a Track:", list(track_layouts.keys()))

# Main Title
st.title("🏁 F1 Fastest Lap Calculator")

# Display Track Image
st.image(track_layouts[selected_track], caption=f"{selected_track} Track Layout", use_container_width=True)

# User Inputs for Lap Calculation
st.subheader("🔢 Enter Lap Details")
distance = st.number_input("Enter Track Distance (in km)", min_value=0.1, value=5.0, step=0.1)
speed = st.number_input("Enter Average Speed (in km/h)", min_value=1, value=200, step=1)

# Calculate & Display Lap Time
if st.button("🚀 Calculate Fastest Lap"):
    result = calculate_fastest_lap(distance, speed)
    st.success(f"🏁 Fastest Lap Time: {result} minutes")

# ---- Lap Animation ----
st.subheader("🏎️ Lap Simulation")

# Create a simulated circular track
fig, ax = plt.subplots(figsize=(4, 4))
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
track_circle = plt.Circle((0, 0), 1, color='gray', fill=False, linewidth=2)
ax.add_patch(track_circle)
car_dot, = ax.plot([], [], 'ro', markersize=8)  # Moving car (red dot)

# Function to update dot position in animation
def update(frame):
    angle = 2 * np.pi * frame / 100  # Convert frame index to angle
    x = np.cos(angle)  # X-coordinate on circle
    y = np.sin(angle)  # Y-coordinate on circle
    car_dot.set_data(x, y)
    return car_dot,

# Create animation (100 frames, loops continuously)
lap_animation = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Show animation in Streamlit
st.pyplot(fig)
