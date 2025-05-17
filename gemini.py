class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        while True:
            try:
                grade = float(input("Enter student grade: "))
                if 0 <= grade <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number for the grade.")

        self.students[student_id] = Student(student_id, name, grade)
        print(f"Student {name} added successfully.")

    def view_all_students(self):
        if not self.students:
            print("No students in the system.")
            return
        print("\n--- All Students ---")
        for student in self.students.values():
            print(student)
        print("--------------------")

    def search_student(self):
        search_term = input("Enter student ID or name to search: ").lower()
        found = False
        print("\n--- Search Results ---")
        for student in self.students.values():
            if search_term in student.student_id.lower() or search_term in student.name.lower():
                print(student)
                found = True
        if not found:
            print("No matching student found.")
        print("----------------------")

    def update_student(self):
        student_id = input("Enter the ID of the student to update: ")
        if student_id in self.students:
            student = self.students[student_id]
            print(f"Current details for student {student_id}: {student}")
            name = input(f"Enter new name (leave blank to keep '{student.name}'): ")
            while True:
                grade_input = input(f"Enter new grade (leave blank to keep '{student.grade}'): ")
                if not grade_input:
                    break
                try:
                    grade = float(grade_input)
                    if 0 <= grade <= 100:
                        student.grade = grade
                        break
                    else:
                        print("Grade must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number for the grade.")

            if name:
                student.name = name
            print(f"Student {student_id} updated successfully.")
        else:
            print(f"Student with ID {student_id} not found.")

    def delete_student(self):
        student_id = input("Enter the ID of the student to delete: ")
        if student_id in self.students:
            del self.students[student_id]
            print(f"Student with ID {student_id} deleted successfully.")
        else:
            print(f"Student with ID {student_id} not found.")

    def display_menu(self):
        print("\n--- Student Management System ---")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("---------------------------------")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_all_students()
            elif choice == '3':
                self.search_student()
            elif choice == '4':
                self.update_student()
            elif choice == '5':
                self.delete_student()
            elif choice == '6':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    system = StudentManagementSystem()
    print("Welcome to the Student Management System!")
    system.run()