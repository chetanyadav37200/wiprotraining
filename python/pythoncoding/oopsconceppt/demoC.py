from oopsconceppt.demoB import B
from oopsconceppt.demoA import A
class C(B,A):
    def __init__(self, n1, n2,msg):
        A.__init__(self,n1, n2)
        B.__init__(self, msg)

    def final(self):
        print("Done")