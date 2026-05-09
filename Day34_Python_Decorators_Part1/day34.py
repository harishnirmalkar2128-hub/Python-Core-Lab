# 1. Decorator function banana
def my_decorator(func):
    def wrapper():
        print("--- Function shuru hone se pehle ka kaam ---")
        func() # Asli function yahan call ho raha hai
        print("--- Function khatam hone ke baad ka kaam ---")
    return wrapper

# 2. Decorator use karna (@ symbol ke saath)
@my_decorator
def say_hello():
    print("Hello Harish! You pass the first step. 🚀")

# 3. Function call karna
say_hello()