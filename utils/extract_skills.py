import pandas as pd

def extract_skills(text):
    skills_df = pd.read_csv(
        "data/skills.csv",
        header=None
    )

    skills_list = skills_df[0].tolist()
    found_skills = []
    text_lower = text.lower()
    for skill in skills_list:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return sorted(list(set(found_skills)))