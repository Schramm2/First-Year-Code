# CSC1015F Practical Test 3: Version B
# Matthew Schramm
# SCHMAT041
# May 2022

# A program that counts substrings with different first and last characters
 
import sys

sys.setrecursionlimit(10000)
 
# A Function that counts subtrings with different first and
# last characters
def countSubstrs(str, i, j, n): # 'i' is the first character. 'j' is the last
    
    
    # character. 'n' is the legnth of the string.
    
                
      
      
     
    
    
 
# driver method
def main():
    try:
        input_str = input("Enter a string:\n")
    
        input_str.lower()
        n = len(input_str)
    
        print("There are", countSubstrs(input_str, 0, n - 1, n), "substrings with different first and last character.")
    except EOFError:
        return
    
    
if __name__=='__main__':
    main()
