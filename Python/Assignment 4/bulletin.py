#Simulation of a simple BBS with one stored message and 2 fixed files
#Matthew Schramm SCHMAT041
#2022/03/16

print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
selection = input("Enter your selection:\n")
if  selection == 'e':
    message = input("Enter the message:\n")
    
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
    selection = input("Enter your selection:\n")
    if selection == 'v':
        print("The message is:",message)
        
        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
        selection = input("Enter your selection:\n")   
        if selection == 'x':
            print("Goodbye!")
elif selection == 'v':
    print("The message is: no message yet")
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
    selection = input("Enter your selection:\n")
    if  selection == 'e':
        message = input("Enter the message:\n")
        
        print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
        selection = input("Enter your selection:\n")
        if selection == 'v':
            print("The message is:",message)
            
            print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
            selection = input("Enter your selection:\n")   
            if selection == 'x':
                print("Goodbye!")    
elif selection == 'l':
    print("List of files: 42.txt, 1015.txt")
    
    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
    selection = input("Enter your selection:\n")
    
    if selection == 'd':
        file = input("Enter the filename: \n")
        if file == "42.txt":
            print("The meaning of life is blah blah blah ...")
            print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
            selection = input("Enter your selection:\n")
            if selection == 'x':
                print("Goodbye!")
        elif file == "1015.txt":
            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
            print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
            selection = input("Enter your selection:\n")
            if selection == 'x':
                print("Goodbye!")            
        else:
            print("File not found")
            print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
            selection = input("Enter your selection:\n")
            if selection == 'd':
                file = input("Enter the filename: \n")
                if file == "42.txt":
                    print("The meaning of life is blah blah blah ...")
                    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
                    selection = input("Enter your selection:\n")
                    if selection == 'x':
                        print("Goodbye!")
                elif file == "1015.txt":
                    print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                    print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
                    selection = input("Enter your selection:\n")
                    if selection == 'd':
                        file = input("Enter the filename: \n")
                        if file == "42.txt":
                            print("The meaning of life is blah blah blah ...")
                            print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
                            selection = input("Enter your selection:\n")
                            if selection == 'x':
                                print("Goodbye!")
                        elif file == "1015.txt":
                            print("Computer Science class notes ... simplified\nDo all work\nPass course\nBe happy")
                            print("Welcome to UCT BBS\nMENU\n(E)nter a message\n(V)iew message\n(L)ist files\n(D)isplay file\ne(X)it")  
                            selection = input("Enter your selection:\n")
                            if selection == 'x':
                                print("Goodbye!")                       

elif selection == 'x':
    print("Goodbye!") 
    
    
        
    