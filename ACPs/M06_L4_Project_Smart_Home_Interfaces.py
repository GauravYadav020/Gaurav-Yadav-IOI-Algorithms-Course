# Module 6 Lesson 4: After-Class Project
# Project Name: Smart IoT Home Architecture Controller Polymorphism Interfaces

class IoTControllerInterface:
    def trigger_power_state(self, state_string):
        raise NotImplementedError("Virtual interface layout method must be implemented.")

class SmartHeaterNode(IoTControllerInterface):
    def trigger_power_state(self, state_string):
        return f"SmartHeaterNode state reassigned to logic payload: {state_string.upper()}"

class SmartMediaStreamer(IoTControllerInterface):
    def trigger_power_state(self, state_string):
        return f"SmartMediaStreamer system network power profile: {state_string.lower()}"

if __name__ == "__main__":
    iot_grid = [SmartHeaterNode(), SmartMediaStreamer()]
    print("Iterating over modern abstract runtime interfaces:")
    for device in iot_grid:
        print(device.trigger_power_state("TERMINATE_STANDBY"))