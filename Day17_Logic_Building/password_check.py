# Simple Logic: Checking if password is secure
password = input("Ek naya password dalo: ")

# len() function characters count karta hai
if len(password) >= 8:
    print("Mubarak ho! Ye ek strong password hai. ✅")
else:
    print("Oops! Password kam se kam 8 characters ka hona chahiye. ❌")