from validators import is_valid_email, is_valid_phone


print(is_valid_email("john@gmail.com"))
print(is_valid_email("john@gmail"))
print(is_valid_email("john.com"))

print(is_valid_phone("9876543210"))
print(is_valid_phone("1234567890"))
print(is_valid_phone("987654321"))