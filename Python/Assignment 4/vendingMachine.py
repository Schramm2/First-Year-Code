#Program to simulate the act of a vending machine
#Matthew Schramm SCHMAT041
#2022/03/16

cost = eval(input("Enter the cost (in cents):\n"))
paid = eval(input("Deposit a coin or note (in cents):\n"))


while cost > paid:
    paid += eval(input("Deposit a coin or note (in cents):\n"))

change = paid - cost
if change == 0:
    print()
elif change % 500 == 0:
    changeCoin = int(change/500)
    changeCoin = str(changeCoin)
    print("Your change is:\n",changeCoin," x R5", sep = "")
elif change % 200 == 0:
    changeCoin = int(change/200)
    changeCoin = str(changeCoin)
    print("Your change is:\n",changeCoin," x R2", sep = "")
elif change % 100 == 0:
    changeCoin = int(change/100)
    changeCoin = str(changeCoin)
    print("Your change is:\n",changeCoin," x R1", sep = "")  

else:
    change = str(change)
    centChange = change[len(change)-2:len(change)+1]
    
    randChange = int(change) - int(centChange)
    
    
    centChange = int(centChange)
    randChange = int(randChange)
    if randChange % 500 == 0:
        if centChange % 50 == 0:
            print("Your change is:\n",int(randChange / 500)," x R5\n",int(centChange/50)," x 50c", sep = "")  
        elif centChange % 20 == 0:
            print("Your change is:\n",int(randChange / 500)," x R5\n",int(centChange/20)," x 20c", sep = "") 
        elif centChange % 10 == 0:
            print("Your change is:\n",int(randChange / 500)," x R5\n",int(centChange/10)," x 10c", sep = "")
        elif centChange % 5 == 0:
            print("Your change is:\n",int(randChange / 500)," x R5\n",int(centChange/5)," x 5c", sep = "") 
    elif randChange % 200 == 0:
        if centChange % 50 == 0:
            print("Your change is:\n",int(randChange / 200)," x R2\n",int(centChange/50)," x 50c", sep = "")  
        elif centChange % 20 == 0:
            print("Your change is:\n",int(randChange / 200)," x R2\n",int(centChange/20)," x 20c", sep = "") 
        elif centChange % 10 == 0:
            print("Your change is:\n",int(randChange / 200)," x R2\n",int(centChange/10)," x 10c", sep = "")
        elif centChange % 5 == 0:
            print("Your change is:\n",int(randChange / 200)," x R2\n",int(centChange/5)," x 5c", sep = "")         
    elif randChange % 100 == 0:
        if centChange % 50 == 0:
            print("Your change is:\n",int(randChange / 100)," x R1\n",int(centChange/50)," x 50c", sep = "")  
        elif centChange % 20 == 0:
            print("Your change is:\n",int(randChange / 100)," x R1\n",int(centChange/20)," x 20c", sep = "") 
        elif centChange % 10 == 0:
            print("Your change is:\n",int(randChange / 100)," x R1\n",int(centChange/10)," x 10c", sep = "")
        elif centChange % 5 == 0:
            print("Your change is:\n",int(randChange / 100)," x R1\n",int(centChange/5)," x 5c", sep = "")      
                
    
    
    
    
    

    

