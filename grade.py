def letter_grade(score):
    if score <o or score > 100:
        raise ValueError("Score must be 0-100")
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"