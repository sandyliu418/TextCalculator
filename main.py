
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
    q1 = input("What would you like to do? Please select one of the following: +, -, /, *, **") 

    if q1 == "+":
        green = True
        while green:
            q2 = input("What is the first number you would you like to add? ") #5
            q2_is_num = detect_if_num(q2) # set result to whether it was a num
            #print("q2" + str(q2_is_num))
            if q2_is_num == True:
                green = False
        q3 = input("What is the second number you would you like to add? ")
        q3_is_num = detect_if_num(q3)
        if q2_is_num and q3_is_num:
            ans = int(q2) + int(q3)
            print(ans)
        else:
            prompt()
    elif q1 == "-":
        green = True
        while green:
            q2 = input("What is the first number you would you like to subtract? ")
            q2_is_num = detect_if_num(q2) # set result to whether it was a num
            #print("q2" + str(q2_is_num))
            if q2_is_num == True:
                green = False
        q3 = input("What is the second number you would you like to subtract? ")
        q3_is_num = detect_if_num(q3)
        if q2_is_num and q3_is_num:
            ans = int(q2) - int(q3)
            print(ans)
        else:
            prompt()
    elif q1 == "/":
        green = True
        while green:
            q2 = input("What is the first number you would you like to divide? ")
            q2_is_num = detect_if_num(q2) # set result to whether it was a num
            #print("q2" + str(q2_is_num))
            if q2_is_num == True:
                green = False
        q3 = input("What is the second number you would you like to divide? ")
        q3_is_num = detect_if_num(q3)
        if q2_is_num and q3_is_num:
            ans = int(q2) / int(q3)
            print(ans)
        else:
            prompt()
    elif q1 == "*":
        green = True
        while green:
            q2 = input("What is the first number you would you like to multiply? ")
            q2_is_num = detect_if_num(q2) # set result to whether it was a num
            #print("q2" + str(q2_is_num))
            if q2_is_num == True:
                green = False
        q3 = input("What is the second number you would you like to multiply? ")
        q3_is_num = detect_if_num(q3)
        if q2_is_num and q3_is_num:
            ans = int(q2) * int(q3)
            print(ans)
        else:
            prompt()
    elif q1 == "**":
        green = True
        while green:
            q2 = input("What is the first number you would you like to exponent? ")
            q2_is_num = detect_if_num(q2) # set result to whether it was a num
            #print("q2" + str(q2_is_num))
            if q2_is_num == True:
                green = False
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
    
prompt()
    
# part 1: MVP (bare minimum of features), later after completed, what else can it do?
# idenitfy the limitations of this program
# write where I want it to go

#part 2:
# write all test cases

# if anything else, then try again
# it does what it's supposed to do
# if first/second number is not a number
    
