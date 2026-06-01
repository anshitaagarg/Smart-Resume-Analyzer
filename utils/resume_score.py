def calculate_resume_score(
    name,
    email,
    phone,
    skills,
    education,
    experience
):

    score = 0

    if name != "Not Found":
        score += 15

    if email != "Not Found":
        score += 15

    if phone != "Not Found":
        score += 10

    if len(skills) > 0:
        score += 25

    if len(education) > 0:
        score += 15

    if len(experience) > 0:
        score += 20

    return score