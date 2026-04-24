
from oopsconceppt.employeedetail import EmployeeDetails

#driver

eno = int(input('Emp no :'))
name=input('Enter emp name :')
bp=float(input('Enter basic pay'))
employee = EmployeeDetails(empno=eno,ename= name,basicpay=bp)
print('Emp no :',employee.emNo)
print('emp name :',employee.emName)
print('Salary of employee',employee.Net_salary())