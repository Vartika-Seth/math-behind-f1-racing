import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Simple Lap Time Calculator
def calculate_fastest_lap(distance, speed):
    if speed == 0:
        return "Invalid speed!"
    lap_time = distance / speed  # Time = Distance / Speed
    return round(lap_time, 2)

# Track Layouts
track_layouts = {
    "Monza": "monza.png",
    "Silverstone": "Silverstone.png",
    "Spa": "Spa.png",
    "Suzuka": "Suzuka.png"
}

# Streamlit Page Settings
st.set_page_config(page_title="F1 Fastest Lap Calculator", layout="wide")

# Sidebar
st.sidebar.title("🏎️ Select F1 Track")
selected_track = st.sidebar.radio("Choose a Track:", list(track_layouts.keys()))

# Title and Image
st.title("🏁 F1 Fastest Lap Calculator")
st.image(track_layouts[selected_track], caption=f"{selected_track} Track Layout", use_container_width=True)

# Inputs
st.subheader("🔢 Enter Lap Details")
distance = st.number_input("Enter Track Distance (in km)", min_value=0.1, value=5.0, step=0.1)
speed = st.number_input("Enter Average Speed (in km/h)", min_value=1, value=200, step=1)

# Lap Time Calculation
if st.button("🚀 Calculate Fastest Lap"):
    result = calculate_fastest_lap(distance, speed)
    st.success(f"🏁 Fastest Lap Time: {result} minutes")

# Fake Animation: Lap Simulation
st.subheader("🏎️ Lap Simulation")

fig, ax = plt.subplots()
circle = plt.Circle((0, 0), 1, color='gray', fill=False)
ax.add_patch(circle)
car_dot, = ax.plot([], [], 'ro', markersize=10)
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.axis('off')

# Display dot moving
for angle in np.linspace(0, 2 * np.pi, 20):
    x = np.cos(angle)
    y = np.sin(angle)
    car_dot.set_data(x, y)
    st.pyplot(fig)
    time.sleep(0.1)
