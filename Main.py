from System import System,Student
from Helper import *

def main():
    main_system = System()
    userAction = 0
    #adding a new user
    while(True):
        printMenu()
        userAction = int(input("Enter an option [1-6]: \n"))
        if(userAction == 1):
            new_student = add_new_user()
            main_system.add_new_student(new_student)
        elif(userAction == 2):
            student_no = get_student_no()
            main_system.delete_student(student_no)
        elif(userAction == 3):
            student_no = get_student_no()
            new_value, operation_type = modify_menu()
            main_system.modify_student_record(student_no, operation_type, new_value)            
        elif(userAction == 4):
            student_no = get_student_no()
            main_system.get_student_by_num(student_no)
        elif(userAction == 5):
            birth_year = get_student_birth_year()
            main_system.get_student_by_birth_year(birth_year)
        elif(userAction == 6):
            main_system.display_all_students()
if __name__ == "__main__":
    main()