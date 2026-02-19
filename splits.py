custom_splits = {
    "3": {
        "hypertrophy": {
            "beginner": [
                # split 1 / PPL
                {
                    "Day 1": [
            ("chest", "compound", "barbell"),
            ("chest", "isolation", "cable"),
            ("chest", "isolation", "machine"),
            ("shoulder", "compound", "barbell"),
            ("shoulder", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("triceps", "compound", "barbell"),
            ("triceps", "isolation", "cable"),
            ("triceps", "compound", "bodyweight")
                    ],
                    "Day 2": [
            ("quads", "isolation", "machine"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "barbell"),
            ("quads", "compound", "dumbbell"),
            ("hamstring", "compound", "barbell"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "compound", "dumbbell"),
            ("calf", "isolation", "machine")           
                    ],
                    "Day 3": [
            ("back", "compound", "machine"),
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "compound", "bodyweight"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "dumbbell"),
            ("lower_back", "isolation", "bodyweight")           
                    ]
                },
                # split 2
                {
                    "Day 1": [
            ("chest", "compound", "barbell"),
            ("chest", "isolation", "machine"),
            ("chest", "isolation", "dumbbell"),
            ("shoulder", "compound", "barbell"),
            ("shoulder", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("triceps", "compound", "barbell"),
            ("triceps", "isolation", "cable"),
            ("triceps", "compound", "bodyweight")            
                    ],
                    "Day 2": [
            ("quads", "isolation", "machine"),
            ("quads", "compound", "barbell"),
            ("quads", "compound", "dumbbell"),
            ("hamstring", "compound", "barbell"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "compound", "dumbbell"),
            ("calf", "isolation", "machine")            
                    ],
                    "Day 3": [
            ("back", "compound", "machine"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("back", "compound", "bodyweight"),
            ("lower_back", "isolation", "bodyweight")

                    ]
                }
            ],
            "intermediate": [
                # split 1 / PPL
                {
    "Day 1": [
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("quads", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_desc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine"),
        ("glute", "compound", "barbell", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "isolation", "machine", "pyramid_asc"),
        ("quads", "isolation", "cable"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_desc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine"),
        ("triceps", "isolation", "barbell", "superset"),
        ("biceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_asc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "cable", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable", "pyramid_desc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_desc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable", "pyramid_desc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "isolation"),
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable", "fst7"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable")
    ],

    "Day 3": [
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_desc")
    ]
},
{
    "Day 1": [
        ("quads", "isolation", "machine"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "machine", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable")
    ],

    "Day 3": [
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_desc")
    ]
}
            ],
            "advanced": [
                # split 1
                {
    "Day 1": [
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("quads", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_desc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine"),
        ("glute", "compound", "barbell", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "isolation", "machine", "pyramid_asc"),
        ("quads", "isolation", "cable"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_desc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine"),
        ("triceps", "isolation", "barbell", "superset"),
        ("biceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_asc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "cable", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable", "pyramid_desc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_desc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable", "pyramid_desc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "isolation"),
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable", "fst7"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable")
    ],

    "Day 3": [
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_desc")
    ]
},
{
    "Day 1": [
        ("quads", "isolation", "machine"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "machine", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable")
    ],

    "Day 3": [
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_desc")
    ]
}


            ]
        },
        "strength": {
            "beginner": [
                # split 1 / PPL
                {
                    "Day 1": [
            ("chest", "compound", "barbell"),
            ("chest", "isolation", "cable"),
            ("chest", "isolation", "machine"),
            ("shoulder", "compound", "barbell"),
            ("shoulder", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("triceps", "compound", "barbell"),
            ("triceps", "isolation", "cable"),
            ("triceps", "compound", "bodyweight")
                    ],
                    "Day 2": [
            ("quads", "isolation", "machine"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "barbell"),
            ("quads", "compound", "dumbbell"),
            ("hamstring", "compound", "barbell"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "compound", "dumbbell"),
            ("calf", "isolation", "machine")           
                    ],
                    "Day 3": [
            ("back", "compound", "machine"),
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "compound", "bodyweight"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "dumbbell"),
            ("lower_back", "isolation", "bodyweight")           
                    ]
                },
                # split 2
                {
                    "Day 1": [
            ("chest", "compound", "barbell"),
            ("chest", "isolation", "machine"),
            ("chest", "isolation", "dumbbell"),
            ("shoulder", "compound", "barbell"),
            ("shoulder", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("triceps", "compound", "barbell"),
            ("triceps", "isolation", "cable"),
            ("triceps", "compound", "bodyweight")            
                    ],
                    "Day 2": [
            ("quads", "isolation", "machine"),
            ("quads", "compound", "barbell"),
            ("quads", "compound", "dumbbell"),
            ("hamstring", "compound", "barbell"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "compound", "dumbbell"),
            ("calf", "isolation", "machine")            
                    ],
                    "Day 3": [
            ("back", "compound", "machine"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("back", "compound", "bodyweight"),
            ("lower_back", "isolation", "bodyweight")

                    ]
                }
            ],
            "intermediate": [
                # split 1 / PPL
                {
    "Day 1": [
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("quads", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_desc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine"),
        ("glute", "compound", "barbell", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "isolation", "machine", "pyramid_asc"),
        ("quads", "isolation", "cable"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_desc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine"),
        ("triceps", "isolation", "barbell", "superset"),
        ("biceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_asc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "cable", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable", "pyramid_desc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_desc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable", "pyramid_desc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "isolation"),
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable", "fst7"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable")
    ],

    "Day 3": [
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_desc")
    ]
},
{
    "Day 1": [
        ("quads", "isolation", "machine"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "machine", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable")
    ],

    "Day 3": [
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_desc")
    ]
}
            ],
            "advanced": [
                # split 1
                {
    "Day 1": [
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("quads", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_desc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine"),
        ("glute", "compound", "barbell", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "isolation", "machine", "pyramid_asc"),
        ("quads", "isolation", "cable"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_desc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine"),
        ("triceps", "isolation", "barbell", "superset"),
        ("biceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_asc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "cable", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable", "pyramid_desc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_desc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable", "pyramid_desc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "isolation"),
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable", "fst7"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable")
    ],

    "Day 3": [
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_desc")
    ]
},
{
    "Day 1": [
        ("quads", "isolation", "machine"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "machine", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable")
    ],

    "Day 3": [
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_desc")
    ]
}


            ]
        },
        "fat_loss":{
            "beginner": [
                # split 1 / PPL
                {
                    "Day 1": [
            ("chest", "compound", "barbell"),
            ("chest", "isolation", "cable"),
            ("chest", "isolation", "machine"),
            ("shoulder", "compound", "barbell"),
            ("shoulder", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("triceps", "compound", "barbell"),
            ("triceps", "isolation", "cable"),
            ("triceps", "compound", "bodyweight")
                    ],
                    "Day 2": [
            ("quads", "isolation", "machine"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "barbell"),
            ("quads", "compound", "dumbbell"),
            ("hamstring", "compound", "barbell"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "compound", "dumbbell"),
            ("calf", "isolation", "machine")           
                    ],
                    "Day 3": [
            ("back", "compound", "machine"),
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "compound", "bodyweight"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "dumbbell"),
            ("lower_back", "isolation", "bodyweight")           
                    ]
                },
                # split 2
                {
                    "Day 1": [
            ("chest", "compound", "barbell"),
            ("chest", "isolation", "machine"),
            ("chest", "isolation", "dumbbell"),
            ("shoulder", "compound", "barbell"),
            ("shoulder", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("triceps", "compound", "barbell"),
            ("triceps", "isolation", "cable"),
            ("triceps", "compound", "bodyweight")            
                    ],
                    "Day 2": [
            ("quads", "isolation", "machine"),
            ("quads", "compound", "barbell"),
            ("quads", "compound", "dumbbell"),
            ("hamstring", "compound", "barbell"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "compound", "dumbbell"),
            ("calf", "isolation", "machine")            
                    ],
                    "Day 3": [
            ("back", "compound", "machine"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("back", "compound", "bodyweight"),
            ("lower_back", "isolation", "bodyweight")

                    ]
                }
            ],
            "intermediate": [
                # split 1 / PPL
                {
    "Day 1": [
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("quads", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_desc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine"),
        ("glute", "compound", "barbell", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "isolation", "machine", "pyramid_asc"),
        ("quads", "isolation", "cable"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_desc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine"),
        ("triceps", "isolation", "barbell", "superset"),
        ("biceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_asc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "cable", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable", "pyramid_desc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_desc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable", "pyramid_desc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "isolation"),
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable", "fst7"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable")
    ],

    "Day 3": [
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_desc")
    ]
},
{
    "Day 1": [
        ("quads", "isolation", "machine"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "machine", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable")
    ],

    "Day 3": [
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_desc")
    ]
}
            ],
            "advanced": [
                # split 1
                {
    "Day 1": [
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("quads", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_desc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine"),
        ("glute", "compound", "barbell", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "isolation", "machine", "pyramid_asc"),
        ("quads", "isolation", "cable"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_desc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine"),
        ("triceps", "isolation", "barbell", "superset"),
        ("biceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_asc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "cable", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable", "pyramid_desc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "pyramid_desc")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable", "pyramid_desc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "superset"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "isolation"),
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable", "fst7"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable")
    ],

    "Day 3": [
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_desc")
    ]
},
{
    "Day 1": [
        ("quads", "isolation", "machine"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "machine", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell")
    ],

    "Day 3": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable", "pyramid_asc")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_asc")
    ],

    "Day 2": [
        ("back", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("biceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable")
    ],

    "Day 3": [
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "pyramid_desc")
    ]
}


            ]
        }
    },

     "4": {
        "hypertrophy": {
            "beginner": [
                # split 1
                {
                 "Day 1": [
            ("quads", "compound", "barbell"),
            ("quads", "compound", "machine"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder", "compound", "machine"),
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "cable"),
            ("biceps", "isolation", "dumbbell"),
            ("biceps", "isolation", "cable"),
            ("abs", "isolation", "cable")            
                    ],
                    "Day 3": [
            ("back", "compound", "machine"),
            ("back", "compound", "machine"),
            ("back", "compound", "barbell"),
            ("back", "compound", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "dumbbell"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                    "Day 4": [
            ("hamstring", "compound", "machine"),
            ("hamstring", "compound", "barbell"),
            ("hamstring", "compound", "dumbbell"),
            ("glute", "isolation", "dumbbell"),
            ("glute", "compound", "barbell"),
            ("hamstring", "isolation", "machine"),
            ("glute", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]  
                },
                # split 2
                {
                 "Day 1": [
            ("quads", "isolation", "machine"),
            ("quads", "compound", "machine"),
            ("quads", "compound", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable"),
            ("back", "isolation", "dumbbell"),
            ("back", "compound", "machine"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "compound", "barbell"),
            ("hamstring", "compound", "barbell"),
            ("glute", "isolation", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "isolation", "dumbbell"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]
                }
            ],
            "intermediate": [
                # split 1
                {
                 "Day 1": [
            ("quads", "compound", "barbell", "pyramid_asc"),
            ("quads", "compound", "machine", "superset"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder", "compound", "machine", "superset"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable", "fst7"),
            ("shoulder_r", "isolation", "cable", "superset"),
            ("shoulder_r", "isolation", "dumbbell"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("biceps_b", "isolation", "dumbbell"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "machine"),
            ("back", "compound", "machine"),
            ("back", "compound", "machine", "superset"),
            ("back", "compound", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "dumbbell"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                    "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("hamstring", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("glute", "isolation", "dumbbell", "pyramid_asc"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "barbell", "fst7"),
            ("glute", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]  
                },
                {
    "Day 1": [
        ("quads", "compound", "machine", "pyramid_desc"),
        ("quads", "compound", "barbell"),
        ("quads", "isolation", "cable", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "dumbbell"),
        ("abductor", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("lower_back", "isolation", "bodyweight"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "dumbbell", "fst7"),
        ("biceps_b", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 3": [
        ("shoulder", "compound", "dumbbell"),
        ("shoulder", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "cable"),
        ("shoulder_l", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "cable", "fst7"),
        ("chest", "compound", "barbell"),
        ("chest", "compound", "machine"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "dumbbell"),
        ("abs", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable")
    ]
},
                {
    "Day 1": [
        ("quads", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("abductor", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 2": [
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "cable", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "fst7"),
        ("abs", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "machine"),
        ("back", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("chest", "compound", "dumbbell"),
        ("chest", "compound", "machine", "pyramid_desc"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "fst7"),
        ("lower_back", "isolation", "bodyweight"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "compound", "dumbbell"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "dumbbell"),
        ("abductor", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable"),
        ("chest", "compound", "barbell"),
        ("chest", "compound", "dumbbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "dumbbell", "fst7"),
        ("lower_back", "isolation", "bodyweight"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 3": [
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("biceps_b", "isolation", "dumbbell"),
        ("abs", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "barbell"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "isolation", "machine"),
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_desc"),
        ("shoulder_r", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "dumbbell"),
        ("chest", "compound", "dumbbell", "pyramid_asc"),
        ("chest", "compound", "machine", "superset"),
        ("chest", "isolation", "dumbbell"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "compound", "barbell"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc")
    ]
},



                
                # split 2
                {
                 "Day 1": [
            ("quads", "isolation", "machine"),
            ("quads", "compound", "barbell", "pyramid_asc"),
            ("quads", "compound", "machine", "pyramid_desc"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine", "superset"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine", "fst7"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "dumbbell", "superset"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell", "pyramid_desc"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell", "pyramid_asc"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable", "superset"),
            ("back", "isolation", "dumbbell"),
            ("back", "compound", "machine"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "compound", "barbell", "superset"),
            ("hamstring", "compound", "dumbbell"),
            ("glute", "isolation", "dumbbell", "pyramid_desc"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "isolation", "dumbbell"),
            ("calf", "isolation", "machine", "fst7"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]
                }
            ],
            "advanced": [
                # split 1
                {
                 "Day 1": [
            ("quads", "compound", "barbell", "pyramid_asc"),
            ("quads", "compound", "machine", "superset"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder", "compound", "machine", "superset"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable", "fst7"),
            ("shoulder_r", "isolation", "cable", "superset"),
            ("shoulder_r", "isolation", "dumbbell"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("biceps_b", "isolation", "dumbbell"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "machine", "superset"),
            ("back", "compound", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "dumbbell"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                    "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("hamstring", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("glute", "isolation", "dumbbell", "pyramid_asc"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "barbell", "fst7"),
            ("glute", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]  
                },
                {
    "Day 1": [
        ("quads", "compound", "machine", "pyramid_desc"),
        ("quads", "compound", "barbell"),
        ("quads", "isolation", "cable", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "dumbbell"),
        ("abductor", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("lower_back", "isolation", "bodyweight"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "dumbbell", "fst7"),
        ("biceps_b", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 3": [
        ("shoulder", "compound", "dumbbell"),
        ("shoulder", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "cable"),
        ("shoulder_l", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "cable", "fst7"),
        ("chest", "compound", "barbell"),
        ("chest", "compound", "machine"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "dumbbell"),
        ("abs", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable")
    ]
},
                {
    "Day 1": [
        ("quads", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("abductor", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 2": [
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "cable", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "fst7"),
        ("abs", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "machine"),
        ("back", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("chest", "compound", "dumbbell"),
        ("chest", "compound", "machine", "pyramid_desc"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "fst7"),
        ("lower_back", "isolation", "bodyweight"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "compound", "dumbbell"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "dumbbell"),
        ("abductor", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable"),
        ("chest", "compound", "barbell"),
        ("chest", "compound", "dumbbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "dumbbell", "fst7"),
        ("lower_back", "isolation", "bodyweight"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 3": [
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("biceps_b", "isolation", "dumbbell"),
        ("abs", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "barbell"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "isolation", "machine"),
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_desc"),
        ("shoulder_r", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "dumbbell"),
        ("chest", "compound", "dumbbell", "pyramid_asc"),
        ("chest", "compound", "machine", "superset"),
        ("chest", "isolation", "dumbbell"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "compound", "barbell"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc")
    ]
},



                
                # split 2
                {
                 "Day 1": [
            ("quads", "isolation", "machine"),
            ("quads", "compound", "barbell", "pyramid_asc"),
            ("quads", "compound", "machine", "pyramid_desc"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine", "superset"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine", "fst7"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "dumbbell", "superset"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell", "pyramid_desc"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell", "pyramid_asc"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable", "superset"),
            ("back", "isolation", "dumbbell"),
            ("back", "compound", "machine"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "compound", "barbell", "superset"),
            ("hamstring", "compound", "dumbbell"),
            ("glute", "isolation", "dumbbell", "pyramid_desc"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "isolation", "dumbbell"),
            ("calf", "isolation", "machine", "fst7"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]
                }
            ]
        },
        "fat_loss":{
            "beginner": [
                # split 1
                {
                 "Day 1": [
            ("quads", "compound", "barbell"),
            ("quads", "compound", "machine"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder", "compound", "machine"),
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "cable"),
            ("biceps", "isolation", "dumbbell"),
            ("biceps", "isolation", "cable"),
            ("abs", "isolation", "cable")            
                    ],
                    "Day 3": [
            ("back", "compound", "machine"),
            ("back", "compound", "machine"),
            ("back", "compound", "barbell"),
            ("back", "compound", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "dumbbell"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                    "Day 4": [
            ("hamstring", "compound", "machine"),
            ("hamstring", "compound", "barbell"),
            ("hamstring", "compound", "dumbbell"),
            ("glute", "isolation", "dumbbell"),
            ("glute", "compound", "barbell"),
            ("hamstring", "isolation", "machine"),
            ("glute", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]  
                },
                # split 2
                {
                 "Day 1": [
            ("quads", "isolation", "machine"),
            ("quads", "compound", "machine"),
            ("quads", "compound", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable"),
            ("back", "isolation", "dumbbell"),
            ("back", "compound", "machine"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "compound", "barbell"),
            ("hamstring", "compound", "barbell"),
            ("glute", "isolation", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "isolation", "dumbbell"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]
                }
            ],
            "intermediate": [
                # split 1
                {
                 "Day 1": [
            ("quads", "compound", "barbell", "pyramid_asc"),
            ("quads", "compound", "machine", "superset"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder", "compound", "machine", "superset"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable", "fst7"),
            ("shoulder_r", "isolation", "cable", "superset"),
            ("shoulder_r", "isolation", "dumbbell"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("biceps_b", "isolation", "dumbbell"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "machine", "superset"),
            ("back", "compound", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "dumbbell"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                    "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("hamstring", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("glute", "isolation", "dumbbell", "pyramid_asc"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "barbell", "fst7"),
            ("glute", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]  
                },
                {
    "Day 1": [
        ("quads", "compound", "machine", "pyramid_desc"),
        ("quads", "compound", "barbell"),
        ("quads", "isolation", "cable", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "dumbbell"),
        ("abductor", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("lower_back", "isolation", "bodyweight"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "dumbbell", "fst7"),
        ("biceps_b", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 3": [
        ("shoulder", "compound", "dumbbell"),
        ("shoulder", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "cable"),
        ("shoulder_l", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "cable", "fst7"),
        ("chest", "compound", "barbell"),
        ("chest", "compound", "machine"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "dumbbell"),
        ("abs", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable")
    ]
},
                {
    "Day 1": [
        ("quads", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("abductor", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 2": [
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "cable", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "fst7"),
        ("abs", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "machine"),
        ("back", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("chest", "compound", "dumbbell"),
        ("chest", "compound", "machine", "pyramid_desc"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "fst7"),
        ("lower_back", "isolation", "bodyweight"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "compound", "dumbbell"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "dumbbell"),
        ("abductor", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable"),
        ("chest", "compound", "barbell"),
        ("chest", "compound", "dumbbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "dumbbell", "fst7"),
        ("lower_back", "isolation", "bodyweight"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 3": [
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("biceps_b", "isolation", "dumbbell"),
        ("abs", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "barbell"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "isolation", "machine"),
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_desc"),
        ("shoulder_r", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "dumbbell"),
        ("chest", "compound", "dumbbell", "pyramid_asc"),
        ("chest", "compound", "machine", "superset"),
        ("chest", "isolation", "dumbbell"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "compound", "barbell"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc")
    ]
},



                
                # split 2
                {
                 "Day 1": [
            ("quads", "isolation", "machine"),
            ("quads", "compound", "barbell", "pyramid_asc"),
            ("quads", "compound", "machine", "pyramid_desc"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine", "superset"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine", "fst7"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "dumbbell", "superset"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell", "pyramid_desc"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell", "pyramid_asc"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable", "superset"),
            ("back", "isolation", "dumbbell"),
            ("back", "compound", "machine"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "compound", "barbell", "superset"),
            ("hamstring", "compound", "dumbbell"),
            ("glute", "isolation", "dumbbell", "pyramid_desc"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "isolation", "dumbbell"),
            ("calf", "isolation", "machine", "fst7"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]
                }
            ],
            "advanced": [
                # split 1
                {
                 "Day 1": [
            ("quads", "compound", "barbell", "pyramid_asc"),
            ("quads", "compound", "machine", "superset"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder", "compound", "machine", "superset"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable", "fst7"),
            ("shoulder_r", "isolation", "cable", "superset"),
            ("shoulder_r", "isolation", "dumbbell"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("biceps_b", "isolation", "dumbbell"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "machine", "superset"),
            ("back", "compound", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "dumbbell"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                    "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("hamstring", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("glute", "isolation", "dumbbell", "pyramid_asc"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "barbell", "fst7"),
            ("glute", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]  
                },
                {
    "Day 1": [
        ("quads", "compound", "machine", "pyramid_desc"),
        ("quads", "compound", "barbell"),
        ("quads", "isolation", "cable", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "dumbbell"),
        ("abductor", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("lower_back", "isolation", "bodyweight"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "dumbbell", "fst7"),
        ("biceps_b", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 3": [
        ("shoulder", "compound", "dumbbell"),
        ("shoulder", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "cable"),
        ("shoulder_l", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "cable", "fst7"),
        ("chest", "compound", "barbell"),
        ("chest", "compound", "machine"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "dumbbell"),
        ("abs", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable")
    ]
},
                {
    "Day 1": [
        ("quads", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("abductor", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 2": [
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "cable", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "fst7"),
        ("abs", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "machine"),
        ("back", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("chest", "compound", "dumbbell"),
        ("chest", "compound", "machine", "pyramid_desc"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "fst7"),
        ("lower_back", "isolation", "bodyweight"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "compound", "dumbbell"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "dumbbell"),
        ("abductor", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable"),
        ("chest", "compound", "barbell"),
        ("chest", "compound", "dumbbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "dumbbell", "fst7"),
        ("lower_back", "isolation", "bodyweight"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 3": [
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("biceps_b", "isolation", "dumbbell"),
        ("abs", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "barbell"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "isolation", "machine"),
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_desc"),
        ("shoulder_r", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "dumbbell"),
        ("chest", "compound", "dumbbell", "pyramid_asc"),
        ("chest", "compound", "machine", "superset"),
        ("chest", "isolation", "dumbbell"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "compound", "barbell"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc")
    ]
},



                
                # split 2
                {
                 "Day 1": [
            ("quads", "isolation", "machine"),
            ("quads", "compound", "barbell", "pyramid_asc"),
            ("quads", "compound", "machine", "pyramid_desc"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine", "superset"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine", "fst7"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "dumbbell", "superset"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell", "pyramid_desc"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell", "pyramid_asc"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable", "superset"),
            ("back", "isolation", "dumbbell"),
            ("back", "compound", "machine"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "compound", "barbell", "superset"),
            ("hamstring", "compound", "dumbbell"),
            ("glute", "isolation", "dumbbell", "pyramid_desc"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "isolation", "dumbbell"),
            ("calf", "isolation", "machine", "fst7"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]
                }
            ]
        },
        "strength":{
            "beginner": [
                # split 1
                {
                 "Day 1": [
            ("quads", "compound", "barbell"),
            ("quads", "compound", "machine"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder", "compound", "machine"),
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "cable"),
            ("biceps", "isolation", "dumbbell"),
            ("biceps", "isolation", "cable"),
            ("abs", "isolation", "cable")            
                    ],
                    "Day 3": [
            ("back", "compound", "machine"),
            ("back", "compound", "machine"),
            ("back", "compound", "barbell"),
            ("back", "compound", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "dumbbell"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                    "Day 4": [
            ("hamstring", "compound", "machine"),
            ("hamstring", "compound", "barbell"),
            ("hamstring", "compound", "dumbbell"),
            ("glute", "isolation", "dumbbell"),
            ("glute", "compound", "barbell"),
            ("hamstring", "isolation", "machine"),
            ("glute", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]  
                },
                # split 2
                {
                 "Day 1": [
            ("quads", "isolation", "machine"),
            ("quads", "compound", "machine"),
            ("quads", "compound", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable"),
            ("back", "isolation", "dumbbell"),
            ("back", "compound", "machine"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "compound", "barbell"),
            ("hamstring", "compound", "barbell"),
            ("glute", "isolation", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "isolation", "dumbbell"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]
                }
            ],
            "intermediate": [
                # split 1
                {
                 "Day 1": [
            ("quads", "compound", "barbell", "pyramid_asc"),
            ("quads", "compound", "machine", "superset"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder", "compound", "machine", "superset"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable", "fst7"),
            ("shoulder_r", "isolation", "cable", "superset"),
            ("shoulder_r", "isolation", "dumbbell"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("biceps_b", "isolation", "dumbbell"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "machine", "superset"),
            ("back", "compound", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "dumbbell"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                    "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("hamstring", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("glute", "isolation", "dumbbell", "pyramid_asc"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "barbell", "fst7"),
            ("glute", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]  
                },
                {
    "Day 1": [
        ("quads", "compound", "machine", "pyramid_desc"),
        ("quads", "compound", "barbell"),
        ("quads", "isolation", "cable", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "dumbbell"),
        ("abductor", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("lower_back", "isolation", "bodyweight"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "dumbbell", "fst7"),
        ("biceps_b", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 3": [
        ("shoulder", "compound", "dumbbell"),
        ("shoulder", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "cable"),
        ("shoulder_l", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "cable", "fst7"),
        ("chest", "compound", "barbell"),
        ("chest", "compound", "machine"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "dumbbell"),
        ("abs", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable")
    ]
},
                {
    "Day 1": [
        ("quads", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("abductor", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 2": [
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "cable", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "fst7"),
        ("abs", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "machine"),
        ("back", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("chest", "compound", "dumbbell"),
        ("chest", "compound", "machine", "pyramid_desc"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "fst7"),
        ("lower_back", "isolation", "bodyweight"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "compound", "dumbbell"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "dumbbell"),
        ("abductor", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable"),
        ("chest", "compound", "barbell"),
        ("chest", "compound", "dumbbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "dumbbell", "fst7"),
        ("lower_back", "isolation", "bodyweight"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 3": [
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("biceps_b", "isolation", "dumbbell"),
        ("abs", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "barbell"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "isolation", "machine"),
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_desc"),
        ("shoulder_r", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "dumbbell"),
        ("chest", "compound", "dumbbell", "pyramid_asc"),
        ("chest", "compound", "machine", "superset"),
        ("chest", "isolation", "dumbbell"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "compound", "barbell"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc")
    ]
},



                
                # split 2
                {
                 "Day 1": [
            ("quads", "isolation", "machine"),
            ("quads", "compound", "barbell", "pyramid_asc"),
            ("quads", "compound", "machine", "pyramid_desc"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine", "superset"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine", "fst7"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "dumbbell", "superset"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell", "pyramid_desc"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell", "pyramid_asc"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable", "superset"),
            ("back", "isolation", "dumbbell"),
            ("back", "compound", "machine"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "compound", "barbell", "superset"),
            ("hamstring", "compound", "dumbbell"),
            ("glute", "isolation", "dumbbell", "pyramid_desc"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "isolation", "dumbbell"),
            ("calf", "isolation", "machine", "fst7"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]
                }
            ],
            "advanced": [
                # split 1
                {
                 "Day 1": [
            ("quads", "compound", "barbell", "pyramid_asc"),
            ("quads", "compound", "machine", "superset"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder", "compound", "machine", "superset"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable", "fst7"),
            ("shoulder_r", "isolation", "cable", "superset"),
            ("shoulder_r", "isolation", "dumbbell"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("biceps_b", "isolation", "dumbbell"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "machine", "superset"),
            ("back", "compound", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "dumbbell"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                    "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("hamstring", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("glute", "isolation", "dumbbell", "pyramid_asc"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "barbell", "fst7"),
            ("glute", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]  
                },
                {
    "Day 1": [
        ("quads", "compound", "machine", "pyramid_desc"),
        ("quads", "compound", "barbell"),
        ("quads", "isolation", "cable", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "dumbbell"),
        ("abductor", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("lower_back", "isolation", "bodyweight"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "dumbbell", "fst7"),
        ("biceps_b", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 3": [
        ("shoulder", "compound", "dumbbell"),
        ("shoulder", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "cable"),
        ("shoulder_l", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "cable", "fst7"),
        ("chest", "compound", "barbell"),
        ("chest", "compound", "machine"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "dumbbell"),
        ("abs", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable")
    ]
},
                {
    "Day 1": [
        ("quads", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "cable"),
        ("abductor", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 2": [
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "cable", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell", "fst7"),
        ("abs", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "machine"),
        ("back", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("chest", "compound", "dumbbell"),
        ("chest", "compound", "machine", "pyramid_desc"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "fst7"),
        ("lower_back", "isolation", "bodyweight"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "compound", "dumbbell"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "dumbbell"),
        ("abductor", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable")
    ],

    "Day 2": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable"),
        ("chest", "compound", "barbell"),
        ("chest", "compound", "dumbbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("triceps", "isolation", "dumbbell", "fst7"),
        ("lower_back", "isolation", "bodyweight"),
        ("abs", "isolation", "bodyweight")
    ],

    "Day 3": [
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("shoulder_r", "isolation", "machine"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("biceps_b", "isolation", "dumbbell"),
        ("abs", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "fst7"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "cable")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "barbell"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "isolation", "machine"),
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "cable"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_desc"),
        ("shoulder_r", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "dumbbell"),
        ("chest", "compound", "dumbbell", "pyramid_asc"),
        ("chest", "compound", "machine", "superset"),
        ("chest", "isolation", "dumbbell"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "compound", "barbell"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc")
    ]
},



                
                # split 2
                {
                 "Day 1": [
            ("quads", "isolation", "machine"),
            ("quads", "compound", "barbell", "pyramid_asc"),
            ("quads", "compound", "machine", "pyramid_desc"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine", "superset"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine", "fst7"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "dumbbell", "superset"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell", "pyramid_desc"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "cable"),
            ("abs", "isolation", "cable")           
                    ],
                    "Day 3": [
            ("back", "compound", "barbell", "pyramid_asc"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable", "superset"),
            ("back", "isolation", "dumbbell"),
            ("back", "compound", "machine"),
            ("lower_back", "isolation", "bodyweight"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "compound", "barbell", "superset"),
            ("hamstring", "compound", "dumbbell"),
            ("glute", "isolation", "dumbbell", "pyramid_desc"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "isolation", "dumbbell"),
            ("calf", "isolation", "machine", "fst7"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ]
                }
            ]
        }
    },

    "5": {
        "hypertrophy": {
            "beginner": [
                # split 1
                {
                 "Day 1": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_r", "isolation", "cable"),
            ("triceps", "isolation", "cable"),
            ("abs", "isolation", "cable"),
            
                        
                    ],
                    "Day 2": [
            ("quads", "compound", "barbell"),
            ("quads", "compound", "machine"),
            ("quads", "compound", "dumbbell"),
            ("quads", "isolation", "machine"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")            
                    ],
                    "Day 3": [
            ("back", "compound", "machine"),
            ("back", "compound", "barbell"),
            ("back", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("biceps", "isolation", "cable"),
            ("lower_back", "isolation", "bodyweight"),
            ("abs", "isolation", "cable"),
            ("abs", "isolation", "bodyweight")
                    ],
                    "Day 4": [
            ("hamstring", "isolation", "dumbbell"),            
            ("hamstring", "compound", "barbell"),
            ("hamstring", "compound", "machine"),
            ("hamstring", "compound", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ],
                    "Day 5": [
            ("glute", "compound", "barbell"),            
            ("glute", "compound", "machine"),
            ("glute", "isolation", "cable"),
            ("glute", "isolation", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("abductor", "isolation", "machine"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight")
                    ] 
                },
                # split 2
                {
                 "Day 1": [
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable"),
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "barbell"),
            ("triceps", "isolation", "dumbbell"),
            ("triceps", "isolation", "cable"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("quads", "compound", "machine"),
            ("quads", "compound", "barbell"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("adductor", "isolation", "machine"),
            ("calf", "isolation", "machine")           
                    ],
                    "Day 3": [
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder", "isolation", "dumbbell"),
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("lower_back", "isolation", "bodyweight"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "compound", "barbell"),
            ("glute", "compound", "machine"),
            ("glute", "isolation", "cable"),
            ("hamstring", "compound", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("glute", "isolation", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "isolation", "dumbbell"),
            ("abductor", "isolation", "machine"),
            ("calf", "isolation", "machine")
                    ],
                    "Day 5": [
            ("glute", "compound", "barbell"),
            ("quads", "compound", "dumbbell"),
            ("glute", "compound", "machine"),
            ("hamstring", "compound", "cable"),
            ("hamstring", "isolation", "machine"),
            ("glute", "isolation", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "isolation", "dumbbell"),
            ("abductor", "isolation", "machine"),
            ("calf", "isolation", "machine")
                    ]
                }
            ],
            "intermediate": [
                # split 1
                {
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("triceps", "isolation", "barbell", "fst7"),
        ("back", "isolation", "cable"),
        ("triceps", "isolation", "cable")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "pyramid_asc"),
        ("quads", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "dumbbell")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_asc"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine")
    ]
}
            ],
            "advanced": [
                # split 1
                {
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("triceps", "isolation", "barbell", "fst7"),
        ("back", "isolation", "cable"),
        ("triceps", "isolation", "cable")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "pyramid_asc"),
        ("quads", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "dumbbell")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_asc"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine")
    ]
}
            ]
        
        },
        "strength": {
            "beginner": [
                # split 1
                {
                 "Day 1": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_r", "isolation", "cable"),
            ("triceps", "isolation", "cable"),
            ("abs", "isolation", "cable"),
            
                        
                    ],
                    "Day 2": [
            ("quads", "compound", "barbell"),
            ("quads", "compound", "machine"),
            ("quads", "compound", "dumbbell"),
            ("quads", "isolation", "machine"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")            
                    ],
                    "Day 3": [
            ("back", "compound", "machine"),
            ("back", "compound", "barbell"),
            ("back", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("biceps", "isolation", "cable"),
            ("lower_back", "isolation", "bodyweight"),
            ("abs", "isolation", "cable"),
            ("abs", "isolation", "bodyweight")
                    ],
                    "Day 4": [
            ("hamstring", "isolation", "dumbbell"),            
            ("hamstring", "compound", "barbell"),
            ("hamstring", "compound", "machine"),
            ("hamstring", "compound", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ],
                    "Day 5": [
            ("glute", "compound", "barbell"),            
            ("glute", "compound", "machine"),
            ("glute", "isolation", "cable"),
            ("glute", "isolation", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("abductor", "isolation", "machine"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight")
                    ] 
                },
                # split 2
                {
                 "Day 1": [
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable"),
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "barbell"),
            ("triceps", "isolation", "dumbbell"),
            ("triceps", "isolation", "cable"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("quads", "compound", "machine"),
            ("quads", "compound", "barbell"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("adductor", "isolation", "machine"),
            ("calf", "isolation", "machine")           
                    ],
                    "Day 3": [
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder", "isolation", "dumbbell"),
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("lower_back", "isolation", "bodyweight"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "compound", "barbell"),
            ("glute", "compound", "machine"),
            ("glute", "isolation", "cable"),
            ("hamstring", "compound", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("glute", "isolation", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "isolation", "dumbbell"),
            ("abductor", "isolation", "machine"),
            ("calf", "isolation", "machine")
                    ],
                    "Day 5": [
            ("glute", "compound", "barbell"),
            ("quads", "compound", "dumbbell"),
            ("glute", "compound", "machine"),
            ("hamstring", "compound", "cable"),
            ("hamstring", "isolation", "machine"),
            ("glute", "isolation", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "isolation", "dumbbell"),
            ("abductor", "isolation", "machine"),
            ("calf", "isolation", "machine")
                    ]
                }
            ],
            "intermediate": [
                # split 1
                {
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("triceps", "isolation", "barbell", "fst7"),
        ("back", "isolation", "cable"),
        ("triceps", "isolation", "cable")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "pyramid_asc"),
        ("quads", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "dumbbell")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_asc"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine")
    ]
}
            ],
            "advanced": [
                # split 1
                {
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("triceps", "isolation", "barbell", "fst7"),
        ("back", "isolation", "cable"),
        ("triceps", "isolation", "cable")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "pyramid_asc"),
        ("quads", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "dumbbell")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_asc"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine")
    ]
}
            ]
        
        },
        "fat_loss": {
            "beginner": [
                # split 1
                {
                 "Day 1": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_r", "isolation", "cable"),
            ("triceps", "isolation", "cable"),
            ("abs", "isolation", "cable"),
            
                        
                    ],
                    "Day 2": [
            ("quads", "compound", "barbell"),
            ("quads", "compound", "machine"),
            ("quads", "compound", "dumbbell"),
            ("quads", "isolation", "machine"),
            ("abductor", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")            
                    ],
                    "Day 3": [
            ("back", "compound", "machine"),
            ("back", "compound", "barbell"),
            ("back", "isolation", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("biceps", "isolation", "cable"),
            ("lower_back", "isolation", "bodyweight"),
            ("abs", "isolation", "cable"),
            ("abs", "isolation", "bodyweight")
                    ],
                    "Day 4": [
            ("hamstring", "isolation", "dumbbell"),            
            ("hamstring", "compound", "barbell"),
            ("hamstring", "compound", "machine"),
            ("hamstring", "compound", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("glute", "isolation", "cable"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight"),
            ("abs", "isolation", "cable")
                    ],
                    "Day 5": [
            ("glute", "compound", "barbell"),            
            ("glute", "compound", "machine"),
            ("glute", "isolation", "cable"),
            ("glute", "isolation", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("glute", "compound", "barbell"),
            ("abductor", "isolation", "machine"),
            ("calf", "isolation", "machine"),
            ("abs", "isolation", "bodyweight")
                    ] 
                },
                # split 2
                {
                 "Day 1": [
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("back", "isolation", "cable"),
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "barbell"),
            ("triceps", "isolation", "dumbbell"),
            ("triceps", "isolation", "cable"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("quads", "compound", "machine"),
            ("quads", "compound", "barbell"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("adductor", "isolation", "machine"),
            ("calf", "isolation", "machine")           
                    ],
                    "Day 3": [
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder", "isolation", "dumbbell"),
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("lower_back", "isolation", "bodyweight"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "compound", "barbell"),
            ("glute", "compound", "machine"),
            ("glute", "isolation", "cable"),
            ("hamstring", "compound", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("glute", "isolation", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "isolation", "dumbbell"),
            ("abductor", "isolation", "machine"),
            ("calf", "isolation", "machine")
                    ],
                    "Day 5": [
            ("glute", "compound", "barbell"),
            ("quads", "compound", "dumbbell"),
            ("glute", "compound", "machine"),
            ("hamstring", "compound", "cable"),
            ("hamstring", "isolation", "machine"),
            ("glute", "isolation", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("hamstring", "isolation", "dumbbell"),
            ("abductor", "isolation", "machine"),
            ("calf", "isolation", "machine")
                    ]
                }
            ],
            "intermediate": [
                # split 1
                {
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("triceps", "isolation", "barbell", "fst7"),
        ("back", "isolation", "cable"),
        ("triceps", "isolation", "cable")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "pyramid_asc"),
        ("quads", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "dumbbell")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_asc"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine")
    ]
}
            ],
            "advanced": [
                # split 1
                {
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("triceps", "isolation", "barbell", "fst7"),
        ("back", "isolation", "cable"),
        ("triceps", "isolation", "cable")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine"),
        ("quads", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "cable", "pyramid_asc"),
        ("quads", "isolation", "cable", "superset"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "dumbbell")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "dumbbell", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("back", "compound", "machine", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_desc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "dumbbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_asc"),
        ("glute", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "barbell"),
        ("back", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "cable", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("quads", "compound", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("quads", "isolation", "machine", "pyramid_desc"),
        ("glute", "isolation", "cable", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7"),
        ("glute", "isolation", "dumbbell"),
        ("quads", "isolation", "cable")
    ],

    "Day 3": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("shoulder", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("back", "compound", "machine", "pyramid_asc"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "fst7"),
        ("back", "isolation", "machine"),
        ("biceps_b", "isolation", "dumbbell")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_desc"),
        ("glute", "compound", "barbell"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "cable", "superset"),
        ("glute", "isolation", "dumbbell"),
        ("hamstring", "isolation", "machine", "pyramid_asc"),
        ("glute", "isolation", "machine"),
        ("hamstring", "isolation", "machine")
    ],

    "Day 5": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine")
    ]
}
            ]
        }
    },

    "6": {
        "hypertrophy": {
            "beginner": [
                {
                     "Day 1": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "barbell"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "dumbbell"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("quads", "compound", "barbell"),
            ("quads", "compound", "machine"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("adductor", "isolation", "machine"),
            ("calf", "isolation", "machine")           
                    ],
                    "Day 3": [
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "compound", "barbell"),
            ("glute", "compound", "machine"),
            ("hamstring", "compound", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "isolation", "machine"),
            ("glute", "isolation", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("calf", "isolation", "machine")
                    ],
                    "Day 5": [
            ("back", "compound", "machine"),
            ("back", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_r", "isolation", "dumbbell"),
            ("biceps", "isolation", "cable"),
            ("biceps", "isolation", "barbell"),
            ("abs", "isolation", "cable")
                    ],
                    "Day 6": [
            ("glute", "compound", "barbell"),
            ("quads", "compound", "machine"),
            ("glute", "compound", "machine"),
            ("hamstring", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("glute", "isolation", "dumbbell"),
            ("calf", "isolation", "machine")

                    ]
                }
            ],
            "intermediate": [
                {
                    
    "Day 1": [
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("shoulder_l", "isolation", "cable", "fst7"),
        ("back", "isolation", "cable", "fst7")
    ],

    "Day 2": [
        ("quads", "compound", "barbell"),
        ("quads", "compound", "machine", "pyramid_asc"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "superset"),
        ("shoulder", "compound", "machine"),
        ("chest", "compound", "barbell", "superset"),
        ("chest", "compound", "dumbbell"),
        ("chest", "compound", "machine", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine"),
        ("chest", "isolation", "cable"),
        ("shoulder_f", "isolation", "dumbbell", "fst7"),
        ("chest", "isolation", "machine", "fst7")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable", "superset"),
        ("abs", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine", "fst7")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "superset"),
        ("back", "compound", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("biceps", "isolation", "machine", "fst7"),
        ("triceps", "isolation", "machine", "fst7")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "fst7")
    ] 
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "cable", "fst7"),
        ("shoulder_l", "isolation", "cable", "fst7")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("quads", "isolation", "cable", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("chest", "compound", "barbell", "pyramid_desc"),
        ("chest", "compound", "machine"),
        ("chest", "compound", "dumbbell", "superset"),
        ("shoulder_r", "isolation", "cable"),
        ("chest", "isolation", "machine", "fst7"),
        ("shoulder_l", "isolation", "cable"),
        ("triceps", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "machine", "superset"),
        ("abs", "isolation", "cable")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "superset"),
        ("biceps_b", "isolation", "dumbbell"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("back", "isolation", "cable", "fst7"),
        ("biceps", "isolation", "machine", "fst7"),
        ("triceps", "isolation", "machine", "fst7")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("back", "isolation", "cable", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_desc"),
        ("chest", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine", "superset"),
        ("chest", "compound", "machine"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine"),
        ("chest", "isolation", "cable"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable"),
        ("chest", "isolation", "machine")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "superset"),
        ("abs", "isolation", "bodyweight"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "machine", "fst7")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("biceps", "isolation", "machine"),
        ("triceps", "isolation", "machine")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine")
    ]
}



            ],
            "advanced": [
                {
                    
    "Day 1": [
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("shoulder_l", "isolation", "cable", "fst7"),
        ("back", "isolation", "cable", "fst7")
    ],

    "Day 2": [
        ("quads", "compound", "barbell"),
        ("quads", "compound", "machine", "pyramid_asc"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "superset"),
        ("shoulder", "compound", "machine"),
        ("chest", "compound", "barbell", "superset"),
        ("chest", "compound", "dumbbell"),
        ("chest", "compound", "machine", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine"),
        ("chest", "isolation", "cable"),
        ("shoulder_f", "isolation", "dumbbell", "fst7"),
        ("chest", "isolation", "machine", "fst7")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable", "superset"),
        ("abs", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine", "fst7")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "superset"),
        ("back", "compound", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("biceps", "isolation", "machine", "fst7"),
        ("triceps", "isolation", "machine", "fst7")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "fst7")
    ] 
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "cable", "fst7"),
        ("shoulder_l", "isolation", "cable", "fst7")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("quads", "isolation", "cable", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("chest", "compound", "barbell", "pyramid_desc"),
        ("chest", "compound", "machine"),
        ("chest", "compound", "dumbbell", "superset"),
        ("shoulder_r", "isolation", "cable"),
        ("chest", "isolation", "machine", "fst7"),
        ("shoulder_l", "isolation", "cable"),
        ("triceps", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "machine", "superset"),
        ("abs", "isolation", "cable")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "superset"),
        ("biceps_b", "isolation", "dumbbell"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("back", "isolation", "cable", "fst7"),
        ("biceps", "isolation", "machine", "fst7"),
        ("triceps", "isolation", "machine", "fst7")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("back", "isolation", "cable", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_desc"),
        ("chest", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine", "superset"),
        ("chest", "compound", "machine"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine"),
        ("chest", "isolation", "cable"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable"),
        ("chest", "isolation", "machine")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "superset"),
        ("abs", "isolation", "bodyweight"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "machine", "fst7")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("biceps", "isolation", "machine"),
        ("triceps", "isolation", "machine")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine")
    ]
}



            ]
        },
        "strength": {
            "beginner": [
                {
                     "Day 1": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "barbell"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "dumbbell"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("quads", "compound", "barbell"),
            ("quads", "compound", "machine"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("adductor", "isolation", "machine"),
            ("calf", "isolation", "machine")           
                    ],
                    "Day 3": [
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "compound", "barbell"),
            ("glute", "compound", "machine"),
            ("hamstring", "compound", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "isolation", "machine"),
            ("glute", "isolation", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("calf", "isolation", "machine")
                    ],
                    "Day 5": [
            ("back", "compound", "machine"),
            ("back", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_r", "isolation", "dumbbell"),
            ("biceps", "isolation", "cable"),
            ("biceps", "isolation", "barbell"),
            ("abs", "isolation", "cable")
                    ],
                    "Day 6": [
            ("glute", "compound", "barbell"),
            ("quads", "compound", "machine"),
            ("glute", "compound", "machine"),
            ("hamstring", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("glute", "isolation", "dumbbell"),
            ("calf", "isolation", "machine")

                    ]
                }
            ],
            "intermediate": [
                {
                    
    "Day 1": [
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("shoulder_l", "isolation", "cable", "fst7"),
        ("back", "isolation", "cable", "fst7")
    ],

    "Day 2": [
        ("quads", "compound", "barbell"),
        ("quads", "compound", "machine", "pyramid_asc"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "superset"),
        ("shoulder", "compound", "machine"),
        ("chest", "compound", "barbell", "superset"),
        ("chest", "compound", "dumbbell"),
        ("chest", "compound", "machine", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine"),
        ("chest", "isolation", "cable"),
        ("shoulder_f", "isolation", "dumbbell", "fst7"),
        ("chest", "isolation", "machine", "fst7")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable", "superset"),
        ("abs", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine", "fst7")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "superset"),
        ("back", "compound", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("biceps", "isolation", "machine", "fst7"),
        ("triceps", "isolation", "machine", "fst7")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "fst7")
    ] 
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "cable", "fst7"),
        ("shoulder_l", "isolation", "cable", "fst7")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("quads", "isolation", "cable", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("chest", "compound", "barbell", "pyramid_desc"),
        ("chest", "compound", "machine"),
        ("chest", "compound", "dumbbell", "superset"),
        ("shoulder_r", "isolation", "cable"),
        ("chest", "isolation", "machine", "fst7"),
        ("shoulder_l", "isolation", "cable"),
        ("triceps", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "machine", "superset"),
        ("abs", "isolation", "cable")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "superset"),
        ("biceps_b", "isolation", "dumbbell"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("back", "isolation", "cable", "fst7"),
        ("biceps", "isolation", "machine", "fst7"),
        ("triceps", "isolation", "machine", "fst7")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("back", "isolation", "cable", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_desc"),
        ("chest", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine", "superset"),
        ("chest", "compound", "machine"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine"),
        ("chest", "isolation", "cable"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable"),
        ("chest", "isolation", "machine")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "superset"),
        ("abs", "isolation", "bodyweight"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "machine", "fst7")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("biceps", "isolation", "machine"),
        ("triceps", "isolation", "machine")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine")
    ]
}



            ],
            "advanced": [
                {
                    
    "Day 1": [
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("shoulder_l", "isolation", "cable", "fst7"),
        ("back", "isolation", "cable", "fst7")
    ],

    "Day 2": [
        ("quads", "compound", "barbell"),
        ("quads", "compound", "machine", "pyramid_asc"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "superset"),
        ("shoulder", "compound", "machine"),
        ("chest", "compound", "barbell", "superset"),
        ("chest", "compound", "dumbbell"),
        ("chest", "compound", "machine", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine"),
        ("chest", "isolation", "cable"),
        ("shoulder_f", "isolation", "dumbbell", "fst7"),
        ("chest", "isolation", "machine", "fst7")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable", "superset"),
        ("abs", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine", "fst7")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "superset"),
        ("back", "compound", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("biceps", "isolation", "machine", "fst7"),
        ("triceps", "isolation", "machine", "fst7")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "fst7")
    ] 
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "cable", "fst7"),
        ("shoulder_l", "isolation", "cable", "fst7")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("quads", "isolation", "cable", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("chest", "compound", "barbell", "pyramid_desc"),
        ("chest", "compound", "machine"),
        ("chest", "compound", "dumbbell", "superset"),
        ("shoulder_r", "isolation", "cable"),
        ("chest", "isolation", "machine", "fst7"),
        ("shoulder_l", "isolation", "cable"),
        ("triceps", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "machine", "superset"),
        ("abs", "isolation", "cable")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "superset"),
        ("biceps_b", "isolation", "dumbbell"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("back", "isolation", "cable", "fst7"),
        ("biceps", "isolation", "machine", "fst7"),
        ("triceps", "isolation", "machine", "fst7")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("back", "isolation", "cable", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_desc"),
        ("chest", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine", "superset"),
        ("chest", "compound", "machine"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine"),
        ("chest", "isolation", "cable"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable"),
        ("chest", "isolation", "machine")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "superset"),
        ("abs", "isolation", "bodyweight"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "machine", "fst7")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("biceps", "isolation", "machine"),
        ("triceps", "isolation", "machine")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine")
    ]
}



            ]
        },
        "fat_loss": {
            "beginner": [
                {
                     "Day 1": [
            ("back", "compound", "barbell"),
            ("back", "compound", "machine"),
            ("back", "compound", "cable"),
            ("shoulder_l", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell"),
            ("chest", "compound", "barbell"),
            ("biceps", "isolation", "barbell"),
            ("biceps", "isolation", "dumbbell"),
            ("abs", "isolation", "cable")
                        
                    ],
                    "Day 2": [
            ("quads", "compound", "barbell"),
            ("quads", "compound", "machine"),
            ("quads", "isolation", "machine"),
            ("quads", "compound", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("adductor", "isolation", "machine"),
            ("calf", "isolation", "machine")           
                    ],
                    "Day 3": [
            ("shoulder", "compound", "machine"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_f", "isolation", "dumbbell"),
            ("shoulder_r", "isolation", "cable"),
            ("chest", "compound", "dumbbell"),
            ("triceps", "isolation", "cable"),
            ("triceps", "isolation", "dumbbell"),
            ("abs", "isolation", "bodyweight")
                    ],
                      "Day 4": [
            ("hamstring", "compound", "barbell"),
            ("glute", "compound", "machine"),
            ("hamstring", "compound", "dumbbell"),
            ("hamstring", "isolation", "machine"),
            ("hamstring", "isolation", "machine"),
            ("glute", "isolation", "dumbbell"),
            ("glute", "isolation", "cable"),
            ("glute", "isolation", "cable"),
            ("abductor", "isolation", "machine"),
            ("calf", "isolation", "machine")
                    ],
                    "Day 5": [
            ("back", "compound", "machine"),
            ("back", "isolation", "cable"),
            ("shoulder", "isolation", "dumbbell"),
            ("shoulder_l", "isolation", "cable"),
            ("shoulder_r", "isolation", "dumbbell"),
            ("biceps", "isolation", "cable"),
            ("biceps", "isolation", "barbell"),
            ("abs", "isolation", "cable")
                    ],
                    "Day 6": [
            ("glute", "compound", "barbell"),
            ("quads", "compound", "machine"),
            ("glute", "compound", "machine"),
            ("hamstring", "isolation", "machine"),
            ("abductor", "isolation", "cable"),
            ("glute", "isolation", "dumbbell"),
            ("calf", "isolation", "machine")

                    ]
                }
            ],
            "intermediate": [
                {
                    
    "Day 1": [
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("shoulder_l", "isolation", "cable", "fst7"),
        ("back", "isolation", "cable", "fst7")
    ],

    "Day 2": [
        ("quads", "compound", "barbell"),
        ("quads", "compound", "machine", "pyramid_asc"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "superset"),
        ("shoulder", "compound", "machine"),
        ("chest", "compound", "barbell", "superset"),
        ("chest", "compound", "dumbbell"),
        ("chest", "compound", "machine", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine"),
        ("chest", "isolation", "cable"),
        ("shoulder_f", "isolation", "dumbbell", "fst7"),
        ("chest", "isolation", "machine", "fst7")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable", "superset"),
        ("abs", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine", "fst7")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "superset"),
        ("back", "compound", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("biceps", "isolation", "machine", "fst7"),
        ("triceps", "isolation", "machine", "fst7")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "fst7")
    ] 
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "cable", "fst7"),
        ("shoulder_l", "isolation", "cable", "fst7")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("quads", "isolation", "cable", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("chest", "compound", "barbell", "pyramid_desc"),
        ("chest", "compound", "machine"),
        ("chest", "compound", "dumbbell", "superset"),
        ("shoulder_r", "isolation", "cable"),
        ("chest", "isolation", "machine", "fst7"),
        ("shoulder_l", "isolation", "cable"),
        ("triceps", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "machine", "superset"),
        ("abs", "isolation", "cable")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "superset"),
        ("biceps_b", "isolation", "dumbbell"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("back", "isolation", "cable", "fst7"),
        ("biceps", "isolation", "machine", "fst7"),
        ("triceps", "isolation", "machine", "fst7")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("back", "isolation", "cable", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_desc"),
        ("chest", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine", "superset"),
        ("chest", "compound", "machine"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine"),
        ("chest", "isolation", "cable"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable"),
        ("chest", "isolation", "machine")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "superset"),
        ("abs", "isolation", "bodyweight"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "machine", "fst7")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("biceps", "isolation", "machine"),
        ("triceps", "isolation", "machine")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine")
    ]
}



            ],
            "advanced": [
                {
                    
    "Day 1": [
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "barbell"),
        ("back", "compound", "cable", "superset"),
        ("shoulder", "compound", "dumbbell"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine", "superset"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("shoulder_l", "isolation", "cable", "fst7"),
        ("back", "isolation", "cable", "fst7")
    ],

    "Day 2": [
        ("quads", "compound", "barbell"),
        ("quads", "compound", "machine", "pyramid_asc"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "superset"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "superset"),
        ("shoulder", "compound", "machine"),
        ("chest", "compound", "barbell", "superset"),
        ("chest", "compound", "dumbbell"),
        ("chest", "compound", "machine", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine"),
        ("chest", "isolation", "cable"),
        ("shoulder_f", "isolation", "dumbbell", "fst7"),
        ("chest", "isolation", "machine", "fst7")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable", "superset"),
        ("abs", "isolation", "machine"),
        ("abs", "isolation", "bodyweight"),
        ("hamstring", "isolation", "machine", "fst7"),
        ("glute", "isolation", "machine", "fst7")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "superset"),
        ("back", "compound", "machine"),
        ("biceps", "isolation", "barbell", "superset"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("biceps", "isolation", "machine", "fst7"),
        ("triceps", "isolation", "machine", "fst7")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "fst7")
    ] 
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_asc"),
        ("back", "compound", "machine"),
        ("back", "compound", "cable", "superset"),
        ("back", "compound", "machine"),
        ("shoulder", "compound", "dumbbell", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "cable", "fst7"),
        ("shoulder_l", "isolation", "cable", "fst7")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_desc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("quads", "isolation", "cable", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine", "superset"),
        ("shoulder_l", "isolation", "cable"),
        ("chest", "compound", "barbell", "pyramid_desc"),
        ("chest", "compound", "machine"),
        ("chest", "compound", "dumbbell", "superset"),
        ("shoulder_r", "isolation", "cable"),
        ("chest", "isolation", "machine", "fst7"),
        ("shoulder_l", "isolation", "cable"),
        ("triceps", "isolation", "cable")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("hamstring", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine"),
        ("glute", "isolation", "cable", "fst7"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "bodyweight"),
        ("abs", "isolation", "machine", "superset"),
        ("abs", "isolation", "cable")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable", "superset"),
        ("biceps_b", "isolation", "dumbbell"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("back", "isolation", "cable", "fst7"),
        ("biceps", "isolation", "machine", "fst7"),
        ("triceps", "isolation", "machine", "fst7")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7")
    ]
},
{
    "Day 1": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("back", "compound", "cable"),
        ("shoulder", "compound", "barbell", "pyramid_asc"),
        ("shoulder_l", "isolation", "cable", "superset"),
        ("shoulder_r", "isolation", "machine"),
        ("shoulder_f", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("back", "isolation", "cable", "pyramid_desc"),
        ("shoulder_l", "isolation", "cable")
    ],

    "Day 2": [
        ("quads", "compound", "barbell", "pyramid_asc"),
        ("quads", "compound", "machine", "superset"),
        ("quads", "isolation", "machine"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("calf", "isolation", "machine", "pyramid_desc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine", "fst7")
    ],

    "Day 3": [
        ("shoulder", "compound", "barbell", "pyramid_desc"),
        ("chest", "compound", "barbell", "pyramid_asc"),
        ("shoulder", "compound", "machine", "superset"),
        ("chest", "compound", "machine"),
        ("shoulder_l", "isolation", "cable"),
        ("shoulder_r", "isolation", "machine"),
        ("chest", "isolation", "cable"),
        ("triceps", "isolation", "barbell"),
        ("triceps", "isolation", "cable"),
        ("chest", "isolation", "machine")
    ],

    "Day 4": [
        ("hamstring", "compound", "barbell", "pyramid_asc"),
        ("hamstring", "isolation", "machine", "superset"),
        ("glute", "compound", "barbell"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("abs", "isolation", "cable"),
        ("abs", "isolation", "machine", "superset"),
        ("abs", "isolation", "bodyweight"),
        ("hamstring", "isolation", "machine"),
        ("glute", "isolation", "machine", "fst7")
    ],

    "Day 5": [
        ("back", "compound", "barbell", "pyramid_desc"),
        ("back", "compound", "machine", "superset"),
        ("biceps", "isolation", "barbell"),
        ("biceps", "isolation", "cable"),
        ("triceps", "isolation", "barbell", "superset"),
        ("triceps", "isolation", "cable"),
        ("biceps_b", "isolation", "dumbbell"),
        ("back", "isolation", "machine"),
        ("biceps", "isolation", "machine"),
        ("triceps", "isolation", "machine")
    ],

    "Day 6": [
        ("glute", "compound", "barbell", "pyramid_asc"),
        ("glute", "compound", "barbell", "pyramid_desc"),
        ("glute", "isolation", "machine", "superset"),
        ("glute", "isolation", "cable"),
        ("glute", "isolation", "dumbbell"),
        ("glute", "isolation", "machine", "fst7"),
        ("calf", "isolation", "machine", "pyramid_asc"),
        ("calf", "isolation", "machine"),
        ("calf", "isolation", "machine", "superset"),
        ("calf", "isolation", "machine")
    ]
}



            ]
        }
    }
}
      # more variations...
