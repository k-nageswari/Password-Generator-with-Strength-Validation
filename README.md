# **Password Generator with Strength Validation**

This repository contains a Python-based password generator that generates strong, random passwords based on specified criteria. The program generates passwords with a mix of lowercase letters, uppercase letters, digits, and special characters. Additionally, it checks the strength of each password to ensure it meets security standards.

## **Features**

- **Generates random passwords** with a combination of:
  - **Lowercase letters** (`a-z`)
  - **Uppercase letters** (`A-Z`)
  - **Digits** (`0-9`)
  - **Special characters** (`@`, `#`, `!`, `$`, `%`, etc.)
  
- Ensures each password contains at least **one of each type**: lowercase, uppercase, digit, and special character.
- **Checks password strength** to ensure:
  - Minimum length of **8 characters**
  - Contains at least **one uppercase letter**
  - Contains at least **one lowercase letter**
  - Contains at least **one digit**
  - Contains at least **one special character**
- Suggests whether the password is **Strong** or **Weak** based on these criteria.


### **Example Usage:**

```bash
How many passwords do you want to generate? 3
Generating 3 passwords
Minimum length of password should be 8
Enter the length of Password #1: 8
Enter the length of Password #2: 12
Enter the length of Password #3: 10
Password #1: qweU8&!r (Strength: Strong)
Password #2: @Z3hV1%fP8gY (Strength: Strong)
Password #3: Gk5*teLn&z (Strength: Strong)
