# Module 2 Lesson 1: After-Class Project
# Project Name: High-Performance Network Logs Parser and Threat Evaluator

class ServerLogAuditor:
    def __init__(self):
        self.threat_signatures = ["401_UNAUTHORIZED", "500_INTERNAL_FAIL", "DROP_WALL"]

    def audit_stream_line(self, raw_log_line):
        flagged = False
        for signature in self.threat_signatures:
            if signature in raw_log_line:
                flagged = True
                break
        return {"RawLine": raw_log_line.strip(), "SecurityAlertFlag": flagged}

if __name__ == "__main__":
    auditor = ServerLogAuditor()
    sample_log = "SYS_LOG_ENV: 2026-04-11 10:22:15 ERROR 401_UNAUTHORIZED malicious packet intercept"
    print(f"Log Security Review Assessment: {auditor.audit_stream_line(sample_log)}")