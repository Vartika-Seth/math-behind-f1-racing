import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time
import os

# ---------------------------- UI Sidebar - Inputs ----------------------------
st.sidebar.header("🔧 Simulation Settings")

track = st.sidebar.selectbox("Select Track", ["Monza", "Silverstone", "Spa", "Suzuka"], key="track_selection")
fuel_load = st.sidebar.slider("Fuel Load (kg)", min_value=10, max_value=110, step=5, value=50, key="fuel_slider")
tire_wear = st.sidebar.slider("Tire Wear (%)", min_value=0, max_value=100, step=5, value=20, key="tire_slider")
weather = st.sidebar.selectbox("Weather Conditions", ["Sunny", "Cloudy", "Wet"], key="weather_selection")

# Placeholder for displaying lap time
lap_time_placeholder = st.empty()

# ---------------------------- Lap Time Prediction Function ----------------------------
def predict_lap_time(fuel, tire, weather, track):
    """Simple prediction model for lap time based on inputs."""
    base_lap_time = {
        "Monza": 80,  # in seconds
        "Silverstone": 95,
        "Spa": 105,
        "Suzuka": 90
    }
    
    # Adjustments based on fuel, tire wear, and weather
    fuel_penalty = (fuel - 50) * 0.2
    tire_penalty = (tire / 100) * 5
    weather_penalty = {"Sunny": 0, "Cloudy": 1.5, "Wet": 5}[weather]
    
    predicted_time = base_lap_time[track] + fuel_penalty + tire_penalty + weather_penalty
    return round(predicted_time, 2)

# ---------------------------- Track Layouts Data (Local Images) ----------------------------
import os
import streamlit as st

# Define the paths for each track image (saved in the main project folder)
track_layouts = {
    "Monza": "monza.png",
    "Silverstone": "Silverstone.png",
    "Spa": "Spa.png",
    "Suzuka": "Suzuka.png"
}

# Debugging: Print the actual paths
st.write("🔍 Checking track image paths:")
for track, path in track_layouts.items():
    st.write(f"{track} image path:", os.path.abspath(path))
    if not os.path.exists(path):
        st.write(f"❌ ERROR: {track} image not found at {path}")

# Example: Display Monza track to check
st.image(track_layouts["Monza"], caption="Monza Track Layout", use_container_width=True)

# ---------------------------- Animated Lap Simulation ----------------------------
def animate_lap(predicted_time, track):
    """Simulates a lap animation on the selected track."""
    fig, ax = plt.subplots(figsize=(6, 4))
    
    # Load local track image
    track_img = plt.imread(track_layouts[track])

    ax.imshow(track_img, extent=[0, 10, 0, 6])
    car_position_x = np.linspace(0, 10, 50)
    car_position_y = np.sin(np.linspace(0, np.pi, 50)) * 3 + 3

    car, = ax.plot([], [], "ro", markersize=8)  # Red dot as car

    for i in range(len(car_position_x)):
        car.set_data(car_position_x[i], car_position_y[i])
        st.pyplot(fig)
        time.sleep(predicted_time / 100)

# ---------------------------- Button Click Event ----------------------------
if st.sidebar.button("🏁 Simulate Lap"):
    predicted_time = predict_lap_time(fuel_load, tire_wear, weather, track)
    lap_time_placeholder.write(f"🏎️ **Predicted Lap Time:** {predicted_time} seconds")

    # Display selected track layout
    st.image(track_layouts[track], caption=f"{track} Circuit Layout", use_container_width=True)

    # Run Lap Animation
    animate_lap(predicted_time, track)
