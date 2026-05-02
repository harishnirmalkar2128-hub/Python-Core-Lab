nums = [1, 2, 3, 4, 5, 6]

# Map: Sabka square kar do
squares = list(map(lambda x: x*x, nums)) 
# Filter: Sirf even numbers rakho
evens = list(filter(lambda x: x%2 == 0, nums))

print(f"Squares: {squares}\nEvens: {evens}")