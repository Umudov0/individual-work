import json

# Student management system
class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age, grade):
        student = {"ID": student_id, "Name": name, "Age": age, "Grade": grade}
        self.students.append(student)
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No students found.")
        else:
            for student in self.students:
                print(student)

    def search_student(self, student_id):
        for student in self.students:
            if student["ID"] == student_id:
                print("Student found:", student)
                return
        print("Student not found.")

    def update_student(self, student_id, name=None, age=None, grade=None):
        for student in self.students:
            if student["ID"] == student_id:
                if name:
                    student["Name"] = name
                if age:
                    student["Age"] = age
                if grade:
                    student["Grade"] = grade
                print("Student updated successfully.")
                return
        print("Student not found.")

    def delete_student(self, student_id):
        for student in self.students:
            if student["ID"] == student_id:
                self.students.remove(student)
                print("Student deleted successfully.")
                return
        print("Student not found.")

    def save_to_file(self, filename="students.json"):
        with open(filename, "w") as file:
            json.dump(self.students, file)
        print("Data saved successfully.")

    def load_from_file(self, filename="students.json"):
        try:
            with open(filename, "r") as file:
                self.students = json.load(file)
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("File not found, loading skipped.")

# Example usage
sms = StudentManagementSystem()
sms.add_student(1, "John Doe", 16, "10th Grade")
sms.view_students()
sms.search_student(1)
sms.update_student(1, grade="11th Grade")
sms.delete_student(1)
sms.save_to_file()
sms.load_from_file()
