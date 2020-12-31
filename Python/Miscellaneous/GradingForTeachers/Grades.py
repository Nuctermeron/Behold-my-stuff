from art import text2art

#Welcome screen
print(text2art("AutoGrades"))
print("Welcome teacher!\n")

student_list = {}

should_stop = False

student_name = input("What's student name?\n")
student_score = int(input("What's student score?\n"))
student_detail = {student_name:student_score}
student_list.update(student_detail)

while not should_stop:
    choice = input("Write stop to end or hit enter to continue\n")
    if choice.lower() == "stop":
        should_stop = True
    else:
        student_name = input("What's student name?\n")
        student_score = int(input("What's student score?\n"))
        student_detail = {student_name:student_score}
        student_list.update(student_detail)

for key in student_list:
    if student_list[key] > 90:
        print(f"{key} got 6")
    elif student_list[key] > 75:
        print(f"{key} got 5")
    elif student_list[key] > 60:
        print(f"{key} got 4")
    elif student_list[key] > 50:
        print(f"{key} got 3")
    elif student_list[key] > 30:
        print(f"{key} got 2")
    else:
        print(f"{key} got 1")
