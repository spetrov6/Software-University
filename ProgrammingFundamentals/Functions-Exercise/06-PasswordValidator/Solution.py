# "Password must be between 6 and 10 characters"
# "Password must consist only of letters and digits"
# "Password must have at least 2 digits"
def password_validator(password):
    def length_check(length_password):
        if 6 <= len(length_password) <= 10:
            return True
        else:
            return False
    def letter_digits_check(password_check):
        for i in password_check:
            if i.isdigit() or 97 <= ord(i) <=122:
                continue
            else:
                return False
        return True
    def password_digit_count(digit_count):
        count = 0
        for i in password:
            if i.isdigit():
                count += 1
        if count < 2:
            return False
        else:
            return True
    if not length_check(password):
        print("Password must be between 6 and 10 characters")
    if not letter_digits_check(password):
        print("Password must consist only of letters and digits")
    if not password_digit_count(password):
        print("Password must have at least 2 digits")
    if length_check(password) == True and letter_digits_check(password) == True and password_digit_count(password) == True:
        print("Password is valid")
password_validator(input().lower())