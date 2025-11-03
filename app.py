import streamlit as st
import random
import pandas as pd

st.set_page_config(page_title="AI Fitness Planner", page_icon="💪")

st.title("💪 AI Fitness Planner")
st.write("Plan personalized workouts based on your goals and preferences.")

# --------------------------
# 1️⃣ EXERCISE DATABASE
# --------------------------
exercises = {
    "chest": ["Bench Press", "Incline Dumbbell Press", "Push-ups", "Cable Fly", "Chest Dips"],
    "back": ["Pull-ups", "Deadlift", "Barbell Row", "Lat Pulldown", "Seated Cable Row"],
    "legs": ["Squats", "Lunges", "Leg Press", "Romanian Deadlift", "Leg Extension"],
    "shoulders": ["Overhead Press", "Lateral Raises", "Front Raises", "Reverse Fly", "Arnold Press"],
    "arms": ["Bicep Curls", "Tricep Pushdown", "Hammer Curls", "Skull Crushers", "Concentration Curl"],
    "core": ["Plank", "Crunches", "Leg Raises", "Bicycle Crunch", "Russian Twists"],
     "biceps": ["Barbell Curl", "Dumbbell Curl", "Preacher Curl"],
    "triceps": ["Tricep Dips", "Overhead Tricep Extension", "Close Grip Bench Press"]
}

# --------------------------
# 2️⃣ SPLIT STRUCTURES
# --------------------------
splits = {
    "Full Body": [["chest", "back", "legs", "shoulders", "arms", "core"]],
    "Upper / Lower": [["chest", "back", "shoulders", "arms"], ["legs", "core"]],
    "Push / Pull / Legs": [["chest", "shoulders", "triceps"], ["back", "biceps"], ["legs", "core"]],
}

# --------------------------
# 3️⃣ USER INPUT
# --------------------------
st.header("🏋️ Plan Your Routine")

days = st.selectbox("How many days per week do you want to work out?", [3, 4, 5, 6])
split_choice = st.selectbox("Choose your workout split:", list(splits.keys()))

if st.button("Generate Plan"):
    chosen_split = splits[split_choice]
    plan = {}

    # Cycle through the split for the number of workout days
    for i in range(days):
        muscles = chosen_split[i % len(chosen_split)]
        day_plan = []
        for m in muscles:
            day_plan.append(f"{m.capitalize()}: {random.choice(exercises.get(m, []))}")
        plan[f"Day {i+1}"] = day_plan

    st.success(f"✅ Generated {days}-Day {split_choice} Plan")
    for day, workouts in plan.items():
        st.subheader(day)
        for w in workouts:
            st.write(f"- {w}")