"""
    Assignment Project: Student Record Manager (Self Evaluation)

    Features:
    Your program should:
    - Add a student record with name and marks
    - View all student records
    - Search a student by name
    - Update a student’s marks
    - Delete a student record
    - Save records to a file
    - Load records automatically when the program starts
    - Handle invalid inputs gracefully
    
"""

import json
import time
import contextlib

RECORDS_FILE = "students.json"

def timer():
    time.sleep(2)

class StudentManager:
    def __init__(self):
        self.students = self.load_records()
        
    def load_records(self):
        with contextlib.suppress(FileNotFoundError):
            with open(RECORDS_FILE, "r") as f:
                return json.load(f)
        return []

    def save_records(self):
        with open(RECORDS_FILE, "w") as file:
            json.dump(self.students, file)  
    
    def add_student(self):
        name = input("Enter student name: ").strip()
        while True:
            try:
                mark = float(input("Enter student mark: "))
                break
            except ValueError as e:
                print("Enter a valid figure", e)
        student = {"name": name, "marks": mark}
        self.students.append(student)
        print(f"{name} added sucessfully!")
    
    def view_students(self):
        if not self.students:
            print("No student records found.")
            return
            
        for i, student in enumerate(self.students, start = 1):
            print(f"Student {i}: {student['name']} | Marks: {student['marks']}")
    
    def search_student(self):
        found = False
        
        fetch_data = input("Search by student name: ").strip().lower()
        for data in self.students:
            if (data["name"]).lower() == fetch_data:
                print("Student Data Found:")
                print(f"Name: {data['name']} | Marks: {data['marks']}")
                found = True
                
        if not found:
            print("Student data not found!")
            return

    def update_student(self): 
        print("-------Update Student Score-------")
        found = False
        find_student = input("Search by student name: ").strip().lower()

        for student in self.students:
            if (student["name"]).lower() == find_student:
                print("Searching....")
                timer()
                print("Student Found! Enter New Mark Below")
                
                while True:
                    try:
                        student["marks"] = float(input("Enter new mark: "))
                        break
                    except ValueError as e:
                        print("Enter a valid score", e)
                found = True
        if not found:
                print("Student data not found!")
    def delete_student(self):
        student_to_delete = None
        
        student_name = input("Enter student name to delete: ").strip().lower()
        for student in self.students:
            if student["name"].lower() == student_name:
                student_to_delete = student
                break
        if student_to_delete:
            self.students.remove(student_to_delete)
            print("Student removed successfully!")
        else:   
            print("Student not found!")
    
def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Save Records")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.update_student()
        elif choice == "5":
            manager.delete_student()
        elif choice == "6":
            manager.save_records()
        elif choice == "7":
            manager.save_records()
            print("Records saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

    print(manager.students)
    
if __name__ == "__main__":
    main()