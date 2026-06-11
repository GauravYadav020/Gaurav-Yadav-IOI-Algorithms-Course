# Module 5 Lesson 3: After-Class Project
# Project Name: Enterprise Database Ingestion Pipeline String Data Sanitizer

import re

class DatabaseIngestionSanitizer:
    def strip_malicious_characters(self, raw_input_string):
        # Strip potential script injections or illegal database character codes
        sanitized = re.sub(r'[;<>]', '', raw_input_string)
        return sanitized.strip()

    def standardize_phone_routing(self, raw_phone_string):
        digits_only = re.sub(r'\D', '', raw_phone_string)
        if len(digits_only) == 10:
            return f"+1-{digits_only[:3]}-{digits_only[3:6]}-{digits_only[6:]}"
        return digits_only

if __name__ == "__main__":
    sanitizer = DatabaseIngestionSanitizer()
    print(f"Sanitized Entry: {sanitizer.strip_malicious_characters('SELECT * FROM Users; <script>')}")
    print(f"Formatted Route: {sanitizer.standardize_phone_routing('(555) 019-2834')}")