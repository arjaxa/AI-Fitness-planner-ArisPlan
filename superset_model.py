import joblib
import random

model = joblib.load("superset_model.pkl")


muscle_map = {
    "quads": 0,
    "hamstring": 1,
    "glute": 2,
    "back": 3,
    "chest": 4,
    "shoulder": 5,
    "biceps": 6,
    "triceps": 7,
    "calf": 8,
    "abs": 9,
    "shoulder_r": 10,
    "shoulder_f": 11,
    "shoulder_l": 12,
    "abductor": 13,
    "adductor": 14,
    "biceps_b": 15,
}

type_map = {
    "compound": 0,
    "isolation": 1
}

equipment_map = {
    "barbell": 0,
    "dumbbell": 1,
    "machine": 2,
    "cable": 3,
    "bodyweight": 4
}

reverse_muscle_map = {v: k for k, v in muscle_map.items()}


def predict_superset_muscle(muscle, ex_type, equipment):
    X = [[
        muscle_map[muscle],
        type_map[ex_type],
    ]]

    prediction = model.predict(X)[0]
    return reverse_muscle_map[prediction]
