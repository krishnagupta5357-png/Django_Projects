class father:
    def skills(self):
        print("Gardening, Programming")
class mother:
    def talents(self):
        print("Painting, Cooking")
class child(father, mother):
    def hobbies(self):
        print("Reading")
child = child()
child.skills()
child.talents()
child.hobbies()