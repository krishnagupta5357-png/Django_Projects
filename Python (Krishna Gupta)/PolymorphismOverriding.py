class animal:
    def speak(self):
        print("The Animal Makes A Sound")
class dog(animal):
    def speak(self):
        print("The Dog Barks")
class cat(animal):
    def speak(self):
        print("The Cat Meows")
a = animal()
d = dog()
c = cat()
a.speak()
d.speak()
c.speak()