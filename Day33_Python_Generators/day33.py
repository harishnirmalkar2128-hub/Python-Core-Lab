# 1. Generator Function banana (yield use hota hai)
def my_generator():
    yield "Pehla Task"
    yield "Dusra Task"
    yield "Tisra Task"

# 2. Generator object banana
gen = my_generator()

# 3. Ek-ek karke value nikalna (Memory efficient)
print(next(gen)) # Output: Pehla Task
print(next(gen)) # Output: Dusra Task

# 4. Generators ko loop mein bhi use kar sakte hain
print("\nLooping through remaining:")
for task in gen:
    print(task)