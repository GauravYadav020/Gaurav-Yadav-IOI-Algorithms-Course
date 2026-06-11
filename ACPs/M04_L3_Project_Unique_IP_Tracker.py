# Module 4 Lesson 3: After-Class Project
# Project Name: Real-Time High-Speed Fraud Security Unique IP Set Monitor

class SecurityIPMonitor:
    def __init__(self):
        self.unique_ip_registry = set()

    def process_packet_ip(self, incoming_source_ip):
        if incoming_source_ip in self.unique_ip_registry:
            return f"IP [{incoming_source_ip}] Verified: Repeat Network Visitor Node."
        else:
            self.unique_ip_registry.add(incoming_source_ip)
            return f"IP [{incoming_source_ip}] Logged: New Global Connection Detected."

if __name__ == "__main__":
    monitor = SecurityIPMonitor()
    print(monitor.process_packet_ip("192.168.1.50"))
    print(monitor.process_packet_ip("192.168.1.50"))