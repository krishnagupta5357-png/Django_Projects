class A:
    def methodA(self):
        print("Method of Class A")
class B(A):
    def methodB(self):
        print("Method of Class B")
class C(A):
    def methodC(self):
        print("Method of Class C")
class D(B, C):
    def methodD(self):
        print("Method of Class D")
d = D()
d.methodA()
d.methodB()
d.methodC()
d.methodD()
