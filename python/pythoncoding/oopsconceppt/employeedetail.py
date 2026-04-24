class EmployeeDetails:
    def __init__(self,empno,ename,basicpay):
        self.emNo = empno
        self.emName = ename
        self.basic_pay = basicpay
        self.da = 20.0
        self.hra = 10.0
        self.pf = 5.5

    def calculate_allowance(self):
        allowance = (self.basic_pay * self.da / 100) + (self.basic_pay * self.hra/100)
        return allowance

    def calculagte_deduction(self):
        deduction=self.basic_pay * self.pf / 100
        return deduction

    def Net_salary(self):
        salary=self.basic_pay + self.calculate_allowance() - self.calculagte_deduction()
        return salary



