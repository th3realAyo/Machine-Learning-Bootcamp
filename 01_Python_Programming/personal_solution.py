FILE_PATH = "content.txt"

class StudentManager:
    def __init__(self):
        self.history = self.load_records()
            
    def load_records(self):
        data = {}
        try:
            with open(FILE_PATH, "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        name, marks = line.split(",")
                        data[name] = float(marks)
        except FileNotFoundError as e:
            print("File does not exist", e)
        return data
    
    def save_records(self):
        try:
            with open(FILE_PATH, "w") as file:
                pass
        except FileNotFoundError as e:
            print("File not found", e)        
    
def main():
    manager = StudentManager()
    manager.load_records()
    manager.save_records()
    print("Test successfull")

if __name__ == "__main__":
    main()