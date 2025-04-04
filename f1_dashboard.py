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

#Pit stop impact calculator

st.subheader("🔧 Pit Stop Impact Calculator")

# Input pit stop details
pit_stops = st.number_input("Enter number of pit stops", min_value=0, value=1, step=1)
pit_duration = st.number_input("Average time per pit stop (in minutes)", min_value=0.0, value=0.3, step=0.1)

# Calculate impact
total_pit_time = pit_stops * pit_duration
adjusted_lap_time = result + total_pit_time if 'result' in locals() and isinstance(result, (int, float)) else None

if adjusted_lap_time:
    st.write(f"⏱️ Additional Pit Time: **{round(total_pit_time, 2)} minutes**")
    st.success(f"🛠️ Adjusted Lap Time including pit stops: **{round(adjusted_lap_time, 2)} minutes**")

    # Comparison again
    if 'predicted_time' in locals():
        adjusted_vs_ai = round(adjusted_lap_time - predicted_time, 2)
        if adjusted_vs_ai < 0:
            st.success(f"✅ Even with pit stops, you're {abs(adjusted_vs_ai)} min faster than AI prediction!")
        elif adjusted_vs_ai > 0:
            st.warning(f"⚠️ You're now {adjusted_vs_ai} min slower than AI prediction due to pit stops.")
        else:
            st.info("🤖 Your adjusted lap equals AI’s prediction even with pit stops!")

from fpdf import FPDF
import datetime

def generate_pdf(track, distance, speed, lap_time, real_time, predicted, pit_stops, pit_time, adjusted):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="🏁 F1 Fastest Lap Summary Report", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Date: {datetime.date.today()}", ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Track Selected: {track}", ln=True)
    pdf.cell(200, 10, txt=f"Track Distance: {distance} km", ln=True)
    pdf.cell(200, 10, txt=f"Input Speed: {speed} km/h", ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Calculated Lap Time: {round(lap_time, 2)} min", ln=True)
    pdf.cell(200, 10, txt=f"Real Fastest Lap Time: {real_time} min", ln=True)
    pdf.cell(200, 10, txt=f"AI-Predicted Lap Time: {round(predicted, 2)} min", ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Pit Stops: {pit_stops}", ln=True)
    pdf.cell(200, 10, txt=f"Pit Stop Duration (each): {pit_time} min", ln=True)
    pdf.cell(200, 10, txt=f"Adjusted Lap Time: {round(adjusted, 2)} min", ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, txt="Thanks for using the F1 Lap Time Dashboard! 🏎️", ln=True)

    filename = f"lap_summary_{track.lower()}_{datetime.date.today()}.pdf"
    pdf.output(filename)
    return filename

if st.button("📥 Download Lap Summary as PDF"):
    if 'result' in locals() and 'predicted_time' in locals() and 'adjusted_lap_time' in locals():
        pdf_file = generate_pdf(
            selected_track,
            track_distances[selected_track],
            speed,
            result,
            f1_fastest_laps[selected_track],
            predicted_time,
            pit_stops,
            pit_duration,
            adjusted_lap_time
        )
        with open(pdf_file, "rb") as file:
            st.download_button(
                label="📄 Click here to download your summary",
                data=file,
                file_name=pdf_file,
                mime="application/pdf"
            )
    else:
        st.error("❗Please calculate lap time before downloading the summary.")
