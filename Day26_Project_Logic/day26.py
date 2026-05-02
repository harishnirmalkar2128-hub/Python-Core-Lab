def analyze_mood(text):
    text = text.lower()
    if "good" in text or "happy" in text or "achha" in text:
        return "Positive Mood! 😊"
    elif "sad" in text or "bad" in text or "tension" in text:
        return "Needs Support. 😐"
    else:
        return "Neutral. 👍"

user_thought = input("Aaj aap kaisa feel kar rahe hain? ")
print(analyze_mood(user_thought))