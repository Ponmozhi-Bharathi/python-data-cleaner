import re

def is_valid_name(name):
    pattern = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
    return re.match(pattern, name) is not None


def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def is_valid_phone(phone):
    pattern = r"^[6-9]\d{9}$"
    return re.match(pattern, phone) is not None