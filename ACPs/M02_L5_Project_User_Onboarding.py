# Module 2 Lesson 5: After-Class Project
# Project Name: User Registration Integrity and Validation Enforcer

class OnboardingValidator:
    def validate_profile_inputs(self, username, passphrase, email_address):
        if len(username) < 5 or " " in username:
            return "Rejected: Username profile layout syntax violation."
        if len(passphrase) < 8 or not any(char.isdigit() for char in passphrase):
            return "Rejected: Complex password rules verification error."
        if "@" not in email_address or "." not in email_address:
            return "Rejected: Malformed email routing parameters."
        return "Approved: Core onboarding profile verified successfully."

if __name__ == "__main__":
    validator = OnboardingValidator()
    print(validator.validate_profile_inputs("instructor_ioi", "SecurePass2026", "ioi@algorithms.edu"))