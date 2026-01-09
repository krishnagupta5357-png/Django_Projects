Students = {"101": "Krishna", "102": "Priyam", "103": "Karan", "104": "Siddarth", "105": "Prem", "106": "Prince", "107": "Krish"}
try:
    SID = input("Enter Student ID:")
    print("STUDENT NAME:", Students[SID])
except KeyError:
    print("Error: Student ID not Found.")