age=20
citizen="yes"

if age>=18:
    if citizen=="yes":
        print("you can vote")
    else:
        print("only citizen can vote")
else:
    print("you are too young to vote")