import streamlit as st
import random
import pandas as pd

from splits import custom_splits

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO
from exercise_library import get_exercise
from validation import validate_template

from ml_engine import ml_should_superset as should_superset


if "generated_plan" not in st.session_state:
    st.session_state.generated_plan = None
if "last_selection" not in st.session_state:
    st.session_state.last_selection = None
if "pdf_file" not in st.session_state:
    st.session_state.pdf_file = None 
if "show_download" not in st.session_state:
    st.session_state.show_download = False       

st.set_page_config(page_title="AI Fitness Planner", page_icon="aris.png")

st.title("ArisPlan • AI Fitness Planner")
st.write("Plan personalized workouts based on your goals and preferences")



# moved to splits.py


# SPLIT STRUCTURES

splits = {
    "Full Body": [["chest", "back", "legs", "shoulders", "arms", "core"]],
    "Upper / Lower": [["chest", "back", "shoulders", "arms"], ["legs", "core"]],
    "Push / Pull / Legs": [["chest", "shoulders", "triceps"], ["back", "biceps"], ["legs", "core"]],
}


# USER INPUT

st.header("🦾 Plan Your Routine")

# user goal
goal = st.selectbox(
    "What's your main goal?", ["Hyperthrophy (Muscle Gain)", "Strength", "Fat Loss"]
)

goal_map = {
    "Hyperthrophy (Muscle Gain)": "hypertrophy",
    "Fat Loss": "fat_loss",
    "Strength": "strength"
}


goal = goal_map[goal]

# experience level
experience = st.selectbox(
    "Select experience level:", ["Beginner", "Intermediate", "Advanced"]
)

experience_map = {
    "Beginner": "beginner",
    "Intermediate": "intermediate",
    "Advanced": "advanced"
}

experience_key = experience_map[experience]

# Choose number of days
days_per_week = st.selectbox("How many days a week do you want to work out?", ["3", "4", "5", "6"]) # add 4,5,6 later

templates = custom_splits[days_per_week][goal][experience_key]
selected_template = random.choice(templates)



currunt_selection = (days_per_week, selected_template)
if st.session_state.last_selection != currunt_selection:
    st.session_state.generated_plan = None
    st.session_state.last_selection = currunt_selection

# sets function
def get_random_sets(experience_key):
    if experience_key == "beginner":
        return random.choice([2, 3])
    elif experience_key == "intermediate":
        return random.choice([3, 4])
    else: # advanced
        return random.choice([4, 5])

# reps function
def get_random_reps(goal):
    if goal == "strength":
        return random.choice([4, 5, 6])
    elif goal == "fat_loss":
        return random.choice([12, 15, 16])
    else: # hyperthrophy
        return random.choice([8, 10, 12])


# Generate plan   
import random

validate_template(selected_template)
from ai_engine import should_superset

from copy import deepcopy
import random


def generate_plan(selected_split, goal, experience_key):

    plan = {}

    for day, exercises in selected_split.items():

        used_exercises_today = set()
        grouped_plan = []

        i = 0

        while i < len(exercises):

            current = exercises[i]

            
            if len(current) == 3:
                muscle, ex_type, equipment = current
                method = "normal"
            else:
                muscle, ex_type, equipment, method = current

            ex1_raw = get_exercise(
                muscle,
                ex_type,
                equipment,
                used_exercises_today
            )

            used_exercises_today.add(ex1_raw["name"])

            ex1 = {
                "name": ex1_raw["name"],
                "primary": ex1_raw["primary"],
                "secondary": ex1_raw["secondary"],
                "type": ex1_raw["type"],
                "equipment": ex1_raw["equipment"]
            }

            # superset
            if method == "superset":

                if i == len(exercises) - 1:
                    raise ValueError(
                        f"Superset slot cannot be last in {day}"
                    )

                next_ex = exercises[i + 1]

                if len(next_ex) == 3:
                    muscle2, ex_type2, equipment2 = next_ex
                else:
                    muscle2, ex_type2, equipment2, _ = next_ex

                ex2_raw = get_exercise(
                    muscle2,
                    ex_type2,
                    equipment2,
                    used_exercises_today
                )

                used_exercises_today.add(ex2_raw["name"])

                ex2 = {
                    "name": ex2_raw["name"],
                    "primary": ex2_raw["primary"],
                    "secondary": ex2_raw["secondary"],
                    "type": ex2_raw["type"],
                    "equipment": ex2_raw["equipment"]
                }

                shared_sets = get_random_sets(experience_key)
                shared_reps = get_random_reps(goal)

                ex1["sets"] = shared_sets
                ex1["reps"] = shared_reps

                ex2["sets"] = shared_sets
                ex2["reps"] = shared_reps

                grouped_plan.append({
                    "mode": "superset",
                    "exercises": [ex1, ex2]
                })

                i += 2  

            # normal
            else:

                ex1["sets"] = get_random_sets(experience_key)
                ex1["reps"] = get_random_reps(goal)

                grouped_plan.append({
                    "mode": "single",
                    "exercises": [ex1]
                })

                i += 1

        plan[day] = grouped_plan

    return plan






# plan to pdf
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO


def plan_to_pdf(plan):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
    pagesize=A4,
    rightMargin=40,
    leftMargin=40,
    topMargin=40,
    bottomMargin=40
    )

    styles = getSampleStyleSheet()

    story = []

    for day, groups in plan.items():

        # Day title
        story.append(Paragraph(f"<b>{day}</b>", styles["Heading2"]))
        story.append(Spacer(1, 10))

        workout_number = 1

        for group in groups:

            if group["mode"] == "single":

                ex = group["exercises"][0]

                text = f"""
                <b>{workout_number}. {ex['name']}</b>
                — {ex['sets']} x {ex['reps']}
                """

                story.append(Paragraph(text, styles["BodyText"]))


            elif group["mode"] == "superset":

                ex1, ex2 = group["exercises"]

                text = f"""
                <b>{workout_number}. {ex1['name']}</b>
                — {ex1['sets']} x {ex1['reps']}<br/>
                + {ex2['name']}
                — {ex2['sets']} x {ex2['reps']}
                """

                story.append(Paragraph(text, styles["BodyText"]))

            story.append(Spacer(1, 6))
            workout_number += 1

        story.append(Spacer(1, 18))

    doc.build(story)

    buffer.seek(0)

    return buffer

 



# Generate plan BTN
if st.button("Generate plan"):
    templates = custom_splits[days_per_week][goal][experience_key]
    selected_template = random.choice(templates)
    st.session_state.generated_plan = generate_plan(selected_template, goal, experience_key)
    st.session_state.show_download = False
    


# Display plan
if st.session_state.generated_plan:

    for day, groups in st.session_state.generated_plan.items():

        st.subheader(day)
        workout_number = 1

        for group in groups:

            # single workouts
            if group["mode"] == "single":

                ex = group["exercises"][0]

                st.markdown(
                    f"""
                    **{workout_number}. {ex['name']}**
                    <span style='float:right'>
                    {ex['sets']} x {ex['reps']}
                    </span>
                    """,
                    unsafe_allow_html=True
                )


            # supersets
            elif group["mode"] == "superset":

                ex1, ex2 = group["exercises"]

                st.markdown(
                    f"""
                    **{workout_number}. {ex1['name']}**
                    <span style='float:right'>
                    {ex1['sets']} x {ex1['reps']}
                    </span>

                    **+ {ex2['name']}**
                    <span style='float:right'>
                    {ex2['sets']} x {ex2['reps']}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

            workout_number += 1

        st.divider()


    
        
        


            




# export pdf

    if st.session_state.generated_plan:
        if st.button("Prepare PDF"):
            st.session_state.pdf_ready = True
    if st.session_state.get("pdf_ready", False):
        if st.download_button(label="Download PDF",
            data=plan_to_pdf(st.session_state.generated_plan),
            file_name="WorkoutPlan.pdf",
            mime="application/pdf"):
            st.session_state.pdf_ready = False
        
               
    
    