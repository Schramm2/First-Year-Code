def fibonacci_sequence(n):
    if n == 0:
        print("return 0")
        return 0
    elif n == 1:
        print("return 1")
        return 1
    
    else:
        print("Calculate: (",n-1,")+F(",n-2,")", sep = "")
        return fibonacci_sequence(n-1)+fibonacci_sequence(n-2)