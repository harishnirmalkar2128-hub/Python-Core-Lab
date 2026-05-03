import os

# 1. Current working directory check karna
print("Abhi hum is location par hain:", os.getcwd())

# 2. Naya folder banana (Agar pehle se nahi hai)
folder_name = "Automation_Test"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"'{folder_name}' folder ban gaya! ✅")
else:
    print("Folder pehle se bana hua hai. 📂")

# 3. List all files (Is folder mein kya kya hai)
print("Files in current directory:", os.listdir())