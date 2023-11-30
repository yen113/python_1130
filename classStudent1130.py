class Student:

    def __init__ (self, schoolName, schoolAddres, department, leadername, studentname, id, studentaddres, credit, gpa):
        self.schoolName = schoolName
        self.schoolAddres = schoolAddres
        self.department = department
        self.leadername = leadername
        self.studentname = studentname
        self.id = id
        self.studentaddres = studentaddres
        self.credit = credit
        self.gpa = gpa


    def get_schoolName(self):
        return self.schoolName
    def set_schoolName(self, new_schoolName):
        self.schoolName = new_schoolName

    def get_schoolAddres(self):
        return self.schoolAddres
    def set_schoolAddres(self, new_schoolAddres):
        self.schoolAddres = new_schoolAddres

    def get_department(self):
        return self.department
    def set_department(self, new_department):
        self.department = new_department

    def get_leadername(self):
        return self.leadername
    def set_leadername(self, new_leadername):
        self.leadername = new_leadername

    def get_studentname(self):
        return self.studentname
    def set_studentname(self, new_studentname):
        self.studentname = new_studentname
        
    def get_id(self):
        return self.id
    def set_id(self, new_id):
        self.id = new_id
        
    def get_studentaddres(self):
        return self.studentaddres
    def set_studentaddres(self, new_studentaddres):
        self.studentaddres = new_studentaddres
        
    def get_credit(self):
        return self.credit
    def set_credit(self, new_credit):
        self.credit = new_credit
        
    def get_gps(self):
        return self.gps
    def set_gpa(self, new_gps):
        self.gps = new_gps
        

student1 = Student("stust", "NTS#1", "Department of Computer Science and Information Engineering", "Gwo-Jiun Horng", "Fen-Yen Kong", "4b0g0007", "4B0G0007@stust.edu.tw", "0", "0")
print(student1.get_schoolName())

student1.set_schoolName("南台科大")
print(student1.get_schoolName())