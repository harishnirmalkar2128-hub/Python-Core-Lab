# --- 1. FOR LOOP (Counting 1 to 5) ---
print("For Loop Table:")
for i in range(1, 6): # 1 se shuru, 6 se pehle khatam
    print("Step Number:", i)

# --- 2. WHILE LOOP (Condition based) ---
print("\nWhile Loop Countdown:")
count = 3
while count > 0:
    print("Counting down...", count)
    count -= 1 # Har baar 1 kam karo (nathi toh infinite loop ho jayega!)
print("Blast off! 🚀")

# --- 15-Min Drill: Multiplication Table ---
num = int(input("\nKiska table chahiye?: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)