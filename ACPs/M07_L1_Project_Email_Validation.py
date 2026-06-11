# Module 7 Lesson 1: After-Class Project
# Project Name: RegEx Corporate Email Verification & Router Pre-Processor

import re

class CorporateEmailScrubber:
    def __init__(self):
        # Strict validation matching company structural format schemas
        self.regex_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'

    def audit_address_syntax(self, candidate_email_string):
        if re.match(self.regex_pattern, candidate_email_string):
            domain_routing_chunk = candidate_email_string.split("@")[1]
            return {"Status": "VALID_SYNTAX", "RoutingDomain": domain_routing_chunk}
        return {"Status": "INVALID_SYNTAX_MALFORMED", "RoutingDomain": None}

if __name__ == "__main__":
    scrubber = CorporateEmailScrubber()
    print(scrubber.audit_address_syntax("instructor.python@ioi-algorithms.edu"))
    print(scrubber.audit_address_syntax("malformed_email@@com"))