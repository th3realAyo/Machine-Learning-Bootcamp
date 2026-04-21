"""
Mini Project: Student Record Manager (Beginner Friendly)

Features:
- Class-based approach
- Menu-driven console program
- Store student records in a dictionary
- Save and load records using a text file
- Basic error handling
"""

DATA_FILE = "students.txt"


class StudentManager:

    def __init__(self):
        self.students = self.load_records()

    # ------------------------
    # File Handling
    # ------------------------
    def load_records(self):
        data = {}
        try:
            with open(DATA_FILE, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        name, marks = line.split(",")
                        data[name] = float(marks)
        except FileNotFoundError:
            pass
        return data

    def save_records(self):
        with open(DATA_FILE, "w") as f:
            for name, marks in self.students.items():
                f.write(f"{name},{marks}\n")

    # ------------------------
    # Helper Methods
    # ------------------------
    def get_marks(self):
        while True:
            value = input("Enter marks: ")
            try:
                return float(value)
            except ValueError:
                print("Please enter a valid number.")

    # ------------------------
    # Core Features
    # ------------------------
    def add_student(self):
        name = input("Enter student name: ")

        if name in self.students:
            print("Student already exists.")
            return

        marks = self.get_marks()
        self.students[name] = marks
        print("Student added successfully.")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\nStudent Records:")
        for name, marks in self.students.items():
            print(name, ":", marks)

    def search_student(self):
        name = input("Enter student name to search: ")

        if name in self.students:
            print(name, ":", self.students[name])
        else:
            print("Student not found.")

    def update_marks(self):
        name = input("Enter student name to update: ")

        if name not in self.students:
            print("Student not found.")
            return

        marks = self.get_marks()
        self.students[name] = marks
        print("Marks updated.")

    def delete_student(self):
        name = input("Enter student name to delete: ")

        if name in self.students:
            del self.students[name]
            print("Student deleted.")
        else:
            print("Student not found.")


def main():
    manager = StudentManager()

    while True:
        print("\nStudent Record Manager")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update marks")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.update_marks()
        elif choice == "5":
            manager.delete_student()
        elif choice == "6":
            manager.save_records()
            print("Goodbye. Records saved.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
    