
def calculateBMI(h, w):
    """Calculate BMI"""
    bmi = w**2/ h
    
    return bmi 
def classifyBMI(bmiC):
    
    





def main():
    """Main User Interface to Calculate and output the BMI of user"""
    choice = "y"
    while choice != "n":
        height = eval(input("What is your height(in cm e.g. 165)? "))
        weight = eval(input("What is your weight(in kg e.g. 72.5)? "))
        bmi = calculateBMI(height, weight)
        
        print("Your BMI is:", bmi)
        choice = input("Do you want to calculate again(Y/N)? ").lower()

main()
        