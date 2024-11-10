# Program to take in a list of strings and then print them all out right-aligned with the longest string
# Matthew Schramm
# 21 april 2022
listOfStrings = []
userString = ""
counter = 0
length = 0
print("Enter strings (end with DONE):")
while userString != "DONE":
    if len(userString) > length and userString != "DONE":
        length = len(userString)
    userString = input()
    listOfStrings.append(userString)
    counter += 1
    
del listOfStrings[counter-1]

counter -= 1


print("\nRight-aligned list:")
for i in range(0, counter):
    for z in range( 0, length - len(listOfStrings[i])):
        print(" ", end = "", sep = "")
    print(listOfStrings[i])                
    
    