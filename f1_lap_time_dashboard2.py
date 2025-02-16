import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# Load F1 background image
bg_image = Image.open('f1_image1.jpeg')

# Set Background Image in the Header
st.image(bg_image, use_column_width=True)
st.markdown("<h1 style='text-align: center; color: red;'>Math Behind F1 Racing: The Fastest Lap</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Explore how speed, acceleration, and braking impact lap times!</p>", unsafe_allow_html=True)

# Sidebar for User Inputs
st.sidebar.header("Adjust Parameters:")
track_length = st.sidebar.slider("Track Length (meters)", 3000, 7000, 5000)
avg_speed_kmh = st.sidebar.slider("Average Speed (km/h)", 150, 350, 250)
acceleration = st.sidebar.slider("Acceleration (m/s²)", 2.0, 6.0, 4.0)
braking = st.sidebar.slider("Braking (m/s²)", 4.0, 8.0, 6.0)

# Convert km/h to m/s
avg_speed_ms = avg_speed_kmh * (1000 / 3600)

# Time to reach max speed
t_accel = avg_speed_ms / acceleration  
s_accel = 0.5 * acceleration * t_accel**2  

# Braking distance (before a turn)
s_braking = (avg_speed_ms**2) / (2 * braking)  

# Remaining track distance for steady speed
s_constant = track_length - (s_accel + s_braking)  
t_constant = s_constant / avg_speed_ms  

# Time for braking phase
t_braking = avg_speed_ms / braking  

# Total Lap Time
lap_time = t_accel + t_constant + t_braking

# Display Results with Styling
st.markdown("<h2 style='color: red;'>Estimated Lap Time:</h2>", unsafe_allow_html=True)
st.markdown(f"<h1 style='color: black;'>{lap_time:.2f} seconds</h1>", unsafe_allow_html=True)

# Visualization Data
time_points = [0, t_accel, t_accel + t_constant, lap_time]
speed_points = [0, avg_speed_ms, avg_speed_ms, 0]
distance_points = [0, s_accel, s_accel + s_constant, track_length]

# Speed vs. Time Plot
fig1, ax1 = plt.subplots()
ax1.plot(time_points, speed_points, label='Speed (m/s)', color='red', marker='o')
ax1.set_title('Speed vs. Time')
ax1.set_xlabel('Time (seconds)')
ax1.set_ylabel('Speed (m/s)')
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend()
st.pyplot(fig1)

# Distance vs. Time Plot
fig2, ax2 = plt.subplots()
ax2.plot(time_points, distance_points, label='Distance (m)', color='blue', marker='o')
ax2.set_title('Distance vs. Time')
ax2.set_xlabel('Time (seconds)')
ax2.set_ylabel('Distance (m)')
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend()
st.pyplot(fig2)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>🏎️ Adjust the sliders and see how lap times change in real-time!</p>", unsafe_allow_html=True)
