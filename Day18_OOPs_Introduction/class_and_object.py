# 1. Blueprint (Class) banana
class Student:
    # Constructor: Data set karne ke liye
    def __init__(self, name, branch):
        self.name = name     # Attribute
        self.branch = branch # Attribute

    # Method: Kuch action karne ke liye
    def intro(self):
        print(f"Namaste! Mera naam {self.name} hai aur main {self.branch} ka student hoon.")

# 2. Object banana
s1 = Student("Harish", "MCA")
s2 = Student("Aman", "B.Tech")
s3 = Student("Riya", "MBA")
s4 = Student("Sita", "B.Sc")
s5 = Student("Rahul", "M.Tech") 
s6 = Student("Priya", "BCA")    
s7 = Student("Vikram", "M.Sc")  



# 3. Actions perform karna
s1.intro()
s2.intro()
s3.intro()
s4.intro()
s5.intro()
s6.intro()
s7.intro()

