import re

def extract_email(text):
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    emails = re.findall(email_pattern, text)
    if emails:
        return emails[0]
    
    return "Not Found"

def extract_phone(text):
    phone_pattern = r'(\+?\d{1,3}[\s-]?)?(\(?\d{3}\)?[\s-]?)?[\d\s-]{10,15}'
    phones = re.findall(phone_pattern, text)
    if phones:
        for phone in phones:
            phone_number = ''.join(phone)
            digits = re.sub(r'\D', '', phone_number)
            if len(digits) >= 10:
                return phone_number

    return "Not Found"