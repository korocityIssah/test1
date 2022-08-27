def average():
    return (Student.marks[0] + Student.marks[1] + Student.marks[2] + Student.marks[3] + Student.marks[4]) / 5


def total():
    return Student.marks[0] + Student.marks[1] + Student.marks[2] + Student.marks[3] + Student.marks[4]


def percentage():
    return average()/100*50


def displayData():
    print("Name is: ", Student.name)
    # print ("Marks in subject 1: ", Student.marks[0])
    # print ("Marks in subject 2: ", Student.marks[1])
    # print ("Marks in subject 3: ", Student.marks[2])
    print("Marks are: ", Student.marks)
    print("Total Marks are: ", total())
    print("Average Marks are: ", average())
    print("percentage Marks are: ", percentage())


def getData(name, m1, m2, m3, m4, m5):
    Student.name = name
    Student.marks.append(m1)
    Student.marks.append(m2)
    Student.marks.append(m3)
    Student.marks.append(m4)
    Student.marks.append(m5)


class Student:
    marks = []


name = input("Enter the name: ")
m1 = int(input("Enter the marks in the first subject: "))
m2 = int(input("Enter the marks in the second subject: "))
m3 = int(input("Enter the marks in the third subject: "))
m4 = int(input("Enter the marks in the third subject: "))
m5 = int(input("Enter the marks in the third subject: "))

s1 = Student()
getData(name, m1, m2, m3, m4, m5)
displayData()
