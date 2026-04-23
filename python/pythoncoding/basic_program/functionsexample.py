'''#functions
def add(a,b):
    return a+b

def sub(a,b):
    return a-b


def mul(a,b):
    return a*b

#driver
n1=int(input("enter first number"))
n2=int(input("enter second number"))
print("sum :",add(n1,n2))
print("sub :",sub(n1,n2))
print("mul :",mul(n1,n2))
'''

#arbitary
'''
def add(numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum

numbers = list()
count =int(input("how many  : "))
for i in range(count):
    numbers.append(int(input('number')))
print(numbers)
print(add(numbers))'''
'''
def add(n1,n2,n3=10):
    sum=n1+n3+n2
    return sum

#main
n1=int(input("enter first number"))
n2=int(input("enter second number"))
print("sum :",add(n1,n2))
'''

#lambda
'''

n1=int(input("enter first number"))
n2=int(input("enter second number"))
add=lambda n1 , n2 : n1+n2
print(add(n1,n2))'''

numbers=[1,2,3,4,5]
square=lambda nums : [num * num for num in nums]
print(square(numbers))