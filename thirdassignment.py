# (1) Write a function that return bool type

# bool

pass_mark = 50
user_score = 50 

def pass_fail():

    if user_score >= pass_mark:
       student_passed = True
    else:
       student_passed = False

    if student_passed:
       print("student passed")
    else:
       print("student did not pass")        

pass_fail()

# (2) Write a Python function that takes 10 lists and returns True if they have
# at least one common member

list1 = [1, 2, 89]
list2 = [4, 5, 88]
list3 = [29, 27, 7]
list4 = [17, 10, 4]
list5 = [11, 12, 67]
list6 = [7, 14, 15]
list7 = [16, 17, 17]
list8 = [76, 0, 21]
list9 = [22, 77, 24]
list10 = [25, 71, 23]

lists_with_7 = [lst for lst in [list1, list2, list3, list4, list5, list6, list7, list8, list9, list10] if 7 in lst]
print(bool(lists_with_7))

# (3) write a python function that takes the name of student,and calculates their ages.
# If the age is greater or equal to 18, it should return true, else false.

stud_name = input("Enter your name; ")
age = int(input("Input your age; "))

print(stud_name)
print(age)

def age_calcular():

    if age >= 18:
        print(True)
    else:
        print(False)

age_calcular()