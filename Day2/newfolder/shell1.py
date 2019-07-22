Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> type(259+33)
<class 'int'>
>>> type(259-33.0)
<class 'float'>
>>> type(4)
<class 'int'>
>>> type('4')
<class 'str'>
>>> type('four')
<class 'str'>
>>> type(5/2.0)
<class 'float'>

>>> type(12 > 2*5)
<class 'bool'>
>>> type(color+3)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(color+3)
NameError: name 'color' is not defined
>>> type('color'*4)
<class 'str'>
>>> #fix:
>>> type('color'+3)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    type('color'+3)
TypeError: must be str, not int
>>> #realfix
>>> type('color'+'3')
<class 'str'>

>>> 
