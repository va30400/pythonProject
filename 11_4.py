"""
WAP to input the Student Name as Key and the marks as Value ,
if the marks secured by the student is >=75 then Store it in Dict A ,
 if the marks secured by student in <75 and >= 50 then store it in Dict B
 else Store the it in Dict C.

"""

dict_a = {}
dict_b = {}
dict_c = {}

stud_count = int(input("how many students do you have : "))

for i in range(0, stud_count):
    stud_name = input("enter student name ")
    assign_marks = int(input("enter exam marks "))
    if assign_marks >= 75:
        dict_a[stud_name] = assign_marks
    elif assign_marks >= 50:
        dict_b[stud_name] = assign_marks
    else:
        dict_c[stud_name] = assign_marks

print(dict_a , " ", dict_b , " ", dict_c)
