mdict = {}
while True:
    studentNo = input("Enter a unique student number: ")
    studentNo = studentNo.upper()
    studentName = input("Enter the student's name: ")
    mdict[studentNo] = [studentName, []]
    while True:
        mark = input("Add a mark (N to finish marks): ")
        if mark[0].upper() == 'N':
            break
        else:
            mdict[studentNo][1].append(eval(mark))
    
    again = input("Do you want to add another student (Y/N)? ")
    if again[0].upper() == 'N':
        break
    
for x in mdict:
    print(x, ":", mdict[x])