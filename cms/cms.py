# Student management system 
#create a student cla# Student management system 
#create a student class
class Students:
    def __init__(self, name, roll, cgpa, department):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa
        self.department = department 
    
    #display students information 
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")
        print(f"CGPA: {self.cgpa}")
        print(f"DEP: {self.department}")
        print(f"Status: {self.is_honors()}")
        
    #identify honors/regular 
    def is_honors(self):
        if self.cgpa >= 3.5:
            return "Honors Student"
        else:
            return "Regular student"
            

#Create GraduateStudents class. Inheritance to Students class
class GraduateStudents(Students):
    #add new property thesis_topic
    def __init__(self, name, roll, cgpa, department, thesis_topic):
        super().__init__(name, roll, cgpa, department)  
        self.thesis_topic = thesis_topic

    def display_info(self):
        super().display_info()
        print(f"Thesis Topic: {self.thesis_topic}")


#==========Create objects==================
print("\n-----Student1------")
s1 = Students("MD Abdur Rohoman(Zehad)", 19, 4.00, "CST")
s1.display_info()
print("\n----Student2--------")
s2 = Students("Khalid Bin Olid(Khalid)",102,3.80,"ET")
s2.display_info()
print("\n------Students3-----")
s3 = Students("Mohammad Obydul(Obydul)",103,3.50,"ET")
s3.display_info()
print("\n-----Student4-----")
s4 = GraduateStudents("Abid",104,3.20,"CST","Web developer")
s4.display_info()
