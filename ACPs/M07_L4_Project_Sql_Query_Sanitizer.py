# Module 7 Lesson 4: After-Class Project
# Project Name: Secure Database Shield Ingestion Pipeline SQL Injection Scanner

import re

class DatabaseShieldScanner:
    def __init__(self):
        self.malicious_sql_patterns = [
            r'UNION\s+SELECT',
            r'OR\s+\d+=\d+',
            r'--'
        ]

    def scan_query_payload(self, inbound_user_query_string):
        for pattern in self.malicious_sql_patterns:
            if re.search(pattern, inbound_user_query_string, re.IGNORECASE):
                return "CRITICAL_THREAT_INTERCEPT: Malicious code injection vector detected."
        return "QUERY_CLEAN_APPROVED"

if __name__ == "__main__":
    shield = DatabaseShieldScanner()
    print(shield.scan_query_payload("SELECT * FROM Accounts WHERE id = 101 OR 1=1"))
    print(shield.scan_query_payload("SELECT * FROM Products WHERE category = 'books'"))