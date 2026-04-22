# natural number print
'''num=int(input("ENter a number"))
val=1
while(val <= num):
    print(val);
    val+=1
'''
#armstrong number
num=input('Enter number')
val=len(num)
ni=int(num)
sum=0
while(ni>0):
    rem=ni%10
    sum+=rem ** val
    ni//=10
if(sum==int(num)):
    print('number is armstrong')
else:
    print('number is not armstrong')