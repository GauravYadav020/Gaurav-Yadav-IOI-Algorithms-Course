# Module 1 Lesson 6: After-Class Project
# Project Name: Micro-Kernel Device System Health Monitor

class KernelSystemMonitor:
    def __init__(self):
        self.telemetry_history = []

    def log_telemetry(self, cpu_load, memory_leak_bytes, core_temperature):
        status = "HEALTHY"
        if cpu_load > 92.5 or core_temperature > 85.0:
            status = "CRITICAL_OVERHEATING_HAZARD"
        
        self.telemetry_history.append({
            "CPU": cpu_load, "Mem": memory_leak_bytes, "Temp": core_temperature, "Status": status
        })
        return status

if __name__ == "__main__":
    monitor = KernelSystemMonitor()
    print(f"System Operational State Summary: {monitor.log_telemetry(95.0, 1048576, 88.3)}")