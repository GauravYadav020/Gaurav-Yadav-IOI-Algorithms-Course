# Module 7 Lesson 2: After-Class Project
# Project Name: RegEx Infrastructure Threat Intelligence Telemetry Tokenizer

import re

class ServerTelemetryExtractor:
    def __init__(self):
        # Captures exact IPv4 structures and error tags inside server trace arrays
        self.extractor_schema = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?\[(?P<tag>ERROR|WARN)\]\s(?P<msg>.*)'

    def parse_trace_line(self, raw_unstructured_log_line):
        match = re.search(self.extractor_schema, raw_unstructured_log_line)
        if match:
            return match.groupdict()
        return None

if __name__ == "__main__":
    extractor = ServerTelemetryExtractor()
    trace = "192.168.4.12 - - [ERROR] Memory segmentation overflow detected at register 0x4F"
    print(f"Extracted Structured Context: {extractor.parse_trace_line(trace)}")