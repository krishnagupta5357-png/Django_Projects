class parent:
    def show(self):
        print("Parent Class")
class child1(parent):
    def feature1(self):
        print("Child1 Feature")
class child2(parent):
    def feature2(self):
        print("Child2 Feature")
c1 = child1()
c2 = child2()
c1.show()
c2.show()
c1.feature1()
c2.feature2()
