def normalize_header(text):
    return text.replace(" ", "").upper()

def extract_education(text):

    lines = text.split('\n')

    education_keywords = [
        "university",
        "University",
        "college",
        "bachelor",
        "Master",
        "degree",
        "phd",
        "doctorate",
        "cgpa",
        "gpa",
        "BS",
        "MS",
        "B.Tech",
        "M.Tech",
        "B.E",
        "M.E",
        "B.Sc",
        "M.Sc",
        "BA",
        "MA",
        "BBA",
        "BS",
    ]

    education_info = []

    for i, line in enumerate(lines):

        lower_line = line.lower()

        if any(keyword in lower_line for keyword in education_keywords):

            education_info.append(line.strip())

            # Capture next 2 lines
            for j in range(1, 3):

                if i + j < len(lines):

                    next_line = lines[i + j].strip()

                    if next_line:
                        education_info.append(next_line)

            break

    return education_info