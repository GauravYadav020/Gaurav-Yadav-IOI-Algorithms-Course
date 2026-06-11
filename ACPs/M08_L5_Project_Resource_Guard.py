# Module 8 Lesson 5: After-Class Project
# Project Name: Virtual System Hardware Connection Handler Context Guard

class NetworkSocketResourceGuard:
    def __init__(self, hardware_socket_address):
        self.address = hardware_socket_address
        self.operational_state = "CLOSED"

    def __enter__(self):
        self.operational_state = "ESTABLISHED_ACTIVE"
        print(f" -> System Hardware Port Socket Connection locked open at channel address: {self.address}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.operational_state = "TERMINATED_CLEAN"
        print(" -> Socket Resource Guard intercept context executed: Connection memory registers flushed cleanly.")
        return True # Suppress internal loop exceptions to protect engine state stability

if __name__ == "__main__":
    print("Initializing safe system hardware socket contexts execution block:")
    with NetworkSocketResourceGuard("192.168.10.45:9000") as socket_channel:
        print(f"    Inside execution scope block context. State flag is: {socket_channel.operational_state}")
        # Intentional error generation to prove resource allocation flush resilience triggers safely
        calc_fault = 10 / 0