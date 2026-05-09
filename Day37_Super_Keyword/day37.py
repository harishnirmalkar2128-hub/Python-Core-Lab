# 1. Parent Class
class Computer:
    def __init__(self, brand):
        self.brand = brand
        print(f"Computer ({self.brand}) initialized.")

# 2. Child Class
class Laptop(Computer):
    def __init__(self, brand, ram):
        # Parent ka constructor call kar rahe hain
        super().__init__(brand) 
        self.ram = ram
        print(f"Laptop with {self.ram}GB RAM is ready.")

    def show_specs(self):
        print(f"Brand: {self.brand}, RAM: {self.ram}")

# 3. Object banana
my_laptop = Laptop("Intel Core Ultra", 16)
my_laptop.show_specs()