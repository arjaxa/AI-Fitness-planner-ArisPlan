def should_superset(ex1, ex2) -> bool:
    return False

def should_triset(ex1, ex2, ex3) -> bool:
    return False

def compatibility_score(ex1, ex2):

    score = 100

    # same primary muscle = bad
    if ex1["primary"] == ex2["primary"]:
        score -= 50

    # secondary overlap = medium bad
    if ex1["secondary"] in ex2["secondary"]:
        score -= 20

    # compound + compound = fatigue
    if ex1["type"] == "compound" and ex2["type"] == "compound":
        score -= 15

    # equipment clash
    if ex1["equipment"] == ex2["equipment"]:
        score -= 10

    return score


def should_superset(ex1, ex2):
    return compatibility_score(ex1, ex2) >= 70
