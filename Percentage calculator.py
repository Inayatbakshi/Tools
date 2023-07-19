marks = float(input("enter the obtained marks: "))
max_marks = float(input("enter the maximum marks: "))

percent = round(marks / max_marks * 100, 2)

print(f"you've got {percent}%")