# Parent Class 1
class Camera:
    def take_photo(self):
        print("Photo khich li! 📸")

# Parent Class 2
class MusicPlayer:
    def play_music(self):
        print("Gaane chal rahe hain... 🎵")

# Child Class (Dono se inherit kar raha hai)
class SmartPhone(Camera, MusicPlayer):
    def show_features(self):
        print("Main ek Smartphone hoon!")

# Object banana
my_phone = SmartPhone()

# Dono parents ke methods access karna
my_phone.show_features()
my_phone.take_photo()    # Camera se aaya
my_phone.play_music()    # MusicPlayer se aaya