import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters (a-z).")

    # Uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters (A-Z).")

    # Digits
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add digits (0-9).")

    # Special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters (!@#$%^&* etc).")

    # Final verdict
    if score == 5:
        strength = "Very strong ✅"
    elif score >= 3:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    return strength, feedback

if __name__ == "__main__":
    password = input("Enter a password to check: ")
    strength, suggestions = check_password_strength(password)

    print(f"\nStrength: {strength}")
    if suggestions:
        print("Suggestions:")
        for suggestion in suggestions:
            print(" -", suggestion)
