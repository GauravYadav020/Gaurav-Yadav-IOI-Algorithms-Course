# Module 3 Lesson 2: After-Class Project
# Project Name: Clinical Patient Medical Triage Priority Pipeline

class HospitalTriagePipeline:
    def __init__(self):
        self.waiting_room_list = []

    def check_in_patient(self, name, severity_tier_1_to_5):
        # 5 indicates critical immediate stabilization criteria
        self.waiting_room_list.append((name, severity_tier_1_to_5))
        # Sort so highest severity patients sit first in the array lineup pipeline
        self.waiting_room_list.sort(key=lambda item: item[1], reverse=True)

    def extract_next_critical_case(self):
        return self.waiting_room_list.pop(0) if self.waiting_room_list else None

if __name__ == "__main__":
    triage = HospitalTriagePipeline()
    triage.check_in_patient("John Doe", 2)
    triage.check_in_patient("Critical Case Emergency", 5)
    print(f"Next Patient Extracted via Triage Array: {triage.extract_next_critical_case()}")