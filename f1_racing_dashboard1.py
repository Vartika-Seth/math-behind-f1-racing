import streamlit as st

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
st.set_page_config(page_title="F1 Fastest Lap Calculator", layout="wide")  # Wide Layout

# Custom CSS for Styling
st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: white;
            font-family: Arial, sans-serif;
        }
        .stButton > button {
            background-color: red;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 18px;
        }
        .stNumberInput > label {
            font-size: 16px;
            font-weight: bold;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

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
