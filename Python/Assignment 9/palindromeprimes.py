# Program that finds all palindromic primes between two integers supplied as input
# Matthew Schramm
# 28 april 2022
import sys
sys.setrecursionlimit (30000)

def palindrome(number):#Program to determine if a number is a palindrome or not
    string = str(number)
    if string == "":
        return True
    elif len(string) == 1:
        return True
    else:
        if string[0:1] == string[len(string)-1:len(string) ]:
            return palindrome(string[1:len(string)-1])
        else:
            return False
def prime(number, counter = 2):#Function to detemine if the number is a prime number or not
    if number % counter == 0 :
        return False
    elif counter == number -1 :
        return True
    else:
        return prime(number, counter +1)
    
    
        
        

def palindromePrimes(start, end ):#Function to print out all palindromic primes between two integers
    if start == end+1:
        return -1
    else:
        if palindrome(start) == True and prime(start) == True:
            print(start)
            return palindromePrimes(start+1, end)
        return palindromePrimes(start+1, end)


startingNumber = eval(input("Enter the starting point N: \n"))
endingNumber = eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")
palindromePrimes(startingNumber, endingNumber)

    