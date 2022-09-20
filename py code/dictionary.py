# Given the grades dictionary provided previously
# {'John': 90, 'Paul': 84, 'Ben': 70, 'Tony': 35, 'Kate': 100}
#
# Create a program that enables the user to choose one of the options:
# See the grade of someone by providing a name
# Add a new student and grade
# Change a grade given a name of an existing student
# List all the grades in the dictionary
#
# Each of the options needs to be implemented as a different function.

def printMenu():
    print("What do you want to do? Here are the options:")
    print("1. see grade by name")
    print("2. add new student with grade")
    print("3. change grade by name")
    print("4. list all students' grades")
    print("5. exit")


def getGrade(myDic, name):
    return myDic.get(name, -1)


def add(myDic, name, grade):
    myDic[name] = grade


def listAll(myDic):
    for student in myDic:
        print(student, "\t", myDic[student])


def main():
    myDic = {'John': 90, 'Paul': 84, 'Ben': 70, 'Tony': 35, 'Kate': 100}
    printMenu()
    op = int(input("Choose your option: "))
    while op != 5:
        if op == 1:  # see the grade by name
            name = input("What's the name of the student? ")
            grade = getGrade(myDic, name)
            if grade != -1:
                print("The student's grade is", grade)
            else:
                print("Student not found")
        elif op == 2:  # add new student with grade
            name = input("What's the name of the student? ")
            grade = int(input("What's the student's grade? "))
            add(myDic, name, grade)
        elif op == 3:  # change grade by name
            name = input("What's the name of the student? ")
            grade = getGrade(myDic, name)
            if grade != -1:
                print("The student's current grade is", grade)
                grade = int(input("What's the student's NEW grade? "))
                add(myDic, name, grade)
            else:
                print("Student not found")
        elif op == 4:  # list all students' grades
            listAll(myDic)
        else:
            print("Invalid option, please choose an option between 1 and 5")
        op = int(input("Choose your option: "))
    else:
        print("The app is now closed")


main()