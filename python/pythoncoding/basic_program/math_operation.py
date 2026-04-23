from mypack.circle import areaofcircle,parimeter
from mypack.basicShape import areaofSquare

si=int(input("Enter side"))
radius=int(input("Enter radius"))
print('area of circle ',areaofcircle(radius))
print('parimeter of circle ',parimeter(radius))
print('area of square ',areaofSquare(si))