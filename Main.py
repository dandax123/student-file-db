from System import System,Student

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
def main():
    main_system = System()
    userAction = 0
    printMenu()
    #adding a new user
    while(True):
        userAction = int(input("Enter an option [1-5]: \n"))
        if(userAction == 1):
            new_student = add_new_user()
            main_system.add_new_student(new_student)
        elif(userAction == 2):
            student_no = get_student_no()
            main_system.delete_student(student_no)
        elif(userAction == 4):
            student_no = get_student_no()
            main_system.get_student_by_num(student_no)
        elif(userAction == 5):
            birth_year = get_student_birth_year()
            main_system.get_student_by_birth_year(birth_year)
        elif(userAction == 6):
            main_system.display_all_students()
        printMenu()
if __name__ == "__main__":
    main()