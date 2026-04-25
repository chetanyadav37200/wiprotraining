from rectangle import rectangle
from square import square

sqobj=square(10)
print(f"Area {sqobj.calculate_area()}\nparameter :{sqobj.calculate_parameter()}")

reobj=rectangle(10,20)
print(f"Area {reobj.calculate_area()}\nparameter :{reobj.calculate_parameter()}")
