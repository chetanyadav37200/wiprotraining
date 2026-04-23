Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> dic1(1:10,2:20,3:30}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> dic1=(1:10,2:20,3:30}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> dic1={1:10, 2:20, 3:30}
>>> dic1
{1: 10, 2: 20, 3: 30}
>>> dic2={'a':10,'b':20}
>>> dic2['b']
20
>>> dic2['c']=30
>>> dic2
{'a': 10, 'b': 20, 'c': 30}
>>> dic2.keys()
dict_keys(['a', 'b', 'c'])
>>> dic2.values()
dict_values([10, 20, 30])
