# Function for greeting
def welcome_msg(name):
    return "Hello " + name + "! Main aapka personal assistant hoon."

# Main Logic
user_name = input("Aapka naam kya hai? ")
print(welcome_msg(user_name))

while True:
    print("\n1. Calculate Age\n2. Health Tip\n3. Exit")
    choice = input("Kya karna chahenge? (1/2/3): ")

    if choice == '1':
        birth_year = int(input("Birth year dalo: "))
        print("Aapki age approx", 2026 - birth_year, "hai.")
    elif choice == '2':
        print("Tip: Fever ke baad khoob paani piyo aur fruits khao! 🍎")
    elif choice == '3':
        print("Alvida! Kal milte hain.")
        break
    else:
        print("Galat option, firse try karo.")