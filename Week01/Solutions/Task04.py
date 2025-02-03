courses = []
print()

while True:
    course = input("Enter a course you have studied (leave empty to finish): ")
    if course == '':
        break
    courses.append(course)

if courses:
    print("The last course you entered is: %s" % courses[-1])
else:
    print("No courses were entered.")
