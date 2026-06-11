# Module 5 Lesson 6: After-Class Project
# Project Name: Real-Time Network Telemetry Threshold Event Boundary Trigger

class SystemEventTriggerEngine:
    def __init__(self, high_cpu_boundary=90.0, high_latency_boundary=150.0):
        self.cpu_limit = high_cpu_boundary
        self.latency_limit = high_latency_boundary

    def evaluate_telemetry_metrics_matrix(self, current_cpu, current_latency):
        active_alerts = []
        if current_cpu >= self.cpu_limit:
            active_alerts.append("ALERT_CPU_RESOURCE_SATURATION_CRITICAL")
        if current_latency >= self.latency_limit:
            active_alerts.append("ALERT_NETWORK_LATENCY_DEGRADATION_WARNING")
            
        return active_alerts if active_alerts else ["METRICS_HEALTHY_STEADY_STATE"]

if __name__ == "__main__":
    trigger = SystemEventTriggerEngine()
    print(f"Telemetry Status Event Output Log: {trigger.evaluate_telemetry_metrics_matrix(94.2, 85.0)}")