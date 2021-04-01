from Student import Student
class File:
    def __init__(self,file_name):
        self.file_name = file_name
    def store_contents(self,students):
        with open(self.file_name,'w',encoding = 'utf-8') as f:
            for std in students:
                student_file_format = std.get_file_format()
                f.write(f"{student_file_format}\n") 
        f.close()
        print("Stored content in file successfully")
    def read_contents(self):
        students = []
        f = open(self.file_name,'r',encoding = 'utf-8')
        for line in f:
            student_data = line.split("~")
            if(len(student_data) > 1):
                std_x = Student(int(student_data[0]), student_data[1], student_data[2], student_data[3], student_data[4], student_data[5])
                students.append(std_x)
        f.close()
        return students 
