from oopsconceppt.agecal import AgeCalculation
from oopsconceppt.myegeexceptio import AgeExeption

age=int(input("Enter age"))
aobj=AgeCalculation()

try:
    aobj.voting_age_check(age)

except AgeExeption as ae:
    print(ae)
else:
    print('Eligible to vote')


try:
    aobj.pansion_age_check(age)

except AgeExeption as ae:
    print(ae)
else:
    print('Eligible to get panssion')