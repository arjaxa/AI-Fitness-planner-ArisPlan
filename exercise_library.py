EXERCISE_LIBRARY = [
    # QUADS
    {
        "name": "Leg Extension",
        "primary": "quads",
        "secondary": [], # complete later/ compound 2-3/ isolation []/ also change muscle to primary in get_exercise() or dont
        "type": "isolation",
        "equipment": "machine"
    },
     {
        "name": "Back Squat",
        "primary": "quads",
        "secondary": ["glute"],
        "type": "compound",
        "equipment": "barbell"
    },
     {
        "name": "Goblet Squat",
        "primary": "quads",
        "type": "compound",
        "equipment": "dumbbell"
    },
    {
        "name": "Leg Press",
        "primary": "quads",
        "type": "compound",
        "equipment": "machine"
    },
     {
        "name": "DB Lunge",
        "primary": "quads",
        "type": "compound",
        "equipment": "dumbbell"
    },
     {
        "name": "",
        "primary": "quads",
        "type": "compound",
        "equipment": "dumbbell"
    },
    # HAMSTRING
    {
        "name": "Lying hamstring curls",
        "primary": "hamstring",
        "type": "isolation",
        "equipment": "machine"
    },
     {
        "name": "BB RDL",
        "primary": "hamstring",
        "type": "compound",
        "equipment": "barbell"
    },
     {
        "name": "DB RDL",
        "primary": "hamstring",
        "type": "compound",
        "equipment": "dumbbell"
    },
    {
        "name": "Seated hamstring curl machine",
        "primary": "hamstring",
        "type": "isolation",
        "equipment": "machine"
    },
    # CALVES
     {
        "name": "Standing calf machine",
        "primary": "calf",
        "type": "isolation",
        "equipment": "machine"
    },
     {
        "name": "Seated calf machine",
        "primary": "calf",
        "type": "isolation",
        "equipment": "machine"
    },
    # CHEST
     {
        "name": "BB Bench Press",
        "primary": "chest",
        "type": "compound",
        "equipment": "barbell"
    },
     {
        "name": "DB Bench Press",
        "primary": "chest",
        "type": "compound",
        "equipment": "dumbbell"
    },
    {
        "name": "Cable fly",
        "primary": "chest",
        "type": "isolation",
        "equipment": "cable"
    },
     {
        "name": "DB Fly",
        "primary": "chest",
        "type": "isolation",
        "equipment": "dumbbell"
    },
    # SHOULDER
     {
        "name": "BB Shoulder Press",
        "primary": "shoulder",
        "type": "compound",
        "equipment": "barbell"
    },
     {
        "name": "DB Shoulder Press",
        "primary": "shoulder",
        "type": "isolation",
        "equipment": "dumbbell"
    },
    {
        "name": "Cable lateral raise",
        "primary": "shoulder",
        "type": "isolation",
        "equipment": "cable"
    },
     {
        "name": "DB Fly back",
        "primary": "shoulder",
        "type": "isolation",
        "equipment": "dumbbell"
    },
    # TRICEPS
      {
        "name": "BB Skull Crusher",
        "primary": "triceps",
        "type": "compound",
        "equipment": "barbell"
    },
     {
        "name": "DB Tricep Kickback",
        "primary": "triceps",
        "type": "isolation",
        "equipment": "dumbbell"
    },
    {
        "name": "Cable Rope Tricep Pushdown",
        "primary": "triceps",
        "type": "isolation",
        "equipment": "cable"
    },
     {
        "name": "Tricep Dips",
        "primary": "triceps",
        "type": "compound",
        "equipment": "bodyweight"
    },
    # BACK
    {
        "name": "Lat Pulldown",
        "primary": "back",
        "type": "compound",
        "equipment": "machine"
    },
    {
        "name": "Seated Cable Row",
        "primary": "back",
        "type": "compound",
        "equipment": "cable"
    },
    {
        "name": "Pull-up",
        "primary": "back",
        "type": "compound",
        "equipment": "bodyweight"
    }
]






import random


def get_exercise(muscle, ex_type=None, equipment=None):
    candidates = [
        ex for ex in EXERCISE_LIBRARY if ex["primary"] == muscle # changed "muscle" to "primary"
    ]

    if ex_type:
        candidates = [ex for ex in candidates if ex["type"] == ex_type]

    if equipment:
        candidates = [ex for ex in candidates if ex["equipment"] == equipment]

    if not candidates:
        raise ValueError(
            f"No exercise found for {muscle}, {ex_type}, {equipment}"
        )

    return random.choice(candidates)