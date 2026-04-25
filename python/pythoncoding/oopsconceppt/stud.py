from oopsconceppt.college import college


class student(college):
    def __init__(self, rlno, sname, m1, m2, m3, ccode, cnsme, ccity):
        super().__init__(ccode, cnsme, ccity)
        self.srollno=rlno
        self.stname = sname
        self.mark1 = m1
        self.mark2 = m2
        self.mark3 = m3

    def calclate_total(self):
        return self.mark1 + self.mark2 + self.mark3

    def calculate_average(self):
        return self.calclate_total() / 3

