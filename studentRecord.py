#Python program to
# 1. Read the names and total marks scored by students of a class of atleast 3 or more studentRanks
# 2. Rank the top 3 students of the class
# 3. Provide a cash reward of $500 to the student who secured first rank, $300 to student who secured second rank and $100 to student who secured third rank. (The cash value cannot be modified)
# 4. Make a statement of appreciation to students who secured above 950 marks and above.

import operator

# get student record
def getstudentrecord():
        studentRecord = {}
        print("Enter no. of students:")
        num = int(input())
        for count in range(0,num):
            print("Enter name of student {}:".format(count+1))
            name = input()
            print("Enter marks of {}:".format(name))
            marks = int(input())
            studentRecord[name] = marks
            print()
        return studentRecord

#give ranks
def studentRanks(studentRecord):
    try:
        sortedstudentrecord = sorted(studentRecord.items(), key = operator.itemgetter(1), reverse = True)
        print("{} gets Rank 1 with score of {}" .format(sortedstudentrecord[0][0], sortedstudentrecord[0][1]))
        print("{} gets Rank 2 with score of {}" .format(sortedstudentrecord[1][0], sortedstudentrecord[1][1]))
        print("{} gets Rank 3 with score of {}" .format(sortedstudentrecord[2][0], sortedstudentrecord[2][1]))
        print()
        return sortedstudentrecord
    except IndexError:
        print("Enter min of 3 students")
        quit()



#reward students
def awardStudents(sortedStudentRecord):
    for count in range (0,3):
        print("{} gets reward of ${}".format(sortedStudentRecord[count][0], reward[count]))

def studentAppreciation(sortedrecord):
    print()
    print("Congratulations! The students below have scored above 950")
    for count in range(0,4):
        if sortedrecord[count][1] >= 950:
            print(sortedrecord[count][0])


record = getstudentrecord()
sortedRecord = studentRanks(record)
reward =("500","300","100")
awardStudents(sortedRecord)
studentAppreciation(sortedRecord)
