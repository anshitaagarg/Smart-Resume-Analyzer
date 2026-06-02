import re

def extract_email(text):
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    emails = re.findall(email_pattern, text)
    if emails:
        return emails[0]
    
    return "Not Found"

import re

def extract_phone(text):

    pattern = r'(\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4})'

    match = re.search(pattern, text)

    if match:
        return match.group(0)
    return "Not Found"