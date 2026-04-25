from oopsconceppt.college import college
class Teacher(college):
    def __init__(self, ccode, cnsme, ccity , ti ,tn, tbp):
        super().__init__(ccode, cnsme, ccity)
        self.teid=ti
        self.tname=tn
        self.Basicpay=tbp

    def calculate_salary(self):
        return self.Basicpay * 1.20 - self.Basicpay * 0.08

