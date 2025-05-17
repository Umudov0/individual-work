import json
import time

students = []

def welcome_screen():
    print("""
    ***************************************
    *     WELCOME TO STUDENT SYSTEM       *
    *       Designed by Aqif :)           *
    ***************************************
    """)
    time.sleep(2)

def main_menu():
    print("""
    ========== MAIN MENU ==========
    1. Add Student
    2. View Students
    3. Search Student by ID
    4. Update Student
    5. Delete Student
    6. Summary Statistics
    7. Save to File
    8. Load from File
    9. Sort Students
    10. Count Students (Recursive)
    11. Help
    12. Clear All Data
    0. Exit
    ===============================
    """)

def input_student():
    try:
        student = {
            "id": input("Enter ID: "),
            "name": input("Enter Name: "),
            "grade": float(input("Enter Grade (0-100): "))
        }
        students.append(student)
        print("✅ Student added successfully.")
    except ValueError:
        print("❌ Invalid grade! Please enter a number.")

def view_students():
    if not students:
        print("📂 No students in the system.")
    else:
        print("{:<10} {:<20} {:<10}".format("ID", "Name", "Grade"))
        for s in students:
            print("{:<10} {:<20} {:<10.2f}".format(s["id"], s["name"], s["grade"]))

def search_student():
    sid = input("Enter ID to search: ")
    for s in students:
        if s["id"] == sid:
            print("🔍 Student Found:", s)
            return
    print("❌ Student not found.")

def update_student():
    sid = input("Enter ID to update: ")
    for s in students:
        if s["id"] == sid:
            s["name"] = input("Enter new name: ")
            try:
                s["grade"] = float(input("Enter new grade: "))
                print("✅ Student updated.")
            except ValueError:
                print("❌ Invalid grade entered.")
            return
    print("❌ Student not found.")

def delete_student():
    sid = input("Enter ID to delete: ")
    for i, s in enumerate(students):
        if s["id"] == sid:
            del students[i]
            print("🗑️ Student deleted.")
            return
    print("❌ Student not found.")

def summary_stats():
    if not students:
        print("📊 No students to analyze.")
        return
    total = sum(s["grade"] for s in students)
    avg = total / len(students)
    print(f"👥 Total students: {len(students)}")
    print(f"📈 Average grade: {avg:.2f}")

def save_to_file():
    with open("students.json", "w") as f:
        json.dump(students, f)
    print("💾 Data saved to students.json.")

def load_from_file():
    global students
    try:
        with open("students.json", "r") as f:
            students = json.load(f)
        print("📂 Data loaded successfully.")
    except FileNotFoundError:
        print("❌ File not found.")
    except json.JSONDecodeError:
        print("❌ File is corrupted.")

def sort_students():
    key = input("Sort by 'id', 'name', or 'grade': ").lower()
    if key in ["id", "name", "grade"]:
        students.sort(key=lambda x: x[key])
        print(f"✅ Students sorted by {key}.")
    else:
        print("❌ Invalid field.")

def recursive_count(index=0):
    if index >= len(students):
        return 0
    return 1 + recursive_count(index + 1)

def help_menu():
    print("""
    📘 Help - How to Use the System:
    - Choose a menu option by typing the number.
    - Make sure each student ID is unique.
    - Use 'Save' before exiting to keep your data.
    - Use 'Load' to bring back saved data.
    """)

def clear_data():
    confirm = input("⚠️ Are you sure to delete all data? (yes/no): ")
    if confirm.lower() == "yes":
        students.clear()
        print("🧹 All student data cleared.")
    else:
        print("❎ Operation cancelled.")

def main():
    welcome_screen()
    while True:
        main_menu()
        choice = input("Choose an option: ")
        match choice:
            case "1": input_student()
            case "2": view_students()
            case "3": search_student()
            case "4": update_student()
            case "5": delete_student()
            case "6": summary_stats()
            case "7": save_to_file()
            case "8": load_from_file()
            case "9": sort_students()
            case "10": print(f"📋 Total students (recursive): {recursive_count()}")
            case "11": help_menu()
            case "12": clear_data()
            case "0":
                print("👋 Goodbye!")
                break
            case _: print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
