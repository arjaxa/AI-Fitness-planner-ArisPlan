# compatibility function

def can_pair(ex1, ex2):
    # avoid overlapping primary muscles
    if ex1["primary"] == ex2["primary"]:
        return False

    # avoid strong secondary overlap
    if ex1["primary"] in ex2["secondary"]:
        return False
    if ex2["primary"] in ex1["secondary"]:
        return False

    return True


# superset scoring

def pairing_score(ex1, ex2):
    score = 0

    # prefer different muscle groups
    if ex1["primary"] != ex2["primary"]:
        score += 2

    # avoid secondary overlap
    overlap = set(ex1["secondary"]) & set(ex2["secondary"])
    score -= len(overlap)

    # too much fatigue together = bad
    if ex1["fatigue"] + ex2["fatigue"] > 4:
        score -= 2

    return score

