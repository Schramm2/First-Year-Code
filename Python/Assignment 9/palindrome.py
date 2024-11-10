# Program to calculate whether or not a string is a palindrome.
# Matthew Schramm
# 28 april 2022
def palindrome(string): #Function to determine whether a number is a palindrome or not
    if string == "":
        return True
    elif len(string) == 1:
        return True
    else:
        if string[0:1] == string[len(string)-1:len(string) ]:
            return palindrome(string[1:len(string)-1])
        else:
            return False


string = input("Enter a string: \n")
if palindrome(string) == True:
    print("Palindrome!")
else:
    print("Not a palindrome!")