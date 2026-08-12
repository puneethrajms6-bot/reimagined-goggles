def get_marks(subjects):
    marks = []
    for subject in subjects:
        while True:
            try:
                value = float(input(f"{subject} marks:"))
                if 0 <= value <= 100:
                    marks.append(value)
                    break
                print("Enter marks from 0 to 100.")
            except ValueError:
                print("Numbers only.")
    return marks
def grade(avg): 
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    return "F"
subjects = ["Maths","Python","DBMS","English","Aptitude"]
name = input("Student name:").strip()
marks = get_marks(subjects)
total = sum(marks)
average = total/len(marks)
status = "PASS"if all(x >= 35 for x in marks)else "FAIL"
print("\n----RESULT----")
print("Name:",name.title())
for subject,mark in zip(subjects,marks):
    print(f"{subject:<10}:{mark:.2f}")
    print(f"Total:{total:.2f}")
    print(f"Average:{average:2f}%")
    print("Grade:",grade(average))
    print("Status:",status)
    print("Highest:",subjects[marks.index(max(marks))])
    print("Lowest:",subjects[marks.index(min(marks))])    
