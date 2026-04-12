# --- Simple Voting System ---
age = int(input("Apni age batao: "))

if age >= 18:
    print("Aap Vote de sakte hain! ✅")
    print("Desh badalne mein madad karein.")
elif age == 17:
    print("Bas ek saal aur rukiye! ⏳")
else:
    print("Aap abhi chote hain. 👶")
    print("Wait for", 18 - age, "years.")