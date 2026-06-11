# Module 2 Lesson 4: After-Class Project
# Project Name: Automated HVAC Climate Control Micro-Controller Engine

class SmartHVACController:
    def __init__(self, target_temp=22.0):
        self.target = target_temp

    def evaluate_hvac_state(self, current_ambient_temp):
        variance = current_ambient_temp - self.target
        if variance >= 1.5:
            return "COMPRESSOR_ACTIVE_COOLING"
        elif variance <= -1.5:
            return "HEATING_COILS_IGNITED"
        return "SYSTEM_STANDBY_OPTIMAL"

if __name__ == "__main__":
    controller = SmartHVACController()
    print(f"HVAC Automated Pin State: {controller.evaluate_hvac_state(25.4)}")