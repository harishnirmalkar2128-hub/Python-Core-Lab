from datetime import datetime

# Aaj ki current details
now = datetime.now()

formatted_date = now.strftime("%d-%m-%Y")
formatted_time = now.strftime("%H:%M:%S")

print(f"Date: {formatted_date}")
print(f"Time: {formatted_time}")