class grandparent:
    def house(self):
        print("Grandparent's House")
class parent(grandparent):
    def car(self):
        print("Parent's House")
class child(parent):
    def bike(self):
        print("Child's Bike")
c = child()
c.house()
c.car()
c.bike()