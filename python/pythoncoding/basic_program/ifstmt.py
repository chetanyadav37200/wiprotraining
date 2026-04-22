#biggest of two number
'''
num1=int(input("Enter first number"))
num2=int(input("Enter Second number"))
if num1 > num2:
    print(num1,"is greater than",num2)
elif num2 > num1:
    print(num2,"is greater than",num1)
else:
    print(num2," is equal to ",num1)
'''
#big 3
'''
num1=int(input("Enter first number"))
num2=int(input("Enter Second number"))
num3=int(input("enter third number"))

if num1 == num2 and num2 == num3:
    print("all value are equal")
elif num1 > num2 and num1 > num3:
    print(num1," is the greatest")
elif num2 > num1 and num2 > num3:
    print(num2," is the greatest")
else:
    print(num3," is the greatest")

'''

#weak day
'''ch=int(input("Enter number between 1-7"))
match(ch):
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Choice")'''
