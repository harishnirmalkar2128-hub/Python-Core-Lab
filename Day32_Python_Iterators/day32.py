# Ek simple list banate hain
my_list = ["Python", "AWS", "Azure", "SQL"]

# 1. List ko iterator mein convert karna
my_iterator = iter(my_list)

# 2. Ek-ek karke element nikalna next() se
print(next(my_iterator)) # Output: Python
print(next(my_iterator)) # Output: AWS
print(next(my_iterator)) # Output: Azure

# 3. For loop bhi piche se iterator hi use karta hai
print("\nLooping through remaining items:")
for item in my_iterator:
    print(item) # Output: SQL (kyunki baaki hum upar nikal chuke hain)