# 1. WRITING (Purana data delete ho jayega)
with open("tasks.txt", "w") as file:
    file.write("Python Day 14: File Writing\n")
    file.write("Task 1: Learn 'w' mode\n")
print("File created and data written!")

# 2. APPENDING (Niche naya data judega)
with open("tasks.txt", "a") as file:
    file.write("Task 2: Learn 'a' mode for adding data\n")
    file.write("Task 3: Practice coding\n")
print("New data appended successfully!")

# 3. Reading to verify
with open("tasks.txt", "r") as file:
    print("\nUpdated File Content:\n", file.read())