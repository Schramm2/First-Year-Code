#Creation of a calendar according to the month and year input by the user
#2022/03/23
#Matthew Schramm
import math


def day_of_week(day, month, year):
    d = day
    m = month
    y = year
    if month == "1" or month == "2":
        m += 12
        y -= 1
        h = (d + ( (13*(m+1) ) /5 ) + y +(y/4)- (y/100)+(y/400))% 7
        h = ((h +5)%7) +1
        for i in range(1, month+1):
            days += num_days_in(i, year)
        days = days - (num_days_in(month, year) - day)
        h = round(h)
        return h
        
    else:
        h = (d + ( (13*(m+1) ) /5 ) + y +(y/4)- (y/100)+(y/400))% 7
        h = ((h +5)%7) +1
        h = round(h)
        return h
              


def is_leap(year):
    if str(year)[2:4] ==  "00":
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        if year % 4 == 0:
            return True
        else:
            return False        
    
    
    
    


def month_num(month_name):
    month_name = month_name.title()
    monthNumber = 0
    if month_name == "January":
        monthNumber = 1
        return monthNumber
    elif month_name == "February":
        monthNumber = 2
        return monthNumber
    elif month_name == "March":
        monthNumber = 3
        return monthNumber
    elif month_name == "April":
        monthNumber = 4
        return monthNumber
    elif month_name == "May":
        monthNumber = 5
        return monthNumber    
    elif month_name == "June":
        monthNumber = 6
        return monthNumber
    elif month_name == "July":
        monthNumber = 7
        return monthNumber
    elif month_name == "August":
        monthNumber = 8
        return monthNumber
    elif month_name == "September":
        monthNumber = 9
        return monthNumber
    elif month_name == "October":
        monthNumber = 10
        return monthNumber
    elif month_name == "November":
        monthNumber = 11
        return monthNumber
    elif month_name == "December":
        monthNumber = 12
        return monthNumber

def num_days_in(month_num, year):
    numberDays = 0
    if month_num == 1 or month_num == 3 or month_num == 5 or month_num == 7 or month_num == 8 or month_num == 10 or month_num == 12:
        numberDays = 31
        return numberDays
    elif month_num == 4 or month_num == 6 or  month_num == 9 or  month_num == 11:
        numberDays = 30
        return numberDays
    elif month_num == 2 and is_leap(year) == True:
        numberDays = 29
        return numberDays
    else:
        numberDays = 28
        return numberDays
    
        


def num_weeks(month_num, year):
    days = num_days_in(month_num, year)
    firstDay = day_of_week(1 , month_num,year)
    
    weeks = days // 7
    if weeks % 7 == 0:
        weeks+= 1
    
            
    return weeks
    
        
        
    


def week(week_num, start_day, days_in_month):
    
    
    if week_num == 1:
        counter = 7 - start_day
        for i in range(1 , counter+1):
            daysNumbers += i + " "
        return daysNumbers
    elif week_num == 2:
        counter = 7 - start_day
              
        for j in range(counter+1, counter + 8 ):
            daysNumbers += i + " "
        return daysNumbers
    elif week_num == 3:
        counter = 7 - start_day
        counter += 7
        for j in range(counter + 1, counter + 8 ):
            daysNumbers += i + " "
        return daysNumbers
    elif week_num == 4:
        counter = 7 - start_day
        counter += 14
        for j in range(counter + 1, counter + 8 ):
            daysNumbers += i + " "
        return daysNumbers
    elif week_num == 5:
        daysLeft = days_in_month % 7
        counter = 7 - start_day
        counter += 21
        
        for j in range(counter + 1, counter + daysLeft ):
            daysNumbers += i + " "
        return daysNumbers
        
            
        
        


def main():
    month = input("What is the month you want printed out?")
    year = input("What is the year of the month you want printed out?")
    numberOfWeeks = num_weeks(month, year)
    
    
    

if __name__=='__main__':
    main()






