try:
    age = -5  # Aap yahan input() bhi use kar sakte hain
    
    if age < 0:
        # Jab age negative ho, error raise karo
        raise ValueError("Bhai, age negative nahi ho sakti! ❌")
    elif age == 0:
        print("Aap abhi paida hue hain! 👶")
    elif age < 18:
        print("Aap abhi bachche hain! 🧒")
    elif age < 60:
        print("Aap ek jawaan hain! 💪")
    else:
        print("Aap senior citizen hain! 👴")

except ValueError as e:
    # Jo error humne raise kiya tha, wo yahan handle hoga
    print(f"Error pakda gaya: {e}")