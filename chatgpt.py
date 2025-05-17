def welcome_screen():
    print("=" * 50)
    print("     Welcome to Student Management System     ")
    print("              by Umudov Aqif Arif             ")
    print("=" * 50)
    print()

def display_menu():
    print("Main Menu:")
    print("1. Add new record")
    print("2. View all records")
    print("3. Search for a record")
    print("4. Update a record")
    print("5. Delete a record")
    print("6. Summary statistics")
    print("7. Save records to file")
    print("8. Load records from file")
    print("9. Help/Instructions")
    print("10. Clear all data")
    print("11. Exit")


records = []


def add_record():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    balance = float(input("Enter balance: "))

    record = {
        "id": student_id,
        "name": name,
        "grade": grade,
        "balance": balance
    }
    records.append(record)
    print("Record added successfully!\n")

def view_records():
    if not records:
        print("No records to show.\n")
        return
    for rec in records:
        print(f"ID: {rec['id']}, Name: {rec['name']}, Grade: {rec['grade']}, Balance: ${rec['balance']}")
    print()

def search_record():
    keyword = input("Enter ID or Name to search: ").lower()
    found = False
    for rec in records:
        if keyword in rec['id'].lower() or keyword in rec['name'].lower():
            print(f"Found: ID: {rec['id']}, Name: {rec['name']}, Grade: {rec['grade']}, Balance: ${rec['balance']}")
            found = True
    if not found:
        print("No matching record found.\n")

def update_record():
    student_id = input("Enter student ID to update: ")
    for rec in records:
        if rec['id'] == student_id:
            rec['name'] = input("Enter new name: ")
            rec['grade'] = float(input("Enter new grade: "))
            rec['balance'] = float(input("Enter new balance: "))
            print("Record updated!\n")
            return
    print("Record not found.\n")

def delete_record():
    student_id = input("Enter student ID to delete: ")
    for rec in records:
        if rec['id'] == student_id:
            records.remove(rec)
            print("Record deleted.\n")
            return
    print("Record not found.\n")

def summary_stats():
    if not records:
        print("No data to summarize.\n")
        return
    avg_grade = sum(r['grade'] for r in records) / len(records)
    total_balance = sum(r['balance'] for r in records)
    print(f"Average Grade: {avg_grade:.2f}")
    print(f"Total Balance: ${total_balance:.2f}\n")

def main():
    welcome_screen()
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option: "))
            print()
            if choice == 1:
                add_record()
            elif choice == 2:
                view_records()
            elif choice == 3:
                search_record()
            elif choice == 4:
                update_record()
            elif choice == 5:
                delete_record()
            elif choice == 6:
                summary_stats()
            elif choice == 7:
                save_to_file()
            elif choice == 8:
                load_from_file()
            elif choice == 9:
                show_help()
            elif choice == 10:
                clear_data()
            elif choice == 11:
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.\n")
        except ValueError:
            print("Please enter a number.\n")


def sort_records():
    if not records:
        print("No records to sort.\n")
        return
    field = input("Sort by 'id', 'name', 'grade', or 'balance': ")
    if field in ["id", "name", "grade", "balance"]:
        sorted_records = sorted(records, key=lambda x: x[field])
        for rec in sorted_records:
            print(f"ID: {rec['id']}, Name: {rec['name']}, Grade: {rec['grade']}, Balance: ${rec['balance']}")
        print()
    else:
        print("Invalid field.\n")

def count_records(index=0):
    if index == len(records):
        return 0
    return 1 + count_records(index + 1)

def show_help():
    print("This is a simple student management system.")
    print("Use the menu to add, update, delete, and view student records.")
    print("You can also save/load data from a file.\n")

def clear_data():
    confirm = input("Are you sure you want to delete all records? (yes/no): ")
    if confirm.lower() == "yes":
        records.clear()
        print("All records cleared.\n")
    else:
        print("Operation cancelled.\n")

def loading_animation():
    import time
    print("Loading", end="")
    for _ in range(5):
        print(".", end="", flush=True)
        time.sleep(0.3)
    print("\n")


if __name__ == "__main__":
    main()

