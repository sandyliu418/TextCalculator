
# rules: +, -, /, *, **
# q1: what would you like to do? yes, detect + - / * **, not one "Try again"
# q2: input the number
# q3: input the second number
# q4: do you have more number? y/n
# q4: how many more numbers do you have?

#mint.com

#q1 = input("What would you like to do? ") 

#if q1 == "+":
    #q1 = +
#elif q1 == "-":
    #q1 = -
#elif q1 == "/":
    #q1 = /
#elif q1 == "*":
    #q1 == *
#elif q1 == "**":
    #q1 == **
#else:

    #print("Try again")
    #q1 = input("What would you like to do? ")
    
def prompt():
    q1 = input("What would you like to do? Please select one of the following: +, -, /, *, **\n") 

    if q1 == "+":
        validFirstNumber = False
        while validFirstNumber == False:
            firstNumber = input("What is the first number you would you like to add? \n") #5
            validFirstNumber = detect_if_num(firstNumber) # set result to whether it was a num
        validSecondNumber = False
        while validSecondNumber == False:
            secondNumber = input("What is the second number you would you like to add? \n") #5
            validSecondNumber = detect_if_num(secondNumber)
        if firstNumber and secondNumber: #what does this line of code mean?
            ans = int(firstNumber) + int(secondNumber)
            print("The current total is " + str(ans))
        
        #NEW
        # another question; do you want to add another number. if yes, it will say what is third number
        # person inputs number, do you want to add another numberif yes, it will say what is fourth number
        else:
            prompt()
        moreNumbersYes = True
        x = 2
        while moreNumbersYes:
            validResponse = False
            while validResponse == False: 
                moreQuestion = input("Do you want to add another number? Y/N\n")
                validResponse = detect_if_YN(moreQuestion)
            if moreQuestion == "Y" or moreQuestion == "y":
                yesQuestion = True
                #num = input("Insert the number you would like to add here:\n")
                while yesQuestion:
                    x += 1
                    newNum = int(input("Insert the " + str(x) + " you would like to add here: \n"))
                    ans = ans + newNum
                    print(ans)
                    yesQuestion = False
            else:
                print("Byebye")
                moreNumbersYes = False
        #NEW

    elif q1 == "-":
        validInput = True
        while validInput:
            q2 = input("What is the first number you would you like to subtract? ")
            q2_is_num = detect_if_num(q2) # set result to whether it was a num
            #print("q2" + str(q2_is_num))
            if q2_is_num == True:
                validInput = False
        q3 = input("What is the second number you would you like to subtract? ")
        q3_is_num = detect_if_num(q3)
        if q2_is_num and q3_is_num:
            ans = int(q2) - int(q3)
            print(ans)
        else:
            prompt()
    elif q1 == "/":
        validInput = True
        while validInput:
            q2 = input("What is the first number you would you like to divide? ")
            q2_is_num = detect_if_num(q2) # set result to whether it was a num
            #print("q2" + str(q2_is_num))
            if q2_is_num == True:
                validInput = False
        q3 = input("What is the second number you would you like to divide? ")
        q3_is
        _num = detect_if_num(q3)
        if q2_is_num and q3_is_num:
            ans = int(q2) / int(q3)
            print(ans)
        else:
            prompt()
    elif q1 == "*":
        validInput = True
        while validInput:
            q2 = input("What is the first number you would you like to multiply? ")
            q2_is_num = detect_if_num(q2) # set result to whether it was a num
            #print("q2" + str(q2_is_num))
            if q2_is_num == True:
                validInput = False
        q3 = input("What is the second number you would you like to multiply? ")
        q3_is_num = detect_if_num(q3)
        if q2_is_num and q3_is_num:
            ans = int(q2) * int(q3)
            print(ans)
        else:
            prompt()
    elif q1 == "**":
        validInput = True
        while validInput:
            q2 = input("What is the first number you would you like to exponent? ")
            q2_is_num = detect_if_num(q2) # set result to whether it was a num
            #print("q2" + str(q2_is_num))
            if q2_is_num == True:
                validInput = False
        q3 = input("What is the second number you would you like to exponent? ")
        q3_is_num = detect_if_num(q3)
        if q2_is_num and q3_is_num:
            ans = int(q2) ** int(q3)
            print(ans)
        else:
            prompt()
    else:
        star = True
        while star:
            print("Try again")
            #q1 = input("What would you like to do? ") #it exits after two tries
            if q1 == "+" or "-" or "/" or "*" or "**":
                star = False
                prompt()
                
                
def detect_if_num(num):
    if num.isdigit():
        return True
    return False

def startNumber(num):
    # ask the question and store it in a variable
    #num = input("Please input the {} number you would like to add\n")
    global ans
    #print(ans)
    ans = ans + int(num)
    #print("Ok, the total is %s" %(ans))
    #print("Ok, the total is" + ans)

def detect_if_YN(x):
    if x == "Y" or x == "y" or x == "N" or x == "n":
        return True
    else:
        return False
    
prompt()
    
# part 1: MVP (bare minimum of features), later after completed, what else can it do?
# idenitfy the limitations of this program
# write where I want it to go

#part 2:
# write all test cases

# if anything else, then try again
# it does what it's supposed to do
# if first/second number is not a number
    
