user_profile = {
    "name": "Harish",
    "role": "Cloud Engineer",
    "target": "UAE"
}

# Sari keys aur values nikalna
print("Keys:", list(user_profile.keys()))
print("Values:", list(user_profile.values()))

# Safe tarike se data access karna
skill = user_profile.get("skill", "Python (Default)")
print(f"Skill: {skill}")