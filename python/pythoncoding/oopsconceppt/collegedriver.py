import teacher

from oopsconceppt.college import college
from oopsconceppt.stud import student
from oopsconceppt.teacher import Teacher
from oopsconceppt.studentgrad import StudentGrade

cc=int(input("Enter college code"))
cn=input("Enter college nane")
ci=input("Enter college city")

'''project=college(cc,cn,ci)

project.welcomr_msg()
project.display_college_detail()'''
'''
sr=int(input("enter student roll number"))
sn=input("Enter student name")
m1=int(input("Enter marks 1"))
m2=int(input("Enter marks 2"))
m3=int(input("Enter marks 3"))'''

'''
stu = StudentGrade(sr,sname=sn,m1=m1,m2=m2,m3=m3,ccode=cc,cnsme=cn,ccity=ci)
stu.display_college_detail()
stu.welcomr_msg()
print(f"student rollnumber :{stu.srollno}")
print(f"student name :{stu.stname}")
print(f"total :{stu.calclate_total()}")
print(f"average :{stu.calculate_average()}")
print(f"Grade :{stu.calculate_grade()} \n Result :{stu.calculate_result()}")
'''

tId=int(input("Enter id"))
tnam=input("Enter teacher name")
tbasic=float(input("Enter salary"))
teach = Teacher(ccode=cc,cnsme=cn,ccity=ci,tn=tnam, ti=tId,tbp=tbasic)
print(f"Teacher Id :{teach.teid} \n teacher name:{teach.tname}")
print(f"Salary :{teach.calculate_salary()}")
