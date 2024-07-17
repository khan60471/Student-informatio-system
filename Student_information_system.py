# Function to insert student data
def insert_student_data():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    with open("student_data.txt", "a") as file:
        file.write(f"{roll_no},{name}\n")
    print("Student data inserted successfully.")

# Function to update student data
def update_student_data():
    roll_no = input("Enter Roll Number to update: ")
    name = input("Enter New Name: ")
    with open("student_data.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if roll_no not in line:
                file.write(line)
        file.write(f"{roll_no},{name}\n")
    print("Student data updated successfully.")

# Function to delete student data
def delete_student_data():
    roll_no = input("Enter Roll Number to delete: ")
    with open("student_data.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if roll_no not in line:
                file.write(line)
        file.truncate()
    print("Student data deleted successfully.")

# Function to mark a student
def marks_student():
    roll_no = input("Enter Roll Number to mark: ")
    marks = []
    for i in range(5):
        marks.append(float(input(f"Enter Marks for Subject {i+1}: ")))
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100
    grade = ''
    if percentage >= 90:
        grade = 'A'
    elif 80 <= percentage < 90:
        grade = 'B'
    elif 70 <= percentage < 80:
        grade = 'C'
    elif 60 <= percentage < 70:
        grade = 'D'
    else:
        grade = 'F'
    
    with open("student_marks.txt", "a") as file:
        file.write(f"{roll_no},{','.join(map(str, marks))},{total_marks},{percentage:.2f},{grade}\n")
    print("Marks added successfully.")

# Function to delete or update marks
def delete_or_update_marks():
    roll_no = input("Enter Roll Number to delete/update marks: ")
    with open("student_marks.txt", "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if roll_no not in line:
                file.write(line)
        file.truncate()
    print("Student marks deleted/updated successfully.")

# Function to retrieve specific roll number data
def retrieve_specific_roll_number(roll_no):
    with open("student_data.txt", "r") as file:
        for line in file:
            if roll_no in line:
                print(line.strip())

# Function to check for duplicates
def check_duplicates(roll_no):
    with open("student_data.txt", "r") as file:
        for line in file:
            if roll_no in line:
                return True
    return False

# Function to show all data in console
def show_data():
    with open("student_data.txt", "r") as file:
        print("Student Data:")
        for line in file:
            print(line.strip())

# Main function
def main():
    while True:
        print("\n*** Student Information System ***")
        print("1) Insert Student Data")
        print("2) Update Student Data")
        print("3) Delete Student Data")
        print("4) Marks of a Student")
        print("5) Delete or Update Marks")
        print("6) Retrieve Specific Roll Number")
        print("7) Check for Duplicates")
        print("8) Show Data in console")
        print("9) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert_student_data()
        elif choice == '2':
            update_student_data()
        elif choice == '3':
            delete_student_data()
        elif choice == '4':
            marks_student()
        elif choice == '5':
            delete_or_update_marks()
        elif choice == '6':
            roll_no = input("Enter Roll Number to retrieve: ")
            retrieve_specific_roll_number(roll_no)
        elif choice == '7':
            roll_no = input("Enter Roll Number to check for duplicates: ")
            if check_duplicates(roll_no):
                print("Duplicate found.")
            else:
                print("No duplicate found.")
        elif choice == '8':
            show_data()
        elif choice == '9':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
