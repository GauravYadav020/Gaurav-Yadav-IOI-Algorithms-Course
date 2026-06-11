# Module 8 Lesson 1: After-Class Project
# Project Name: Infrastructure Disk System Log Writer Exception Safeguard

import os

class DiskLogPersistenceManager:
    def __init__(self, logging_filepath="sys_infrastructure_trace.log"):
        self.target_path = logging_filepath

    def commit_log_event(self, log_message_string):
        try:
            # Use contextual safe context file streams operators handles
            with open(self.target_path, "a", encoding="utf-8") as stream_handle:
                stream_handle.write(f"[LOG_EVENT] {log_message_string}\n")
            return True
        except IOError as disk_exception:
            print(f"🚨 Low-Level OS Disk Output IO Exception Handled: {disk_exception}")
            return False

if __name__ == "__main__":
    writer = DiskLogPersistenceManager()
    if writer.commit_log_event("Kernel buffer pool verified steady state."):
        print("Log entry persisted safely onto local virtual storage directory.")
        if os.path.exists("sys_infrastructure_trace.log"): os.remove("sys_infrastructure_trace.log")