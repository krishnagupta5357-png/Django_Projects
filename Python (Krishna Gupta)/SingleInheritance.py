class animal:
    def speak(self):
        print("Animal Speaks")
class dog(animal):
    def bark(self):
        print("Dog Barks")
dog = dog()
dog.speak()
dog.bark()