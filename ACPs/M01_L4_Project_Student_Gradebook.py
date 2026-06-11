# Module 1 Lesson 4: After-Class Project
# Project Name: Academic Gradebook Analyzer and Analytics Engine

class AcademicGradebook:
    def __init__(self):
        self.records = {}

    def commit_grade(self, student_name, homework_scores, exam_score):
        avg_hw = sum(homework_scores) / len(homework_scores) if homework_scores else 0
        composite_score = (avg_hw * 0.4) + (exam_score * 0.6)
        
        if composite_score >= 90: grade = 'A'
        elif composite_score >= 80: grade = 'B'
        elif composite_score >= 70: grade = 'C'
        else: grade = 'F'
        
        self.records[student_name] = {"Score": composite_score, "Grade": grade}

if __name__ == "__main__":
    book = AcademicGradebook()
    book.commit_grade("Rohan Sharma", [85, 90, 95], 88)
    print(f"Evaluated Academic Profile: {book.records}")