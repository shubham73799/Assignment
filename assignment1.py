def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return False

    # Uppercase check
    has_upper = False
    for ch in password:
        if ch.isupper():
            has_upper = True
            break

    # Lowercase check
    has_lower = False
    for ch in password:
        if ch.islower():
            has_lower = True
            break

    # Digit check
    has_digit = False
    for ch in password:
        if ch.isdigit():
            has_digit = True
            break

    # Special character check
    special_characters = "!@#$%^&*()-_=+[]{};:,<.>/?"
    has_special = False
    for ch in password:
        if ch in special_characters:
            has_special = True
            break

    # Final result
    if has_upper and has_lower and has_digit and has_special:
        return True
    else:
        return False


# Main program
password = input("Enter your password: ")

if check_password_strength(password):
    print("Your password is strong.")
else:
    print("Weak password. Please include:")
    print("- At least 8 characters")
    print("- Uppercase and lowercase letters")
    print("- At least one number")
    print("- At least one special character")