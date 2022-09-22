"""
WAP to create a nested Dictionary of Student ,
In which the keys is the student name and the value is a nested Dictionary of the marks they have secured
in Test,LAB and Assignment.

Example :      Student =
{"JACK" : {"assignment" : [80, 50, 40, 20],"test" : [75, 75],"lab" : [78.20, 77.20]} ,
 "james" : { "assignment" : [82, 56, 44,45],"test" : [80, 80],"lab" : [67.90, 78.72]}}
"""
final_dict = {}
a_marks_dict = {}


stud_count = int(input("how many students do you have : "))

for i in range(0, stud_count):
        stud_name = input("enter student name ")
        assign_list = []
        test_list = []
        lab_list = []
        for j in range(1,5):
                assign_marks = int(input(f"enter assignment {j} marks "))
                assign_list.append(assign_marks)
        for k in range(1,3):
                test_marks = int(input(f"enter test {k} marks "))
                test_list.append(test_marks)
        for l in range(1,3):
                lab_marks = float(input(f"enter lab {l} marks "))
                lab_list.append(lab_marks)
        a_marks_dict["assignment"] = assign_list
        a_marks_dict["test"] = test_list
        a_marks_dict["lab"] = lab_list
        final_dict[stud_name] = a_marks_dict

print(final_dict)

