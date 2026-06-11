# Module 7 Lesson 5: After-Class Project
# Project Name: Healthcare Data Pipeline HIPAA PII Masking Anonymizer

import re

class PatientDataAnonymizer:
    def mask_sensitive_pii(self, messy_clinical_text):
        # Mask United States SSN configurations pattern schemas
        scrubbed = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', "[REDACTED_SSN]", messy_clinical_text)
        # Mask localized phone numbers mapping dimensions
        fully_anonymized = re.sub(r'\b\d{3}-\d{3}-\d{4}\b', "[REDACTED_PHONE]", scrubbed)
        return fully_anonymized

if __name__ == "__main__":
    anonymizer = PatientDataAnonymizer()
    notes = "Patient records verified by SSN: 999-12-3456. Contact clinical relative via 555-019-2834."
    print(anonymizer.mask_sensitive_pii(notes))