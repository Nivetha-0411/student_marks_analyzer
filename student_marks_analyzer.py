name=input("Student Name:")
mark1=int(input("Enter the mark 1:"))
mark2=int(input("Enter the mark 2:"))
mark3=int(input("Enter the mark 3:"))
total=mark1+mark2+mark3
avg=total/3
if avg >= 90:
    grade="O"
elif avg >= 80:
    grade="A"
elif avg >=70:
    grade="B"
elif avg>=60:
    grade="C"
else :
    grade="F"
print("\n------Report Card------")
print("Name:",name)
print("Total:",total)
print("average:",avg)
print("Grade:",grade)
