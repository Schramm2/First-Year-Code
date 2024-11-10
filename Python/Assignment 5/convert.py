#Converting a standard 24 hour time and date to a long 12 hour format
#2022/03/23
#Matthew Schramm

shortFormat = input("Enter the date and time (yyyy-mm-dd hh:mm):\n")

date = shortFormat[0:10]
time = shortFormat[11:len(shortFormat)]

hour = time[0:2]
hour = int(hour)
longFormat = ""

year = date[2:4]
month = date[5:7]
month = int(month)
day = date[8:10]
day = int(day)



if  hour < 12 and hour >0:
    if hour <10:
        day = int(day)
        if day == 1 or day == 21:
            day = str(day)
            longFormat += time[1:5] + " am on the " + day + "st of "
            if month == 1:
                monthName = "January"
                longFormat += monthName + " \'"+year
            elif month == 2:
                monthName = "February"
                longFormat += monthName + " \'"+year  
            elif month == 3:
                monthName = "March"
                longFormat += monthName + " \'"+year
            elif month == 4:
                monthName = "April"
                longFormat += monthName + " \'"+year  
            elif month == 5:
                monthName = "May"
                longFormat += monthName + " \'"+year  
            elif month == 6:
                monthName = "June"
                longFormat += monthName + " \'"+year 
            elif month == 7:
                monthName = "July"
                longFormat += monthName + " \'"+year   
            elif month == 8:
                monthName = "August"
                longFormat += monthName + " \'"+year  
            elif month == 9:
                monthName = "September"
                longFormat += monthName + " \'"+year  
            elif month == 10:
                monthName = "October"
                longFormat += monthName + " \'"+year
            elif month == 11:
                monthName = "November"
                longFormat += monthName + " \'"+year  
            elif month == 12:
                monthName = "December"
                longFormat += monthName + " \'"+year 
        elif day == 2 or day == 22:
            day = str(day)
            longFormat += time[1:5] + " am on the " + day + "nd of "
            if month == 1:
                monthName = "January"
                longFormat += monthName + " \'"+year
            elif month == 2:
                monthName = "February"
                longFormat += monthName + " \'"+year  
            elif month == 3:
                monthName = "March"
                longFormat += monthName + " \'"+year
            elif month == 4:
                monthName = "April"
                longFormat += monthName + " \'"+year  
            elif month == 5:
                monthName = "May"
                longFormat += monthName + " \'"+year  
            elif month == 6:
                monthName = "June"
                longFormat += monthName + " \'"+year 
            elif month == 7:
                monthName = "July"
                longFormat += monthName + " \'"+year   
            elif month == 8:
                monthName = "August"
                longFormat += monthName + " \'"+year  
            elif month == 9:
                monthName = "September"
                longFormat += monthName + " \'"+year  
            elif month == 10:
                monthName = "October"
                longFormat += monthName + " \'"+year
            elif month == 11:
                monthName = "November"
                longFormat += monthName + " \'"+year  
            elif month == 12:
                monthName = "December"
                longFormat += monthName + " \'"+year   
        elif day == 3 or day == 23:
            day = str(day)
            longFormat += time[1:5] + " am on the " + day + "rd of "
            if month == 1:
                monthName = "January"
                longFormat += monthName + " \'"+year
            elif month == 2:
                monthName = "February"
                longFormat += monthName + " \'"+year  
            elif month == 3:
                monthName = "March"
                longFormat += monthName + " \'"+year
            elif month == 4:
                monthName = "April"
                longFormat += monthName + " \'"+year  
            elif month == 5:
                monthName = "May"
                longFormat += monthName + " \'"+year  
            elif month == 6:
                monthName = "June"
                longFormat += monthName + " \'"+year 
            elif month == 7:
                monthName = "July"
                longFormat += monthName + " \'"+year   
            elif month == 8:
                monthName = "August"
                longFormat += monthName + " \'"+year  
            elif month == 9:
                monthName = "September"
                longFormat += monthName + " \'"+year  
            elif month == 10:
                monthName = "October"
                longFormat += monthName + " \'"+year
            elif month == 11:
                monthName = "November"
                longFormat += monthName + " \'"+year  
            elif month == 12:
                monthName = "December"
                longFormat += monthName + " \'"+year  
        else:
            day = str(day)
            longFormat += time[1:5] + " am on the " + day + "th of "
            if month == 1:
                monthName = "January"
                longFormat += monthName + " \'"+year
            elif month == 2:
                monthName = "February"
                longFormat += monthName + " \'"+year  
            elif month == 3:
                monthName = "March"
                longFormat += monthName + " \'"+year
            elif month == 4:
                monthName = "April"
                longFormat += monthName + " \'"+year  
            elif month == 5:
                monthName = "May"
                longFormat += monthName + " \'"+year  
            elif month == 6:
                monthName = "June"
                longFormat += monthName + " \'"+year 
            elif month == 7:
                monthName = "July"
                longFormat += monthName + " \'"+year   
            elif month == 8:
                monthName = "August"
                longFormat += monthName + " \'"+year  
            elif month == 9:
                monthName = "September"
                longFormat += monthName + " \'"+year  
            elif month == 10:
                monthName = "October"
                longFormat += monthName + " \'"+year
            elif month == 11:
                monthName = "November"
                longFormat += monthName + " \'"+year  
            elif month == 12:
                monthName = "December"
                longFormat += monthName + " \'"+year             
            
            
        
                   
        
    else:
        if day == 1 or day == 21:
            day = str(day)
            longFormat += time[0:5] + " am on the " + day + "st of "
            if month == 1:
                monthName = "January"
                longFormat += monthName + " \'"+year
            elif month == 2:
                monthName = "February"
                longFormat += monthName + " \'"+year  
            elif month == 3:
                monthName = "March"
                longFormat += monthName + " \'"+year
            elif month == 4:
                monthName = "April"
                longFormat += monthName + " \'"+year  
            elif month == 5:
                monthName = "May"
                longFormat += monthName + " \'"+year  
            elif month == 6:
                monthName = "June"
                longFormat += monthName + " \'"+year 
            elif month == 7:
                monthName = "July"
                longFormat += monthName + " \'"+year   
            elif month == 8:
                monthName = "August"
                longFormat += monthName + " \'"+year  
            elif month == 9:
                monthName = "September"
                longFormat += monthName + " \'"+year  
            elif month == 10:
                monthName = "October"
                longFormat += monthName + " \'"+year
            elif month == 11:
                monthName = "November"
                longFormat += monthName + " \'"+year  
            elif month == 12:
                monthName = "December"
                longFormat += monthName + " \'"+year 
        elif day == 2 or day == 22:
            day = str(day)
            longFormat += time[0:5] + " am on the " + day + "nd of "
            if month == 1:
                monthName = "January"
                longFormat += monthName + " \'"+year
            elif month == 2:
                monthName = "February"
                longFormat += monthName + " \'"+year  
            elif month == 3:
                monthName = "March"
                longFormat += monthName + " \'"+year
            elif month == 4:
                monthName = "April"
                longFormat += monthName + " \'"+year  
            elif month == 5:
                monthName = "May"
                longFormat += monthName + " \'"+year  
            elif month == 6:
                monthName = "June"
                longFormat += monthName + " \'"+year 
            elif month == 7:
                monthName = "July"
                longFormat += monthName + " \'"+year   
            elif month == 8:
                monthName = "August"
                longFormat += monthName + " \'"+year  
            elif month == 9:
                monthName = "September"
                longFormat += monthName + " \'"+year  
            elif month == 10:
                monthName = "October"
                longFormat += monthName + " \'"+year
            elif month == 11:
                monthName = "November"
                longFormat += monthName + " \'"+year  
            elif month == 12:
                monthName = "December"
                longFormat += monthName + " \'"+year   
        elif day == 3 or day == 23:
            day = str(day)
            longFormat += time[0:5] + " am on the " + day + "rd of "
            if month == 1:
                monthName = "January"
                longFormat += monthName + " \'"+year
            elif month == 2:
                monthName = "February"
                longFormat += monthName + " \'"+year  
            elif month == 3:
                monthName = "March"
                longFormat += monthName + " \'"+year
            elif month == 4:
                monthName = "April"
                longFormat += monthName + " \'"+year  
            elif month == 5:
                monthName = "May"
                longFormat += monthName + " \'"+year  
            elif month == 6:
                monthName = "June"
                longFormat += monthName + " \'"+year 
            elif month == 7:
                monthName = "July"
                longFormat += monthName + " \'"+year   
            elif month == 8:
                monthName = "August"
                longFormat += monthName + " \'"+year  
            elif month == 9:
                monthName = "September"
                longFormat += monthName + " \'"+year  
            elif month == 10:
                monthName = "October"
                longFormat += monthName + " \'"+year
            elif month == 11:
                monthName = "November"
                longFormat += monthName + " \'"+year  
            elif month == 12:
                monthName = "December"
                longFormat += monthName + " \'"+year
        else:
            day = str(day)
            longFormat += time[0:5] + " am on the " + day + "th of "
            if month == 1:
                monthName = "January"
                longFormat += monthName + " \'"+year
            elif month == 2:
                monthName = "February"
                longFormat += monthName + " \'"+year  
            elif month == 3:
                monthName = "March"
                longFormat += monthName + " \'"+year
            elif month == 4:
                monthName = "April"
                longFormat += monthName + " \'"+year  
            elif month == 5:
                monthName = "May"
                longFormat += monthName + " \'"+year  
            elif month == 6:
                monthName = "June"
                longFormat += monthName + " \'"+year 
            elif month == 7:
                monthName = "July"
                longFormat += monthName + " \'"+year   
            elif month == 8:
                monthName = "August"
                longFormat += monthName + " \'"+year  
            elif month == 9:
                monthName = "September"
                longFormat += monthName + " \'"+year  
            elif month == 10:
                monthName = "October"
                longFormat += monthName + " \'"+year
            elif month == 11:
                monthName = "November"
                longFormat += monthName + " \'"+year  
            elif month == 12:
                monthName = "December"
                longFormat += monthName + " \'"+year            
            
elif hour == 24 or hour == 0:
    day = int(day)
    hour = 12
    hour = str(hour)
    if day == 1 or day == 21:
        day = str(day)
        
        longFormat += hour+":"  + time[3:5] + " am on the " + day + "st of "
        if month == 1:
            monthName = "January"
            longFormat += monthName + " \'"+year
        elif month == 2:
            monthName = "February"
            longFormat += monthName + " \'"+year  
        elif month == 3:
            monthName = "March"
            longFormat += monthName + " \'"+year
        elif month == 4:
            monthName = "April"
            longFormat += monthName + " \'"+year  
        elif month == 5:
            monthName = "May"
            longFormat += monthName + " \'"+year  
        elif month == 6:
            monthName = "June"
            longFormat += monthName + " \'"+year 
        elif month == 7:
            monthName = "July"
            longFormat += monthName + " \'"+year   
        elif month == 8:
            monthName = "August"
            longFormat += monthName + " \'"+year  
        elif month == 9:
            monthName = "September"
            longFormat += monthName + " \'"+year  
        elif month == 10:
            monthName = "October"
            longFormat += monthName + " \'"+year
        elif month == 11:
            monthName = "November"
            longFormat += monthName + " \'"+year  
        elif month == 12:
            monthName = "December"
            longFormat += monthName + " \'"+year        
    elif day == 2 or day == 22:
        day = str(day)
              
        longFormat += hour+":"  + time[3:5] + " am on the " +day + "nd of "
        if month == 1:
            monthName = "January"
            longFormat += monthName + " \'"+year
        elif month == 2:
            monthName = "February"
            longFormat += monthName + " \'"+year  
        elif month == 3:
            monthName = "March"
            longFormat += monthName + " \'"+year
        elif month == 4:
            monthName = "April"
            longFormat += monthName + " \'"+year  
        elif month == 5:
            monthName = "May"
            longFormat += monthName + " \'"+year  
        elif month == 6:
            monthName = "June"
            longFormat += monthName + " \'"+year 
        elif month == 7:
            monthName = "July"
            longFormat += monthName + " \'"+year   
        elif month == 8:
            monthName = "August"
            longFormat += monthName + " \'"+year  
        elif month == 9:
            monthName = "September"
            longFormat += monthName + " \'"+year  
        elif month == 10:
            monthName = "October"
            longFormat += monthName + " \'"+year
        elif month == 11:
            monthName = "November"
            longFormat += monthName + " \'"+year  
        elif month == 12:
            monthName = "December"
            longFormat += monthName + " \'"+year      
    elif day == 3 or day == 23:
        day = str(day)  
       
        longFormat += hour+":"  + time[3:5] + " am on the " + day + "rd of "
        if month == 1:
            monthName = "January"
            longFormat += monthName + " \'"+year
        elif month == 2:
            monthName = "February"
            longFormat += monthName + " \'"+year  
        elif month == 3:
            monthName = "March"
            longFormat += monthName + " \'"+year
        elif month == 4:
            monthName = "April"
            longFormat += monthName + " \'"+year  
        elif month == 5:
            monthName = "May"
            longFormat += monthName + " \'"+year  
        elif month == 6:
            monthName = "June"
            longFormat += monthName + " \'"+year 
        elif month == 7:
            monthName = "July"
            longFormat += monthName + " \'"+year   
        elif month == 8:
            monthName = "August"
            longFormat += monthName + " \'"+year  
        elif month == 9:
            monthName = "September"
            longFormat += monthName + " \'"+year  
        elif month == 10:
            monthName = "October"
            longFormat += monthName + " \'"+year
        elif month == 11:
            monthName = "November"
            longFormat += monthName + " \'"+year  
        elif month == 12:
            monthName = "December"
            longFormat += monthName + " \'"+year   
    else:
        day = str(day)       
        longFormat += hour+":"  + time[3:5] + " am on the " + day + "th of "
        if month == 1:
            monthName = "January"
            longFormat += monthName + " \'"+year
        elif month == 2:
            monthName = "February"
            longFormat += monthName + " \'"+year  
        elif month == 3:
            monthName = "March"
            longFormat += monthName + " \'"+year
        elif month == 4:
            monthName = "April"
            longFormat += monthName + " \'"+year  
        elif month == 5:
            monthName = "May"
            longFormat += monthName + " \'"+year  
        elif month == 6:
            monthName = "June"
            longFormat += monthName + " \'"+year 
        elif month == 7:
            monthName = "July"
            longFormat += monthName + " \'"+year   
        elif month == 8:
            monthName = "August"
            longFormat += monthName + " \'"+year  
        elif month == 9:
            monthName = "September"
            longFormat += monthName + " \'"+year  
        elif month == 10:
            monthName = "October"
            longFormat += monthName + " \'"+year
        elif month == 11:
            monthName = "November"
            longFormat += monthName + " \'"+year  
        elif month == 12:
            monthName = "December"
            longFormat += monthName + " \'"+year  
            
elif hour == 12:
    day = int(day)
    
    hour = str(hour)
    if day == 1 or day == 21:
        day = str(day)
        longFormat += hour+":"  + time[3:5] + " pm on the " + day + "st of "
        if month == 1:
            monthName = "January"
            longFormat += monthName + " \'"+year
        elif month == 2:
            monthName = "February"
            longFormat += monthName + " \'"+year  
        elif month == 3:
            monthName = "March"
            longFormat += monthName + " \'"+year
        elif month == 4:
            monthName = "April"
            longFormat += monthName + " \'"+year  
        elif month == 5:
            monthName = "May"
            longFormat += monthName + " \'"+year  
        elif month == 6:
            monthName = "June"
            longFormat += monthName + " \'"+year 
        elif month == 7:
            monthName = "July"
            longFormat += monthName + " \'"+year   
        elif month == 8:
            monthName = "August"
            longFormat += monthName + " \'"+year  
        elif month == 9:
            monthName = "September"
            longFormat += monthName + " \'"+year  
        elif month == 10:
            monthName = "October"
            longFormat += monthName + " \'"+year
        elif month == 11:
            monthName = "November"
            longFormat += monthName + " \'"+year  
        elif month == 12:
            monthName = "December"
            longFormat += monthName + " \'"+year        
    elif day == 2 or day == 22:
        day = str(day)      
        longFormat += hour+":"  + time[3:5] + " pm on the " + day + "nd of "
        if month == 1:
            monthName = "January"
            longFormat += monthName + " \'"+year
        elif month == 2:
            monthName = "February"
            longFormat += monthName + " \'"+year  
        elif month == 3:
            monthName = "March"
            longFormat += monthName + " \'"+year
        elif month == 4:
            monthName = "April"
            longFormat += monthName + " \'"+year  
        elif month == 5:
            monthName = "May"
            longFormat += monthName + " \'"+year  
        elif month == 6:
            monthName = "June"
            longFormat += monthName + " \'"+year 
        elif month == 7:
            monthName = "July"
            longFormat += monthName + " \'"+year   
        elif month == 8:
            monthName = "August"
            longFormat += monthName + " \'"+year  
        elif month == 9:
            monthName = "September"
            longFormat += monthName + " \'"+year  
        elif month == 10:
            monthName = "October"
            longFormat += monthName + " \'"+year
        elif month == 11:
            monthName = "November"
            longFormat += monthName + " \'"+year  
        elif month == 12:
            monthName = "December"
            longFormat += monthName + " \'"+year      
    elif day == 3 or day == 23:
        day = str(day)      
        longFormat += hour+":"  + time[3:5] + " pm on the " + day + "rd of "
        if month == 1:
            monthName = "January"
            longFormat += monthName + " \'"+year
        elif month == 2:
            monthName = "February"
            longFormat += monthName + " \'"+year  
        elif month == 3:
            monthName = "March"
            longFormat += monthName + " \'"+year
        elif month == 4:
            monthName = "April"
            longFormat += monthName + " \'"+year  
        elif month == 5:
            monthName = "May"
            longFormat += monthName + " \'"+year  
        elif month == 6:
            monthName = "June"
            longFormat += monthName + " \'"+year 
        elif month == 7:
            monthName = "July"
            longFormat += monthName + " \'"+year   
        elif month == 8:
            monthName = "August"
            longFormat += monthName + " \'"+year  
        elif month == 9:
            monthName = "September"
            longFormat += monthName + " \'"+year  
        elif month == 10:
            monthName = "October"
            longFormat += monthName + " \'"+year
        elif month == 11:
            monthName = "November"
            longFormat += monthName + " \'"+year  
        elif month == 12:
            monthName = "December"
            longFormat += monthName + " \'"+year   
    else:
        day = str(day)        
        longFormat += hour +":" + time[3:5] + " pm on the " + day + "th of "
        if month == 1:
            monthName = "January"
            longFormat += monthName + " \'"+year
        elif month == 2:
            monthName = "February"
            longFormat += monthName + " \'"+year  
        elif month == 3:
            monthName = "March"
            longFormat += monthName + " \'"+year
        elif month == 4:
            monthName = "April"
            longFormat += monthName + " \'"+year  
        elif month == 5:
            monthName = "May"
            longFormat += monthName + " \'"+year  
        elif month == 6:
            monthName = "June"
            longFormat += monthName + " \'"+year 
        elif month == 7:
            monthName = "July"
            longFormat += monthName + " \'"+year   
        elif month == 8:
            monthName = "August"
            longFormat += monthName + " \'"+year  
        elif month == 9:
            monthName = "September"
            longFormat += monthName + " \'"+year  
        elif month == 10:
            monthName = "October"
            longFormat += monthName + " \'"+year
        elif month == 11:
            monthName = "November"
            longFormat += monthName + " \'"+year  
        elif month == 12:
            monthName = "December"
            longFormat += monthName + " \'"+year       
    
else:
    day = int(day)
    hour = hour -12
    hour = str(hour)
    if day == 1 or day == 21:
        day = str(day)
        longFormat += hour+":"  + time[3:5] + " pm on the " + day + "st of "
        if month == 1:
            monthName = "January"
            longFormat += monthName + " \'"+year
        elif month == 2:
            monthName = "February"
            longFormat += monthName + " \'"+year  
        elif month == 3:
            monthName = "March"
            longFormat += monthName + " \'"+year
        elif month == 4:
            monthName = "April"
            longFormat += monthName + " \'"+year  
        elif month == 5:
            monthName = "May"
            longFormat += monthName + " \'"+year  
        elif month == 6:
            monthName = "June"
            longFormat += monthName + " \'"+year 
        elif month == 7:
            monthName = "July"
            longFormat += monthName + " \'"+year   
        elif month == 8:
            monthName = "August"
            longFormat += monthName + " \'"+year  
        elif month == 9:
            monthName = "September"
            longFormat += monthName + " \'"+year  
        elif month == 10:
            monthName = "October"
            longFormat += monthName + " \'"+year
        elif month == 11:
            monthName = "November"
            longFormat += monthName + " \'"+year  
        elif month == 12:
            monthName = "December"
            longFormat += monthName + " \'"+year        
    elif day == 2 or day == 22:
        day = str(day)      
        longFormat += hour+":"  + time[3:5] + " pm on the " + day + "nd of "
        if month == 1:
            monthName = "January"
            longFormat += monthName + " \'"+year
        elif month == 2:
            monthName = "February"
            longFormat += monthName + " \'"+year  
        elif month == 3:
            monthName = "March"
            longFormat += monthName + " \'"+year
        elif month == 4:
            monthName = "April"
            longFormat += monthName + " \'"+year  
        elif month == 5:
            monthName = "May"
            longFormat += monthName + " \'"+year  
        elif month == 6:
            monthName = "June"
            longFormat += monthName + " \'"+year 
        elif month == 7:
            monthName = "July"
            longFormat += monthName + " \'"+year   
        elif month == 8:
            monthName = "August"
            longFormat += monthName + " \'"+year  
        elif month == 9:
            monthName = "September"
            longFormat += monthName + " \'"+year  
        elif month == 10:
            monthName = "October"
            longFormat += monthName + " \'"+year
        elif month == 11:
            monthName = "November"
            longFormat += monthName + " \'"+year  
        elif month == 12:
            monthName = "December"
            longFormat += monthName + " \'"+year      
    elif day == 3 or day == 23:
        day = str(day)      
        longFormat += hour+":"  + time[3:5] + " pm on the " + day + "rd of "
        if month == 1:
            monthName = "January"
            longFormat += monthName + " \'"+year
        elif month == 2:
            monthName = "February"
            longFormat += monthName + " \'"+year  
        elif month == 3:
            monthName = "March"
            longFormat += monthName + " \'"+year
        elif month == 4:
            monthName = "April"
            longFormat += monthName + " \'"+year  
        elif month == 5:
            monthName = "May"
            longFormat += monthName + " \'"+year  
        elif month == 6:
            monthName = "June"
            longFormat += monthName + " \'"+year 
        elif month == 7:
            monthName = "July"
            longFormat += monthName + " \'"+year   
        elif month == 8:
            monthName = "August"
            longFormat += monthName + " \'"+year  
        elif month == 9:
            monthName = "September"
            longFormat += monthName + " \'"+year  
        elif month == 10:
            monthName = "October"
            longFormat += monthName + " \'"+year
        elif month == 11:
            monthName = "November"
            longFormat += monthName + " \'"+year  
        elif month == 12:
            monthName = "December"
            longFormat += monthName + " \'"+year   
    else:
        day = str(day)        
        longFormat += hour +":" + time[3:5] + " pm on the " + day + "th of "
        if month == 1:
            monthName = "January"
            longFormat += monthName + " \'"+year
        elif month == 2:
            monthName = "February"
            longFormat += monthName + " \'"+year  
        elif month == 3:
            monthName = "March"
            longFormat += monthName + " \'"+year
        elif month == 4:
            monthName = "April"
            longFormat += monthName + " \'"+year  
        elif month == 5:
            monthName = "May"
            longFormat += monthName + " \'"+year  
        elif month == 6:
            monthName = "June"
            longFormat += monthName + " \'"+year 
        elif month == 7:
            monthName = "July"
            longFormat += monthName + " \'"+year   
        elif month == 8:
            monthName = "August"
            longFormat += monthName + " \'"+year  
        elif month == 9:
            monthName = "September"
            longFormat += monthName + " \'"+year  
        elif month == 10:
            monthName = "October"
            longFormat += monthName + " \'"+year
        elif month == 11:
            monthName = "November"
            longFormat += monthName + " \'"+year  
        elif month == 12:
            monthName = "December"
            longFormat += monthName + " \'"+year           
        
    
         

print(longFormat)
    
