Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
type(s1)
<class 'str'>
s1.upper()
'HELLO'
s1.capitalize
<built-in method capitalize of str object at 0x000002731DEE37E0>
s1.capitalize()
'Hello'
s1.lower()
'hello'
s1='hELLo'
s1.casefold()
'hello'
s1='HEllo'
s1.casefold()
'hello'
s1.count()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s1.count()
TypeError: count expected at least 1 argument, got 0
s1.count('h')
0
s1.count('H')
1
s1.count(casefold('h'))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s1.count(casefold('h'))
NameError: name 'casefold' is not defined
s1=s1.casefold()
s1.count('l')
2
s1.count('h')
1
11
11


s1.isalppha()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s1.isalppha()
AttributeError: 'str' object has no attribute 'isalppha'. Did you mean: 'isalpha'?
s1.isdigit()
False
>>> s1.removeprefix("h')
...                 
SyntaxError: unterminated string literal (detected at line 1)
>>> 
>>> s1.removeprefix('h')
...                 
'ello'
>>> s1='how are you'
...                 
>>> s1.split(' ')
...                 
['how', 'are', 'you']
>>> 
>>> s1='hello there!!!'
...                 
>>> s1.len()
...                 
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s1.len()
AttributeError: 'str' object has no attribute 'len'
>>> len(s1)
...                 
14
>>> s1[2,12:2]
...                 
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    s1[2,12:2]
TypeError: string indices must be integers, not 'tuple'
>>> s1[2:12:2]
...                 
'lotee'
>>> s1[::2]
...                 
'hlotee!'
