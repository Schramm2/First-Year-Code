item = ""
counter = 1
sequence = ""
numbers = ""
position = 0
smallest = 999999999999
while item != "DONE":
    print("Enter item " , counter, ":", sep = "")
    item = input()
    counter += 1
    if item.isdigit() == True:
        numbers += item + str(counter-1) + " "
        if int(item) < int(smallest):
            smallest = item
            position = counter - 1
        
    sequence += str(item)
    sequence += " "
    
counter = counter - 2

sequence = sequence[0:len(sequence)-5]

if numbers == "":
    print("No numerical items.")
else:
    print("Item", position, "is the minimum integer value.")
    
        
    
    
    