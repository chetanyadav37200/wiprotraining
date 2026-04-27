from oopsconceppt.calc import Calc
calcobj=Calc()
print(calcobj.add(10,5))
print(calcobj.sub(10,5))
print(calcobj.mul(10,5))

try:
    res=calcobj.fdiv(10,0)
except ZeroDivisionError:
    print('0 in Denominator')
except:
    print('oops')
else:
    print(res)
finally:
    print('done')