import os
import json
import time


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.file_path = "students.json"
        self.load_data()

    def welcome_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n==== TƏLƏBƏ İDARƏETMƏ SİSTEMİ ====")
        print("     Yaradıcı: Umudov Aqif Arif")
        print("================================\n")
        time.sleep(1)

    def display_menu(self):
        print("\n=== ƏSAS MENYU ===")
        print("1. Yeni tələbə əlavə et")
        print("2. Bütün tələbələri göstər")
        print("3. Tələbə axtar")
        print("4. Tələbə məlumatlarını yenilə")
        print("5. Tələbəni sil")
        print("6. Statistikanı hesabla")
        print("7. Məlumatları fayla yaz")
        print("8. Fayldan məlumatları oxu")
        print("9. Tələbələri sırala")
        print("10. Yardım/Təlimatlar")
        print("11. Bütün məlumatları təmizlə")
        print("12. Çıxış")
        print("================")

    def add_student(self):
        print("\n-- Yeni Tələbə Əlavə Et --")
        student_id = input("Tələbə ID: ")

        # ID-nin təkrar olub-olmadığını yoxla
        if any(student["id"] == student_id for student in self.students):
            print("Xəta: Bu ID artıq mövcuddur!")
            return

        name = input("Ad Soyad: ")

        try:
            age = int(input("Yaş: "))
            if age <= 0 or age > 100:
                print("Səhv yaş! 1-100 arasında olmalıdır.")
                return
        except ValueError:
            print("Səhv daxil edilib! Yaş rəqəm olmalıdır.")
            return

        try:
            grade = float(input("Ortalama bal (0.0-4.0): "))
            if grade < 0 or grade > 4.0:
                print("Səhv bal! 0.0-4.0 arasında olmalıdır.")
                return
        except ValueError:
            print("Səhv daxil edilib! Bal rəqəm olmalıdır.")
            return

        courses = input("Fənlər (vergüllə ayırın): ").split(",")
        courses = [course.strip() for course in courses if course.strip()]

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "courses": courses
        }

        self.students.append(student)
        print(f"\n'{name}' uğurla əlavə edildi!")

    def view_all_students(self):
        if not self.students:
            print("\nSistemde tələbə yoxdur.")
            return

        print("\n-- Bütün Tələbələr --")
        print("\n{:<5} {:<20} {:<5} {:<6} {:<25}".format(
            "ID", "Ad", "Yaş", "Bal", "Fənlər"))
        print("-" * 65)

        for student in self.students:
            courses_str = ", ".join(student["courses"][:2])
            if len(student["courses"]) > 2:
                courses_str += "..."

            print("{:<5} {:<20} {:<5} {:<6.2f} {:<25}".format(
                student["id"],
                student["name"][:18],
                student["age"],
                student["grade"],
                courses_str[:23]
            ))

    def search_student(self):
        if not self.students:
            print("\nSistemde tələbə yoxdur.")
            return

        print("\n-- Tələbə Axtar --")
        search_term = input("Tələbə ID və ya adını daxil edin: ").lower()

        found = False
        for student in self.students:
            if (search_term == student["id"].lower() or
                    search_term in student["name"].lower()):
                found = True
                print("\n--- Tələbə Tapıldı ---")
                print(f"ID: {student['id']}")
                print(f"Ad: {student['name']}")
                print(f"Yaş: {student['age']}")
                print(f"Bal: {student['grade']:.2f}")
                print(f"Fənlər: {', '.join(student['courses'])}")

        if not found:
            print(f"\nBu adda veya ID-də tələbə tapılmadı: '{search_term}'.")

    def update_student(self):
        if not self.students:
            print("\nSistemde tələbə yoxdur.")
            return

        print("\n-- Tələbə Məlumatlarını Yenilə --")
        student_id = input("Yeniləmək üçün tələbə ID: ")

        for i, student in enumerate(self.students):
            if student["id"] == student_id:
                print(f"\nTələbəni yeniləmə: {student['name']}")

                name = input(f"Yeni ad (hazırkı: {student['name']}), və ya Enter basın: ")
                if name:
                    self.students[i]["name"] = name

                try:
                    age_input = input(f"Yeni yaş (hazırkı: {student['age']}), və ya Enter basın: ")
                    if age_input:
                        age = int(age_input)
                        if age <= 0 or age > 100:
                            print("Səhv yaş! 1-100 arasında olmalıdır.")
                            return
                        self.students[i]["age"] = age
                except ValueError:
                    print("Səhv daxil edilib! Yaş rəqəm olmalıdır.")
                    return

                try:
                    grade_input = input(f"Yeni bal (hazırkı: {student['grade']:.2f}), və ya Enter basın: ")
                    if grade_input:
                        grade = float(grade_input)
                        if grade < 0 or grade > 4.0:
                            print("Səhv bal! 0.0-4.0 arasında olmalıdır.")
                            return
                        self.students[i]["grade"] = grade
                except ValueError:
                    print("Səhv daxil edilib! Bal rəqəm olmalıdır.")
                    return

                courses_input = input(f"Yeni fənlər (hazırkı: {', '.join(student['courses'])}), və ya Enter basın: ")
                if courses_input:
                    courses = courses_input.split(",")
                    courses = [course.strip() for course in courses if course.strip()]
                    self.students[i]["courses"] = courses

                print(f"\nTələbə '{self.students[i]['name']}' uğurla yeniləndi!")
                return

        print(f"\nBu ID-də tələbə tapılmadı: {student_id}")

    def delete_student(self):
        if not self.students:
            print("\nSistemde tələbə yoxdur.")
            return

        print("\n-- Tələbəni Sil --")
        student_id = input("Silmək üçün tələbə ID: ")

        for i, student in enumerate(self.students):
            if student["id"] == student_id:
                confirm = input(
                    f"'{student['name']}' adlı tələbəni silmək istədiyinizə əminsiniz? (bəli/xeyr): ").lower()
                if confirm == "bəli" or confirm == "beli":
                    deleted_student = self.students.pop(i)
                    print(f"\nTələbə '{deleted_student['name']}' uğurla silindi!")
                else:
                    print("\nSilmə əməliyyatı ləğv edildi.")
                return

        print(f"\nBu ID-də tələbə tapılmadı: {student_id}")

    def calculate_statistics(self):
        print("\n-- Statistika --")

        if self.students:
            total_students = len(self.students)
            avg_age = sum(student["age"] for student in self.students) / total_students
            avg_grade = sum(student["grade"] for student in self.students) / total_students

            # Ən yaxşı tələbəni tap
            top_student = max(self.students, key=lambda x: x["grade"])

            # Fənləri say
            all_courses = []
            for student in self.students:
                all_courses.extend(student["courses"])
            unique_courses = set(all_courses)

            print(f"Tələbələrin ümumi sayı: {total_students}")
            print(f"Orta yaş: {avg_age:.2f}")
            print(f"Orta bal: {avg_grade:.2f}")
            print(f"Ən yaxşı tələbə: {top_student['name']} (Bal: {top_student['grade']:.2f})")
            print(f"Fərqli fənlərin sayı: {len(unique_courses)}")
        else:
            print("Sistemdə tələbə yoxdur.")

    def save_data(self):
        try:
            with open(self.file_path, "w") as file:
                json.dump(self.students, file, indent=4)

            print(f"\nMəlumatlar uğurla '{self.file_path}' faylına yazıldı")
        except Exception as e:
            print(f"\nMəlumatları yazarkən xəta baş verdi: {e}")

    def load_data(self):
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, "r") as file:
                    self.students = json.load(file)
                return True
            return False
        except Exception as e:
            print(f"\nMəlumatları oxuyarkən xəta baş verdi: {e}")
            return False

    def load_data_with_feedback(self):
        if self.load_data():
            print(f"\nMəlumatlar uğurla '{self.file_path}' faylından oxundu")
            print(f"{len(self.students)} tələbə yükləndi.")
        else:
            print(f"\n'{self.file_path}' faylı tapılmadı")

    def sort_students(self):
        if not self.students:
            print("\nSistemde tələbə yoxdur.")
            return

        print("\n-- Tələbələri Sırala --")
        print("Sıralama növü:")
        print("1. ID")
        print("2. Ad")
        print("3. Yaş")
        print("4. Bal (yüksəkdən aşağı)")

        try:
            choice = int(input("\nSeçiminiz (1-4): "))

            if choice == 1:
                self.students.sort(key=lambda x: x["id"])
                field = "ID"
            elif choice == 2:
                self.students.sort(key=lambda x: x["name"].lower())
                field = "ad"
            elif choice == 3:
                self.students.sort(key=lambda x: x["age"])
                field = "yaş"
            elif choice == 4:
                self.students.sort(key=lambda x: x["grade"], reverse=True)
                field = "bal (yüksəkdən aşağı)"
            else:
                print("Yanlış seçim.")
                return

            print(f"\nTələbələr {field} əsasında sıralandı.")
            self.view_all_students()
        except ValueError:
            print("Yanlış daxil edilib! Zəhmət olmasa rəqəm daxil edin.")

    def count_entries(self, data, depth=0):
        """Rekursiv funksiya ilə elementləri say"""
        if isinstance(data, list):
            return sum(self.count_entries(item, depth + 1) for item in data)
        return 1

    def count_recursively(self):
        student_count = self.count_entries(self.students)
        print(f"\nSistemde olan tələbələrin sayı: {student_count}")

    def display_help(self):
        print("\n--- YARDIM VƏ TƏLİMATLAR ---")
        print("1. Yeni tələbə əlavə etmək üçün menüdan 1-i seçin.")
        print("2. Tələbələri görmək üçün menüdan 2-ni seçin.")
        print("3. Konkret bir tələbəni axtarmaq üçün menüdan 3-ü seçin.")
        print("4. Tələbə məlumatlarını yeniləmək üçün menüdan 4-ü seçin.")
        print("5. Tələbə silmək üçün menüdan 5-i seçin.")
        print("6. Statistikanı görmək üçün menüdan 6-nı seçin.")
        print("7. Məlumatları fayla yazmaq üçün menüdan 7-ni seçin.")
        print("8. Məlumatları fayldan oxumaq üçün menüdan 8-i seçin.")
        print("9. Tələbələri sıralamaq üçün menüdan 9-u seçin.")
        print("10. Yardım almaq üçün menüdan 10-u seçin.")
        print("11. Bütün məlumatları silmək üçün menüdan 11-i seçin.")
        print("12. Proqramdan çıxmaq üçün menüdan 12-ni seçin.")

    def clear_all_data(self):
        if not self.students:
            print("\nSistemde tələbə yoxdur.")
            return

        confirm = input("\nDİQQƏT: Bütün tələbə məlumatları silinəcək. Davam etmək istəyirsiniz? (bəli/xeyr): ").lower()
        if confirm == "bəli" or confirm == "beli":
            self.students = []
            print("\nBütün məlumatlar uğurla silindi!")
        else:
            print("\nƏməliyyat ləğv edildi.")

    def run(self):
        self.welcome_screen()

        while True:
            self.display_menu()

            try:
                choice = input("\nSeçiminiz (1-12): ")

                if choice == "1":
                    self.add_student()
                elif choice == "2":
                    self.view_all_students()
                elif choice == "3":
                    self.search_student()
                elif choice == "4":
                    self.update_student()
                elif choice == "5":
                    self.delete_student()
                elif choice == "6":
                    self.calculate_statistics()
                elif choice == "7":
                    self.save_data()
                elif choice == "8":
                    self.load_data_with_feedback()
                elif choice == "9":
                    self.sort_students()
                elif choice == "10":
                    self.display_help()
                elif choice == "11":
                    self.clear_all_data()
                elif choice == "12":
                    print("\nProqramdan çıxılır...")
                    print("Sağ olun! Yenə görüşənədək!")
                    break
                else:
                    print("\nYanlış seçim! Zəhmət olmasa 1-12 arası bir rəqəm daxil edin.")

                input("\nDavam etmək üçün ENTER düyməsini basın...")
                os.system('cls' if os.name == 'nt' else 'clear')

            except Exception as e:
                print(f"\nXəta baş verdi: {e}")
                input("\nDavam etmək üçün ENTER düyməsini basın...")


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.run()