#built-in function:
numbers=[11,22,33,44]
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#user-defined function:
def display():
    print("Welcome to Python Programming!")
display()

#function with parameters:
def add(a,b):
    print("sum:", a+b)
    print("mul:", a*b)
add(9,8)

#function with return value:
def square(num):
    return num*num
result=square(10)
print("square:", result)

#function returning multiple values:
def calc(a, b, c, d):
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return add, sub, mul, div
x,y,z,o=calc(9, 5, 6, 4)
print("addition:", x)
print("substraction:", y)
print("multiplication:",z)
print("division:",o)