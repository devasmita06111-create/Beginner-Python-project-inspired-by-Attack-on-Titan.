tamil = int(input("tamil mark: "))
english = int(input("english mark: "))
maths = int(input("maths mark: "))
biology = int(input("biology mark: "))
physics = int(input("physics mark: "))
chemistry = int(input("chemistry mark: "))

total = tamil + english + maths + biology + physics + chemistry
average = total / 6

# Highest & Lowest Subject
marks = [tamil, english, maths, biology, physics, chemistry]
subjects = ["Tamil", "English", "Maths", "Biology", "Physics", "Chemistry"]

max_mark = max(marks)
min_mark = min(marks)
max_sub = subjects[marks.index(max_mark)]
min_sub = subjects[marks.index(min_mark)]

print("\n--- REPORT CARD ---")
print(f"Total = {total} / 600")
print(f"Average = {average:.2f}%")

# ASCII Progress Bar
bar = "█" * int(average // 5)
print(f"Performance: [{bar:<20}] {average:.1f}%")

# Grade System - AOT Style
if average >= 90:
    grade = "S-Rank 🗼"
    msg = "Erwin ah minjirita. Survey Corps Commander!"
elif average >= 75:
    grade = "A-Rank ⚔️"
    msg = "Levi Squad ku select aaita. ODM gear ready pannu!"
elif average >= 60:
    grade = "B-Rank 🛡️"
    msg = "Garrison la seralam. Walls kaapathu!"
elif average >= 50:
    grade = "C-Rank 🍗"
    msg = "Pass aaniya. Sasha kooda potato thinnu celebrate pannu."
else:
    grade = "F-Rank 🧟"
    msg = "Fail. Titan ku food aagatha. Next time padida!"

print(f"Grade = {grade}")
print(msg)

print(f"\nTop Subject: {max_sub} = {max_mark} 🗼")
print(f"Weak Subject: {min_sub} = {min_mark} 🎯")

# Per Subject Fail Check
if tamil < 35 or english < 35 or maths < 35 or biology < 35 or physics < 35 or chemistry < 35:
    print("\nWarning: Oru subject la Arrears da thambi 🚨")