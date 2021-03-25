from Student import Student
from Helper import modify_operations

class System:
    def __init__(self, input_file = None):
        #this contains the list of all students 
        self.students  = []
    
    
    def get_student_by_birth_year(self, birth_year):
        birth_year_matches = []
        for std in self.students:
            if(std.get_birth_year == birth_year):
                birth_year_matches.append(std)
        self.display_students_info(birth_year_matches)
        return birth_year_matches
    
    def delete_student(self, student_no):
        is_student_exist = self.get_student_by_num(student_no)
        if(is_student_exist == -1):
            print("Student Not found!!!")
            
        self.students.pop(is_student_exist)
        print("Student deleted successfully\n\n")
        
    def modify_student_record(self,student_no, type, new_value):
        student_index =self.get_student_by_num(student_no)
        if(student_index == -1):
            #print not found
            return -1
        operation_type = f"set_{type}" 
        modify_operation = getattr(self.students[student_index], operation_type)
        modify_operation(new_value)
    def get_student_by_num(self, student_no):
        isFound = -1
        for i in range(0, len(self.students)):
            if(self.students[i].get_student_no() == student_no):
                print("Student Info: \n")
                print(self.students[i].display_info())
                #print student info and break return std
                isFound = i
        if(isFound == -1):
            print("Student not found!!!")
        return isFound
    
    def add_new_student(self, student):
        if(len(self.students) >=100):
            print("Students array is full!!!")
        else:
            self.students.append(student)
            print("Student added successfully\n\n")
    def display_all_students(self):
        self.display_students_info()
    def display_students_info(self, students=None):
        print("Students Info")
        if(students):
            for std in students:
                print(std.display_info())
                print("----------------------")
        else:
            for std in self.students:
                print(std.display_info())
                print("----------------------")
    
