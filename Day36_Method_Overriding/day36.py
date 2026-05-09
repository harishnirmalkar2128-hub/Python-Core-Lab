# 1. Parent Class
class Parent:
    def property(self):
        print("Gold + Zameen + Purani Car 🚗")
    
    def career(self):
        print("Government Job ki taiyari karo! 📝")

# 2. Child Class (Inherit kar raha hai)
class Child(Parent):
    # Career function ko override kar rahe hain
    def career(self):
        print("Nahi, mujhe Software Engineer banna hai! 💻🚀")

# 3. Object banana
obj = Child()

# Property wahi milegi jo parent ki hai (Inheritance)
obj.property() 

# Career wala method override ho chuka hai (Overriding)
obj.career()