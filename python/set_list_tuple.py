Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
type(s1)
<class 'str'>
id(s1)
3116680754688
s='hi'
id(s2)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    id(s2)
NameError: name 's2' is not defined. Did you mean: 's1'?
is(s)
SyntaxError: invalid syntax
id(s)
140712781821368
s3=s1
id(s3)
3116680754688
list1=[10,12,13,15]
type(list1)
<class 'list'>
list1[2]
13
list1[1::2]
[12, 15]
list1[::2]
[10, 13]
list1[::2]
[10, 13]
list('india')
['i', 'n', 'd', 'i', 'a']
id(list1)
3116638391232
list2=[100,100,True,'hi',68.9]
list2
[100, 100, True, 'hi', 68.9]
list2[1]
100
list2[1]=1001
list2
[100, 1001, True, 'hi', 68.9]
lis12.append(23)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    lis12.append(23)
NameError: name 'lis12' is not defined. Did you mean: 'list2'?
list2.append(23)
list2
[100, 1001, True, 'hi', 68.9, 23]
list2.remove('23')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list2.remove('23')
ValueError: list.remove(x): x not in list
list2.remove(23)
list2
[100, 1001, True, 'hi', 68.9]
list2.append(2000)
list2
[100, 1001, True, 'hi', 68.9, 2000]
list2.remove(list2[5])
list2
[100, 1001, True, 'hi', 68.9]
list2.insert(2,24)
list2
[100, 1001, 24, True, 'hi', 68.9]
list1.clean()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    list1.clean()
AttributeError: 'list' object has no attribute 'clean'. Did you mean: 'clear'?
list1.clear()
list1
[]
del(list1)
list1
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    list1
NameError: name 'list1' is not defined. Did you mean: 'list2'?
tuple1=(11,11.2,'h1')
tuple1
(11, 11.2, 'h1')
tuple1[1]
11.2
tuple1[3]=3
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    tuple1[3]=3
TypeError: 'tuple' object does not support item assignment
tuple1[:2]
(11, 11.2)
tuple.index(11.2)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    tuple.index(11.2)
TypeError: descriptor 'index' for 'tuple' objects doesn't apply to a 'float' object
tuple1.index(11.2)
1
tuple1.count('hi')
0
tuple1.count('h1')
1
tuple2=tuple1
id(tuple1)
3116683390352
id(tuple2)
3116683390352
>>> se1={10,20,30}
>>> se1
{10, 20, 30}
>>> set.add(40)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    set.add(40)
TypeError: descriptor 'add' for 'set' objects doesn't apply to a 'int' object
>>> set1.add(40)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    set1.add(40)
NameError: name 'set1' is not defined. Did you mean: 'se1'?
>>> set1.add('40')
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    set1.add('40')
NameError: name 'set1' is not defined. Did you mean: 'se1'?
>>> se1.add(40)
>>> se2=se1
>>> se2
{40, 10, 20, 30}
>>> se1.remove(40)
>>> se1
{10, 20, 30}
>>> se2
{10, 20, 30}
>>> se2.remove(10)
>>> se2
{20, 30}
>>> se1
{20, 30}
>>> se2.append(20)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    se2.append(20)
AttributeError: 'set' object has no attribute 'append'
