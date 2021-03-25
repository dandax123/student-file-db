from Student import Student
modify_operations = ["first_name", "last_name", "gender", "date_of_birth", "country_of_birth"]
modify_operations_label = ["First Name", "Last Name", "Gender", "Date Of Birth", "Country of Birth"]
def add_new_user():
    student_no = int(input("Enter your Student No: \n"))
    first_name=input("Enter your first name: \n")
    last_name=input("Enter your last name: \n")
    gender=input("Enter your gender[M-F]: \n")
    date_of_birth=input("Enter your date of birth(dd-mm-yyyy): \n")
    country_of_birth=input("Enter your country of birth: \n")
    new_student = Student(student_no, first_name, last_name, gender, date_of_birth, country_of_birth)
    return new_student

def get_student_no():
    student_no=int(input("Enter your Student No: \n"))
    return student_no

def get_new_value(modifyAction):
    new_value = input(f"Enter the new value for {modify_operations_label[modifyAction-1]}\n")
    return new_value

def modify_menu():
    print("Enter the Field to be modified\n")
    for i in range(0, len(modify_operations_label)):
        print(f"{i+1} {modify_operations_label[i]}\n")
    modifyAction = int(input("Enter the operation you want to perform [1-5] \n"))
    operation_type = modify_operations[modifyAction-1]
    new_value = get_new_value(modifyAction)
    return new_value, operation_type


def get_student_birth_year():
    birth_year = int(input("Enter the birth year: \n"))
    return birth_year    
def printMenu():
    print("Welcome to Student Menu \n")
    print("Enter the number for the instructions\n")
    print("1. Add new Student \n")
    print("2. Delete Student \n")
    print("3. Modify Student records \n")
    print("4. Find Student by No \n")
    print("5. Finds Students by Birth Year \n") 
    print("6. Display all Students \n")