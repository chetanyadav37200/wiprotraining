import re
'''
txt=input('Enter a text')
bpath=input("Enter beg pattern")
epath=input("Enter end pattern")
bpath='^'+bpath
epath=epath+'$'

if re.search(bpath,txt):
    print("Beginning pattern available")
else:
    print("Beginning pattern is not available")

if re.search(epath,txt):
    print("end pattern available")
else:
    print("end pattern is not available")'''
'''
mbo=input("Enter a text")
pat=r"\d"

if re.fullmatch(pattern=pat,string=mbo):
    print('only digit')
else:
    print('other digit')'''
'''
un=input("Enter UN ")
pat=r"[a-z]{8}$"

if re.match(pat,un):
    print("all 8 digit are lower case")
else:
    print("invalid")'''
'''
email=input("Enter email address")
pat=r"[a-zA-Z0-9_]+@[a-z]+\.[a-z]+$"
if re.match(pat,email):
    print("valid")
else:
    print("invalid")'''

#password
password=input("Enter password")
pat=r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
if re.match(pat,password):
    print("valid")
else:
    print("invalid")