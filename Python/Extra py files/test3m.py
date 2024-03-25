# A program to recusively count the number of times a given key
# appears in an array of strings.
# matthew Schramm
# SCHMAT041
# May 2022

def recursiveCount(lst, key):
    if len(lst) == 0:
        return 0
    else:
        count = 0
        if lst[0] == key:
            count = 1
            return count + recursiveCount(lst[1:], key)
        else:
            return recursiveCount(lst[1:], key)


def main():
    arraySearch = input("Enter an array of strings separated by space: \n")
    arrayOfStrings = arraySearch.split(" ")
    search_key = input("Enter a string to find:\n")
    result = recursiveCount(arrayOfStrings, search_key)
    
    print('The string', search_key, 'occurs', result, 'times', end='.')


if __name__ == '__main__':
    main()

