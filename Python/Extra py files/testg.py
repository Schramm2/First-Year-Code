listOfNumbers = ""
num = ""
counter1 = 0
while num != "END":
    num = input("Enter an integer (or 'END'):\n")
    listOfNumbers += num+","
    counter1 += 1
    
    
listOfNumbers = listOfNumbers[0: len(listOfNumbers)-5]
listOfNumbers += ","

counter2 = 0
for i in range(0,counter1-2):
    num1 = listOfNumbers[0:listOfNumbers.find(",")]
    num1 = int(num1)
    
    num2 = listOfNumbers[listOfNumbers.find(",")+1:listOfNumbers.find(",",5)]
    num2 = int(num2)        
    
    
    if num1 <= num2:
        counter2 += 1
        listOfNumbers = listOfNumbers[listOfNumbers.find(",")+1:len(listOfNumbers)]
        
    else:
        listOfNumbers = listOfNumbers[listOfNumbers.find(",")+1:len(listOfNumbers)]
        
print("Pairs of adjacent numbers where 2nd at least as large as 1st:",counter2)


