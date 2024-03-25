#Print the month out that the user inputted in a calender format
#Matthew Schramm SCHMAT041
#2022/03/16


month = input("Enter the month ('January', ..., 'December'):\n")
sDay = input("Enter the start day ('Monday', ..., 'Sunday'):\n")

print(month,"\nMo Tu We Th Fr Sa Su")
dayTrack = 0
counter = 0
if  sDay == "Monday": #Calculating the starting position of the first of the month
        if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
                dayTrack = 31
                for i in range (1, dayTrack + 1):
                        if  i < 10 and i > 0:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        else:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")                  
        elif month == "April" or month == "June" or  month == "September" or  month == "November":
                dayTrack = 30
                for i in range (1, dayTrack + 1):
                        if  i < 10 and i > 0:
                                print(" ",i," ", sep = "", end = "")
                                ounter += 1
                                if counter % 7 == 0:
                                        print("")
                        else:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")                       
        else:
                dayTrack = 28
                for i in range (1, dayTrack + 1):
                        if  i < 10 and i > 0:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        else:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")                   



elif sDay == "Tuesday": #Calculating the starting position of the first of the month
        if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
                dayTrack = 31
                
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("    ",i," ",end = "", sep = "")
                                counter += 2
                                if counter % 7 == 0:
                                        print("")                   
        
        
        
        
        
        
        
        elif month == "April" or month == "June" or  month == "September" or  month == "November":
                dayTrack = 30
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("    ",i," ",end = "", sep = "")
                                counter += 2
                                if counter % 7 == 0:
                                        print("")                          
        else:
                dayTrack = 28
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("    ",i," ",end = "", sep = "")
                                counter += 2
                                if counter % 7 == 0:
                                        print("")                                       
elif sDay == "Wednesday": #Calculating the starting position of the first of the month
        if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
                dayTrack = 31
                
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("       ",i," ",end = "", sep = "")
                                counter += 3
                                if counter % 7 == 0:
                                        print("")                   
        
        
        
        
        
        
        
        elif month == "April" or month == "June" or  month == "September" or  month == "November":
                dayTrack = 30
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("       ",i," ",end = "", sep = "")
                                counter += 3
                                if counter % 7 == 0:
                                        print("")                          
        else:
                dayTrack = 28
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("       ",i," ",end = "", sep = "")
                                counter += 3
                                if counter % 7 == 0:
                                        print("")
elif sDay == "Thursday": #Calculating the starting position of the first of the month
        if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
                dayTrack = 31
                
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("          ",i," ",end = "", sep = "")
                                counter += 4
                                if counter % 7 == 0:
                                        print("")                   
        
        
        
        
        
        
        
        elif month == "April" or month == "June" or  month == "September" or  month == "November":
                dayTrack = 30
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("          ",i," ",end = "", sep = "")
                                counter += 4
                                if counter % 7 == 0:
                                        print("")                          
        else:
                dayTrack = 28
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("          ",i," ",end = "", sep = "")
                                counter += 4
                                if counter % 7 == 0:
                                        print("")
elif sDay == "Friday": #Calculating the starting position of the first of the month
        if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
                dayTrack = 31
                
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("             ",i," ",end = "", sep = "")
                                counter += 5
                                if counter % 7 == 0:
                                        print("")                   
        
        
        
        
        
        
        
        elif month == "April" or month == "June" or  month == "September" or  month == "November":
                dayTrack = 30
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("             ",i," ",end = "", sep = "")
                                counter += 5
                                if counter % 7 == 0:
                                        print("")                          
        else:
                dayTrack = 28
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("             ",i," ",end = "", sep = "")
                                counter += 5
                                if counter % 7 == 0:
                                        print("")
elif sDay == "Saturday": #Calculating the starting position of the first of the month
        if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
                dayTrack = 31
                
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("                ",i," ",end = "", sep = "")
                                counter += 6
                                if counter % 7 == 0:
                                        print("")                   
        
        
        
        
        
        
        
        elif month == "April" or month == "June" or  month == "September" or  month == "November":
                dayTrack = 30
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("                ",i," ",end = "", sep = "")
                                counter += 6
                                if counter % 7 == 0:
                                        print("")                          
        else:
                dayTrack = 28
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("                ",i," ",end = "", sep = "")
                                counter += 6
                                if counter % 7 == 0:
                                        print("")
elif sDay == "Sunday": #Calculating the starting position of the first of the month
        if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
                dayTrack = 31
                
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("                   ",i," ",end = "", sep = "")
                                counter += 7
                                if counter % 7 == 0:
                                        print("")                   
        
        
        
        
        
        
        
        elif month == "April" or month == "June" or  month == "September" or  month == "November":
                dayTrack = 30
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("                   ",i," ",end = "", sep = "")
                                counter += 7
                                if counter % 7 == 0:
                                        print("")                          
        else:
                dayTrack = 28
                for i in range (1,dayTrack +1):
                        if  i < 10 and i > 1:
                                print(" ",i," ", sep = "", end = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")
                        elif i >= 10:
                                print (i," ",end = "", sep = "")
                                counter += 1
                                if counter % 7 == 0:
                                        print("")             
                        else:
                                print ("                   ",i," ",end = "", sep = "")
                                counter += 7
                                if counter % 7 == 0:
                                        print("")

        
                              
            
