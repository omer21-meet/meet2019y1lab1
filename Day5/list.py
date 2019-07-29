Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = ['she','sells','sea','shells','by','the','sea','shore']
>>> b = "selfish shellfish"
>>> c = [1, 1, 2, 3, 5, 8, 13]
>>> b[3:4]
'f'
>>> c[6]
13
>>> c[5]
8

>>> c[:-2]
[1, 1, 2, 3, 5]
>>> a[2]
'sea'
>>> b[0:4]
'self'
>>> 'by' in a
True
>>> a[2] == a[6]
True
>>> 
>>> 'self' in b
True
>>> [1,2,5] in c
False
>>> [1,1,2] in c
False
>>> [1] in c
False
>>> c = ['1', '2', '3', '5','6']
>>> ['1] in c
     
SyntaxError: EOL while scanning string literal
>>> ['1'] in c
     
False
>>> [1] in c
     
False
>>> '1' in c
     
True
>>> [1,2,5] in c
     
False
>>> c = [1,1,2,5,8,13]
     
>>> 1,2,5 in c
     
(1, 2, True)
>>> c = [1,1,2,3,5,8,13]
     
>>> [1,2,5] in c
     
False
>>> gs
     
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    gs
NameError: name 'gs' is not defined
>>> [sh] in c
     
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    [sh] in c
NameError: name 'sh' is not defined
>>> 'sh' in c
     
False
>>>  a[3] == b[8:13]
     
SyntaxError: unexpected indent
>>> a[3] == b[8:13]
     
False
>>> 
