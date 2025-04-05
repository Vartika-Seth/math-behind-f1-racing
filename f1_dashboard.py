import streamlit as st
from PIL import Image
from fpdf import FPDF
from sklearn.linear_model import LinearRegression
import pandas as pd

# --- Function to Calculate Lap Time ---
def calculate_fastest_lap(distance, speed):
    if speed == 0:
        return "Invalid speed!"
    lap_time = distance / speed  # Time = Distance / Speed
    return round(lap_time, 2)  # Rounded to 2 decimal places

# --- Function to Generate PDF Summary ---
def generate_lap_summary_pdf(track_name, speed, lap_time):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="F1 Fastest Lap Summary", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Track Selected: {track_name}", ln=True)
    pdf.cell(200, 10, txt=f"Speed Entered: {speed} km/h", ln=True)
    pdf.cell(200, 10, txt=f"Calculated Lap Time: {lap_time} minutes", ln=True)

    output_path = "lap_summary.pdf"
    pdf.output(output_path)
    return output_path

# --- Track Layouts (Ensure images are present in your folder) ---
track_layouts = {
    "Monza": "monza.png",
    "Silverstone": "Silverstone.png",
    "Spa": "Spa.png",
    "Suzuka": "Suzuka.png"
}

# --- Streamlit UI Setup ---
st.set_page_config(page_title="F1 Fastest Lap Calculator", layout="wide")

# --- Custom CSS Styling ---
st.markdown("""
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
    """, unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("🏎️ Select F1 Track")
selected_track = st.sidebar.radio("Choose a Track:", list(track_layouts.keys()))

# --- Main Title ---
st.title("🏁 F1 Fastest Lap Calculator")

# --- Display Track Image ---
st.image(track_layouts[selected_track], caption=f"{selected_track} Track Layout", use_container_width=True)

# --- User Inputs ---
st.subheader("🔢 Enter Lap Details")
distance = st.number_input("Enter Track Distance (in km)", min_value=0.1, value=5.0, step=0.1)
speed = st.number_input("Enter Average Speed (in km/h)", min_value=1, value=200, step=1)

# --- Calculate & Show Lap Time ---
if st.button("🚀 Calculate Fastest Lap"):
    result = calculate_fastest_lap(distance, speed)
    st.success(f"🏁 Fastest Lap Time: {result} minutes")

# --- Real F1 Fastest Laps ---
st.subheader("📊 Compare with Real F1 Fastest Lap")
f1_fastest_laps = {
    "Monza": 1.21,
    "Silverstone": 1.27,
    "Spa": 1.46,
    "Suzuka": 1.30
}
if selected_track in f1_fastest_laps and speed > 0:
    real_time = f1_fastest_laps[selected_track]
    st.write(f"🏎️ Fastest Real Lap Time at {selected_track}: **{real_time} minutes**")

    if 'result' in locals() and isinstance(result, (int, float)):
        diff = round(result - real_time, 2)
        if diff < 0:
            st.success(f"🔥 Your lap is **{abs(diff)} minutes faster** than the real F1 record!")
        elif diff == 0:
            st.info("🎯 Your lap exactly matches the real F1 lap time! Wow!")
        else:
            st.warning(f"⏱️ Your lap is **{diff} minutes slower** than the real F1 record.")

# --- AI-Based Lap Time Prediction ---
st.subheader("🤖 AI-Based Lap Time Prediction")
sample_data = {
    "Monza": [(180, 1.5), (200, 1.3), (220, 1.2), (240, 1.1)],
    "Silverstone": [(180, 1.6), (200, 1.4), (220, 1.3), (240, 1.2)],
    "Spa": [(180, 1.8), (200, 1.6), (220, 1.5), (240, 1.4)],
    "Suzuka": [(180, 1.7), (200, 1.5), (220, 1.4), (240, 1.3)],
}
data = sample_data[selected_track]
df = pd.DataFrame(data, columns=["Speed", "LapTime"])

model = LinearRegression()
model.fit(df[["Speed"]], df["LapTime"])
predicted_time = model.predict([[speed]])[0]
st.write(f"🧠 Predicted Lap Time (AI Model): **{round(predicted_time, 2)} minutes**")

if 'result' in locals() and isinstance(result, (int, float)):
    ai_diff = round(result - predicted_time, 2)
    if ai_diff < 0:
        st.success(f"🚀 You're faster than AI's prediction by {abs(ai_diff)} minutes!")
    elif ai_diff > 0:
        st.warning(f"📉 You're {ai_diff} minutes slower than AI's prediction.")
    else:
        st.info("🤝 Your time matches the AI prediction!")

# --- Pit Stop Impact Calculator ---
st.subheader("🔧 Pit Stop Impact Calculator")
pit_stops = st.number_input("Enter number of pit stops", min_value=0, value=1, step=1)
pit_duration = st.number_input("Average time per pit stop (in minutes)", min_value=0.0, value=0.3, step=0.1)
total_pit_time = pit_stops * pit_duration
adjusted_lap_time = result + total_pit_time if 'result' in locals() and isinstance(result, (int, float)) else None

if adjusted_lap_time:
    st.write(f"⏱️ Additional Pit Time: **{round(total_pit_time, 2)} minutes**")
    st.success(f"🛠️ Adjusted Lap Time including pit stops: **{round(adjusted_lap_time, 2)} minutes**")

    if 'predicted_time' in locals():
        adjusted_vs_ai = round(adjusted_lap_time - predicted_time, 2)
        if adjusted_vs_ai < 0:
            st.success(f"✅ Still {abs(adjusted_vs_ai)} min faster than AI even after pit stops!")
        elif adjusted_vs_ai > 0:
            st.warning(f"⚠️ Now {adjusted_vs_ai} min slower than AI due to pit stops.")
        else:
            st.info("🤖 Your adjusted lap matches AI prediction!")

# PDF Download Section
if 'result' in locals() and isinstance(result, (int, float)):
    st.subheader("📝 Export Lap Summary")

    # Generate PDF only when button clicked
    if st.button("📄 Generate PDF"):
        pdf_path = generate_lap_summary_pdf(selected_track, speed, result)

        # After generating, show download button
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="⬇️ Download Lap Summary PDF",
                data=f,
                file_name="lap_summary.pdf",
                mime="application/pdf"
            )
