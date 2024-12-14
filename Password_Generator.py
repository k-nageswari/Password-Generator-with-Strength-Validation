import random
import string

def generatePassword(pwlength):

    alphabet = string.ascii_lowercase  # Lowercase letters
    special_chars = string.punctuation  # Special characters
    passwords = []

    for length in pwlength:
        password = ""
        for _ in range(length):
            # Randomly choose from lowercase, uppercase, digits, or special chars
            choice = random.choice([alphabet, string.ascii_uppercase, string.digits, special_chars])
            password += random.choice(choice)

        # Ensure the password contains at least one of each type (lower, upper, digit, special char)
        password = ensurePasswordStrength(password, alphabet, string.ascii_uppercase, string.digits, special_chars)
        
        passwords.append(password)
    
    return passwords

def ensurePasswordStrength(password, lower, upper, digits, specials):
    # Ensure at least one lowercase letter
    if not any(c in lower for c in password):
        password += random.choice(lower)
    
    # Ensure at least one uppercase letter
    if not any(c in upper for c in password):
        password += random.choice(upper)

    # Ensure at least one digit
    if not any(c in digits for c in password):
        password += random.choice(digits)

    # Ensure at least one special character
    if not any(c in specials for c in password):
        password += random.choice(specials)

    # Shuffle the password to randomize the order
    password = ''.join(random.sample(password, len(password)))
    
    return password

def isStrongPassword(password):
    # Check if the password is strong:
    # - At least 8 characters long
    # - Contains uppercase, lowercase, digit, and special character
    if len(password) < 8:
        return "Weak"
    if not any(c.islower() for c in password):
        return "Weak"
    if not any(c.isupper() for c in password):
        return "Weak"
    if not any(c.isdigit() for c in password):
        return "Weak"
    if not any(c in string.punctuation for c in password):
        return "Weak"
    
    return "Strong"

def main():
    numPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(numPasswords) + " passwords")
    
    passwordLengths = []

    print("Minimum length of password should be 8")

    for i in range(numPasswords):
        length = int(input(f"Enter the length of Password #{i+1}: "))
        if length < 8:
            length = 8  # Enforce minimum length of 8
        passwordLengths.append(length)
    
    Passwords = generatePassword(passwordLengths)

    for i in range(numPasswords):
        password = Passwords[i]
        strength = isStrongPassword(password)
        print(f"Password #{i+1}: {password} (Strength: {strength})")

main()
