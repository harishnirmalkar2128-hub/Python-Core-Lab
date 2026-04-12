# Grade Checker for Multiple Students
marks = [85, 40, 92, 28, 65]

print("Result Analysis:")
for m in marks:
    if m >= 33:
        status = "PASS ✅"
    else:
        status = "FAIL ❌"
    print(f"Marks: {m} | Status: {status}")

# Action: Check if 92 is the topper
print("\nMax Marks:", max(marks))