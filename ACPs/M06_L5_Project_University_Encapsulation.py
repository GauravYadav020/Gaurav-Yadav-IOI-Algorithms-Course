# Module 6 Lesson 5: After-Class Project
# Project Name: Secured Academic Registrar Student Database Encapsulation System

class EncapsulatedStudentProfile:
    def __init__(self, student_id, legal_name):
        self.__student_id = student_id # Strict private field encapsulation
        self.__legal_name = legal_name
        self.__cgpa = 0.0

    @property
    def cgpa(self):
        return self.__cgpa

    @cgpa.setter
    def cgpa(self, values_input_score):
        # Business logic access rules enforcement validation
        if 0.0 <= values_input_score <= 10.0:
            self.__cgpa = values_input_score
        else:
            print("🚨 Secure Validation Alert: Illegal CGPA entry bounds blocked.")

if __name__ == "__main__":
    profile = EncapsulatedStudentProfile("UID-2026-94", "Kabir Mehta")
    profile.cgpa = 9.4
    print(f"Validated Student Encapsulated Score Attribute: {profile.cgpa}")
    profile.cgpa = 14.2 # Triggers fallback validation error guards