# File Handling in Python


# 1. 'with' keyword file ko apne aap close kar deta hai
# 'r' ka matlab hai Read mode
with open("example.txt", "r") as file:
    content = file.read()
    print("File ka data ye hai:")
    print(content)

# 2. Line by line read karna (Large files ke liye)
with open("example.txt", "r") as file:
    print("\nLine by line reading:")
    for line in file:
        print(line.strip()) # .strip() extra spaces/newlines hatata hai