def extract_name(text):

    lines = text.split('\n')

    blacklist = [
        "resume",
        "sample",
        "career summary",
        "experience",
        "education",
        "skills"
    ]

    for line in lines[:10]:

        line = line.strip()

        if not line:
            continue

        if '@' in line:
            continue

        if any(char.isdigit() for char in line):
            continue

        lower_line = line.lower()

        if any(word in lower_line for word in blacklist):
            continue

        words = line.split()

        if 2 <= len(words) <= 4:
            return line

    return "Not Found"