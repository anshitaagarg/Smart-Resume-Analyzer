def normalize_header(text):
    return text.replace(" ", "").upper()

def extract_experience(text):

    lines = text.split('\n')
    experience_info = []
    capture = False

    experience_headers = [
        "EXPERIENCE",
        "WORKEXPERIENCE",
        "PROFESSIONALEXPERIENCE",
        "EMPLOYMENT"
    ]

    stop_headers = [
        "PROJECTS",
        "TECHNICALSKILLS",
        "SKILLS",
        "EDUCATION",
        "CERTIFICATIONS",
        "SOFTWAREENGINEERINGPROJECTS",
        "ACHIEVEMENTS"
    ]

    for line in lines:

        clean_line = normalize_header(line.strip())

        if clean_line in experience_headers:
            capture = True
            continue

        if capture and clean_line in stop_headers:
            break

        if capture and line.strip():
            experience_info.append(line.strip())

    return experience_info