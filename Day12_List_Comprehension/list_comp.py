# --- Normal Way (Using Loop) ---
numbers = [1, 2, 3, 4, 5, 6]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print("Normal List:", evens)

# --- List Comprehension Way (Professional) ---
# Syntax: [expression for item in list if condition]
pro_evens = [n for n in numbers if n % 2 == 0]
print("Pro List:", pro_evens)

# --- Ek aur example: Square of numbers ---
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares) # Output: [1, 4, 9, 16, 25]