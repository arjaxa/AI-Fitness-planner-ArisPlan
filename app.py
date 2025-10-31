import streamlit as st
import pandas as pd

st.set_page_config(page_title="AI Fitness Planner", layout="centered")

st.title("🏋️ AI Fitness Planner")
st.write("Get personalized workout plans based on your info")

# Sidebar for user input
st.sidebar.header("Your Information")
age = st.sidebar.slider("Age", 15, 70, 25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
goal = st.sidebar.selectbox("Goal", ["Lose Weight", "Gain Muscle", "Maintain Fitness"])
experience = st.sidebar.selectbox("Experience Level", ["Beginner", "Intermediate", "Advanced"])
days = st.sidebar.slider("Days per week you can train", 1, 7, 3)

# Placeholder workout plan
st.subheader("Your Personalized Workout Plan")
st.write("👇 This is a placeholder. We’ll hook it to an ML model soon.")

workout_plan = {
    "Lose Weight": ["Cardio + HIIT", "Full-body Circuits", "Light Strength Training"],
    "Gain Muscle": ["Heavy Compound Lifts", "Progressive Overload", "Isolation Exercises"],
    "Maintain Fitness": ["Balanced Routine", "Mix of Cardio & Weights", "Mobility Work"]
}

st.write(f"Based on your goal: **{goal}**, here’s a sample plan:")
for item in workout_plan[goal]:
    st.write("- ", item)

st.success("This is the basic skeleton. We'll make it smarter soon!")
# test