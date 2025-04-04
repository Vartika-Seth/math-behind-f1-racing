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


# --- Step 3: Lap Time Comparison with Real F1 Records ---

st.subheader("📊 Compare with Real F1 Fastest Lap")

# Real lap records (in minutes for simplicity)
f1_fastest_laps = {
    "Monza": 1.21,         # 1:21 = 81 seconds = 1.35 minutes
    "Silverstone": 1.27,   # ~1:27 = 87 sec
    "Spa": 1.46,           # ~1:46 = 106 sec
    "Suzuka": 1.30         # ~1:30 = 90 sec
}
if selected_track in f1_fastest_laps and speed > 0:
    real_time = f1_fastest_laps[selected_track]
    st.write(f"🏎️ Fastest Real Lap Time at {selected_track}: **{real_time} minutes**")

    if 'result' in locals() and isinstance(result, (int, float)):
        diff = round(result - real_time, 2)
        if diff < 0:
            st.success(f"🔥 Your lap is **{abs(diff)} minutes faster** than the real F1 record! Unbelievable! 😲")
        elif diff == 0:
            st.info("🎯 Your lap exactly matches the real F1 lap time! Wow!")
        else:
            st.warning(f"⏱️ Your lap is **{diff} minutes slower** than the real F1 record. Try increasing your speed!")


#AI-Based Lap Time Prediction (Simple Linear Regression Model)

from sklearn.linear_model import LinearRegression
import pandas as pd

st.subheader("🤖 AI-Based Lap Time Prediction")

# Simulated past data (Speed in km/h, Lap Time in minutes)
sample_data = {
    "Monza": [(180, 1.5), (200, 1.3), (220, 1.2), (240, 1.1)],
    "Silverstone": [(180, 1.6), (200, 1.4), (220, 1.3), (240, 1.2)],
    "Spa": [(180, 1.8), (200, 1.6), (220, 1.5), (240, 1.4)],
    "Suzuka": [(180, 1.7), (200, 1.5), (220, 1.4), (240, 1.3)],
}

# Get data for selected track
data = sample_data[selected_track]
df = pd.DataFrame(data, columns=["Speed", "LapTime"])

# Train simple linear regression model
model = LinearRegression()
model.fit(df[["Speed"]], df["LapTime"])

# Predict lap time from user speed
predicted_time = model.predict([[speed]])[0]
st.write(f"🧠 Predicted Lap Time (AI Model): **{round(predicted_time, 2)} minutes**")

# Comparison with user lap
if 'result' in locals() and isinstance(result, (int, float)):
    ai_diff = round(result - predicted_time, 2)
    if ai_diff < 0:
        st.success(f"🚀 You're faster than AI's prediction by {abs(ai_diff)} minutes!")
    elif ai_diff > 0:
        st.warning(f"📉 You're {ai_diff} minutes slower than AI's prediction. Try increasing speed!")
    else:
        st.info("🤝 Your time exactly matches the AI prediction!")


