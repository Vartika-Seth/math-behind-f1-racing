import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image

# Custom CSS for Full Background Image and Transparent Containers
st.markdown("""
    <style>
    body {
        background-image: url('f1_image3.jpg');
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
**Adjust the inputs** below to see how it impacts lap times!
""")

# Sidebar for User Inputs
st.sidebar.header("Adjust Parameters:")
# Track Selection with Preset Lengths
track_options = {
    "Monaco": 3337,
    "Silverstone": 5891,
    "Monza": 5793,
    "Spa-Francorchamps": 7004,
    "Yas Marina": 5581
}
selected_track = st.sidebar.selectbox("Choose Track:", list(track_options.keys()))
track_length = track_options[selected_track]
st.sidebar.write(f"Track Length: {track_length} meters")
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
st.markdown("<h2 style='color: #FF5757;'>Estimated Lap Time:</h2>", unsafe_allow_html=True)
st.markdown(f"<h1 style='color: #FFF700;'>{lap_time:.2f} seconds</h1>", unsafe_allow_html=True)

# Visualization Data
time_points = [0, t_accel, t_accel + t_constant, lap_time]
speed_points = [0, avg_speed_ms, avg_speed_ms, 0]
distance_points = [0, s_accel, s_accel + s_constant, track_length]

# Speed vs. Time Plot
fig1, ax1 = plt.subplots()
ax1.plot(time_points, speed_points, label='Speed (m/s)', color='#FF5757', marker='o')
ax1.set_title('Speed vs. Time', color='white')
ax1.set_xlabel('Time (seconds)', color='white')
ax1.set_ylabel('Speed (m/s)', color='white')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.legend()
ax1.tick_params(colors='white')
fig1.patch.set_alpha(0)
ax1.set_facecolor('black')
st.pyplot(fig1)

# Distance vs. Time Plot
fig2, ax2 = plt.subplots()
ax2.plot(time_points, distance_points, label='Distance (m)', color='#FFF700', marker='o')
ax2.set_title('Distance vs. Time', color='white')
ax2.set_xlabel('Time (seconds)', color='white')
ax2.set_ylabel('Distance (m)', color='white')
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.legend()
ax2.tick_params(colors='white')
fig2.patch.set_alpha(0)
ax2.set_facecolor('black')
st.pyplot(fig2)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #FFF700;'>🏎️ Adjust the sliders and see how lap times change in real-time!</p>", unsafe_allow_html=True)
