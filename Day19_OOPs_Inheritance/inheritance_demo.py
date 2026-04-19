# 1. Parent Class (Basic Features)
class Phone:
    def call(self):
        print("Calling... 📞")

# 2. Child Class (Extra Features + Parent Features)
class SmartPhone(Phone): # Bracket mein 'Phone' likhne se inheritance hota hai
    def camera(self):
        print("Photo clicked! 📸")

# 3. Object banana
my_phone = SmartPhone()

my_phone.call()   # Purana feature (Parent se aaya)
my_phone.camera() # Naya feature (Child ka apna hai)