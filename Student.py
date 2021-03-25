class Student(object):
    def __init__(self, student_no, first_name, last_name, gender, date_of_birth, country_of_birth):
        self.student_no = student_no
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.country_of_birth = country_of_birth
        self.gender  = gender
    def __str__(self):
        return str(self.student_no)
    
    def get_name(self):
        return self.first_name + " " +self.last_name
    
    def get_student_no(self):
        return int(self.student_no)
    def get_gender(self):
        if(self.gender == 'M'):
            return "Male"
        else:
            return "Female"
    def get_student_age(self):
        return int(2021-self.get_birth_year())
    def set_first_name(self, first_name):
        self.first_name = first_name
    def get_birth_year(self):
        return int(self.date_of_birth[6:10])
    def get_date_of_birth(self):
        return self.date_of_birth
    def get_country_of_birth(self):
        return self.country_of_birth
    def display_info(self):
        print("Name: \t\t" + self.get_name() + "\n")
        print("Student No: \t" + str(self.get_student_no()) + "\n")
        print("Age: \t\t" + str(self.get_student_age()) + "\n")
        print("Gender: \t" + self.get_gender() + "\n")
        print("Date Of Birth: \t" + self.get_date_of_birth() + "\n")
        print("Country Of Birth: " + self.get_country_of_birth() + "\n")
        return ''
        
    def set_last_name(self, last_name):
        self.last_name = last_name
        
    def set_gender(self, gender):
        self.gender = gender 


# student1 = Student(18701850, "daniel", "test", "M", "12-07-2000", "ng")
# print(student1.display_info())