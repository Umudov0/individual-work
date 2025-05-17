# Re-run full code including the missing definitions at the top

import json

# Global data store
students = []

# 1. Welcome screen
def welcome_screen():
    print("="*40)
    print("     Student Management System")
    print("="*40)

# 2. Main menu
def show_menu():
    print("\nMain Menu:")
    print("1. Add new student")
    print("2. View all students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Calculate statistics")
    print("7. Save to file")
    print("8. Load from file")
    print("9. Sort students")
    print("10. Help")
    print("11. Clear all data")
    print("0. Exit")

# 3. Add new record
def add_student():
    try:
        student = {}
        student['id'] = input("Enter ID: ")
        student['name'] = input("Enter name: ")
        student['age'] = int(input("Enter age: "))
        student['grade'] = float(input("Enter grade: "))
        students.append(student)
        print("Student added successfully.")
    except ValueError:
        print("Invalid input. Please enter correct data.")

# 5. View all records
def view_students():
    if not students:
        print("No student records found.")
        return
    print("\nStudent Records:")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")

# 6. Search for a student
def search_student():
    keyword = input("Enter ID or name to search: ")
    found = False
    for s in students:
        if s['id'] == keyword or s['name'].lower() == keyword.lower():
            print(f"Found: ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")
            found = True
            break
    if not found:
        print("Student not found.")

# 7. Update a student's data
def update_student():
    sid = input("Enter student ID to update: ")
    for s in students:
        if s['id'] == sid:
            s['name'] = input("Enter new name: ")
            s['age'] = int(input("Enter new age: "))
            s['grade'] = float(input("Enter new grade: "))
            print("Student updated.")
            return
    print("Student not found.")

# 8. Delete a student
def delete_student():
    sid = input("Enter student ID to delete: ")
    for s in students:
        if s['id'] == sid:
            students.remove(s)
            print("Student deleted.")
            return
    print("Student not found.")

# 10. Calculate summary statistics
def calculate_stats():
    if not students:
        print("No data to calculate.")
        return
    total = sum(s['grade'] for s in students)
    avg = total / len(students)
    print(f"Average grade: {avg:.2f}")

# 11. Save to file
def save_to_file():
    with open("students.json", "w") as f:
        json.dump(students, f)
    print("Data saved to students.json.")

# 12. Load from file
def load_from_file():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
        print("Data loaded from file.")
    except FileNotFoundError:
        print("File not found.")

# 16. Sorting
def sort_students():
    field = input("Sort by 'id', 'name', 'age' or 'grade': ")
    if field in ['id', 'name', 'age', 'grade']:
        sorted_list = sorted(students, key=lambda x: x[field])
        for s in sorted_list:
            print(f"ID: {s['id']}, Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}")
    else:
        print("Invalid field.")

# 17. Recursive operation: Count students
def count_students_recursive(lst):
    if not lst:
        return 0
    return 1 + count_students_recursive(lst[1:])

# 18. Help menu
def show_help():
    print("""
This is a simple Student Management System.
You can:
- Add, update, delete, view, and search student records.
- Save/load data to/from a file.
- View statistics and sort students.
- Clear all data (with confirmation).
""")

# 19. Clear all data
def clear_all_data():
    confirm = input("Are you sure you want to delete all data? (yes/no): ")
    if confirm.lower() == "yes":
        students.clear()
        print("All data cleared.")
    else:
        print("Action canceled.")

# 20. Optional: ASCII Art / UI polish
def ascii_art():
    print(r"""
   ____  _             _            _       
  / ___|| |_ ___   ___| | ___   ___| |_ ___ 
  \___ \| __/ _ \ / __| |/ _ \ / __| __/ __|
   ___) | || (_) | (__| | (_) | (__| |_\__ \
  |____/ \__\___/ \___|_|\___/ \___|\__|___/
    """)

# Main loop
def main():
    welcome_screen()
    ascii_art()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            calculate_stats()
        elif choice == "7":
            save_to_file()
        elif choice == "8":
            load_from_file()
        elif choice == "9":
            sort_students()
        elif choice == "10":
            show_help()
        elif choice == "11":
            clear_all_data()
        elif choice == "0":
            print(f"Total students counted recursively: {count_students_recursive(students)}")
            print("Exiting the system...")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
main()

