import pandas as pd
import streamlit as st
from scheduler import generate_schedule
from datetime import date
import random

st.title("📚 AI-Based Personalized Study Plan Generator")

# Input fields for subjects, difficulties, and respective exam dates
subjects = [s.strip() for s in st.text_area("Enter your subjects (comma-separated):", "Math, Physics, OOP").split(",")]
difficulties = [d.strip() for d in st.text_area("Enter difficulty levels (comma-separated):", "Medium, Hard, Easy").split(",")]
exam_dates = []

# Ensure there are as many exam dates as subjects
for subject in subjects:
    exam_date = st.date_input(f"Select the exam date for {subject.strip()}:", date(2025, 6, 1))
    exam_dates.append(exam_date)

# Slider for hours per day
hours_per_day = st.slider("How many hours can you study per day?", 1, 12, 4)

if st.button("Generate Study Plan"):
    # Generate the study plan
    plan = generate_schedule(subjects, difficulties, exam_dates, hours_per_day)
    st.success("✅ Study plan generated!")
    st.dataframe(plan)

    # AI motivational tip
    tips = [
        "Stay consistent! Daily progress matters.",
        "Start with the hard subjects first.",
        "Revise in intervals – it boosts memory.",
        "Don't forget to rest and hydrate!"
    ]
    st.markdown(f"💡 **AI Tip:** {random.choice(tips)}")

    # Convert the study plan to CSV and enable downloading
    csv = plan.to_csv(index=False).encode('utf-8')
    st.download_button("📥 Download Study Plan", csv, "study_plan.csv", "text/csv", key="download_plan")
