# 1. Basic Try-Except
try:
    number = int(input("Ek number dalo: ")) # Agar user 'abc' likh de toh?
    result = 10 / number
    print("Result is:", result)

except ValueError:
    # Jab data type galat ho
    print("Error: Bhai, sirf number likhna tha, text nahi! ❌")

except ZeroDivisionError:
    # Jab kisi number ko 0 se divide karein
    print("Error: Aap kisi number ko 0 se divide nahi kar sakte! ❌")

except Exception as e:
    # Koi bhi aur anjan error
    print("Kuch toh gadbad hai:", e)

finally:
    # Ye block hamesha chalega (Chai break ki tarah)
    print("Kaam khatam! Program band nahi hua. ✅")