# Program that takes in a list of marks and outputs a histogram representation of the marks according to the mark categories at UCT
# Matthew Schramm
# 21 april 2022
listMarks = input("Enter a space-separated list of marks:\n")
marks = listMarks.split(" ")
one = 0
twoUp = 0
twoDown = 0
three = 0
fail = 0
for i in range (len(marks)):
    if int(marks[i]) < 50:
        fail+= 1
    elif int(marks[i])  >= 50 and int(marks[i])  <60:
        three += 1
    elif int(marks[i])  >= 60 and int(marks[i])  < 70:
        twoDown += 1
    elif int(marks[i])  >= 70 and int(marks[i])  < 75:
        twoUp += 1
    elif int(marks[i])  >= 75:
        one += 1

print("1 |", "X" * one,sep = "")
print("2+|", "X" * twoUp,sep = "")
print("2-|", "X" * twoDown,sep = "")
print("3 |", "X" * three,sep = "")
print("F |", "X" * fail,sep = "")
