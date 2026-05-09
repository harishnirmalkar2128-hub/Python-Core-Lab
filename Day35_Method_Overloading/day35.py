class Calculator:
    # Python mein overloading default arguments se hoti hai
    def add(self, a, b, c = 0):
        result = a + b + c
        return result

# Object banana
obj = Calculator()

# 1. Do numbers ke saath call karna
print("Sum of 2 numbers:", obj.add(10, 20))

# 2. Teen numbers ke saath call karna
print("Sum of 3 numbers:", obj.add(10, 20, 30))