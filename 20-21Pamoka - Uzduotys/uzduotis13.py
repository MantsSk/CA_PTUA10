class PasswordChecker:
    def check_strength(self, password):
        length_criteria = len(password) >= 8
        uppercase_criteria = any(char.isupper() for char in password)
        lowercase_criteria = any(char.islower() for char in password)
        digit_criteria = any(char.isdigit() for char in password)
        special_char_criteria = any(not char.isalnum() for char in password)

        if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
            return "Strong"
        elif length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria:
            return "Moderate"
        elif length_criteria and (uppercase_criteria or lowercase_criteria) and digit_criteria:
            return "Weak"
        else:
            return "Very Weak"


password = input("Enter your password: ")
password_checker = PasswordChecker()
strength = password_checker.check_strength(password)

print(f'Password strength: {strength}')


