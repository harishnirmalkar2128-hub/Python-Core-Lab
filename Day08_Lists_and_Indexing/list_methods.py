# 1. List banana
skills = ["Python", "DBMS", "Cloud"]

# 2. Item access karna (Counting 0 se shuru hoti hai)
print("Pehli skill:", skills[0]) 

# 3. Nayi skill add karna
skills.append("AWS")
print("Updated Skills:", skills)

# 4. List ki length check karna
print("Total skills:", len(skills))

# 5. Loop ke saath list print karna
print("\nMy Learning Path:")
for s in skills:
    print("- " + s)



    # --- List Operations ---
goals = ["UAE Job", "Weight Gain", "Cloud Expert"]

# 1. Accessing items (Index 0 se start hota hai)
print("Primary Goal:", goals[0]) 

# 2. Modifying items
goals[1] = "Fit Body" # "Weight Gain" ko "Fit Body" se badal diya

# 3. Adding new items
goals.append("Python Pro") # List ke end mein add hoga

# 4. Removing items
goals.remove("Fit Body")

print("\nUpdated Goal List:")
for goal in goals:
    print("- " + goal)

# --- 15-Min Drill ---
# Ek list banao 'days' naam ki aur usme 1 se 7 numbers dalo.
# Phir 'reverse()' function use karke use ulta print karo.