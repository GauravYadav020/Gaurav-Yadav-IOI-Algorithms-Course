# Module 8 Lesson 6: After-Class Project
# Project Name: Infrastructure Security Scrubber and File System Directory Auditor

class LogFileScrubberEngine:
    def sanitize_active_log_in_place(self, file_lines_input_array):
        scrubbed_clean_lines = []
        lines_removed_counter = 0
        
        for line in file_lines_input_array:
            # Filter out lines flagged with security debug noise elements completely
            if "DEBUG_VERBOSE_DUMP" in line:
                lines_removed_counter += 1
            else:
                scrubbed_clean_lines.append(line)
                
        return {"CleanLines": scrubbed_clean_lines, "TotalScrubbedCount": lines_removed_counter}

if __name__ == "__main__":
    engine = LogFileScrubberEngine()
    dirty_logs = [
        "INFO: Initialization sequence started.",
        "DEBUG_VERBOSE_DUMP: Register hex state 0x00F43A",
        "WARN: Connection timeout threshold approached."
    ]
    print(f"Scrubber Run Complete Analysis: {engine.sanitize_active_log_in_place(dirty_logs)}")