Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #元组
>>> tuple = (1,3,4,5,6,8,9)
>>> 
>>> tuple(0)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tuple(0)
TypeError: 'tuple' object is not callable
>>> tuple[0]
1
>>> tuple[2:]
(4, 5, 6, 8, 9)
>>> tuple[1] = 5
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple[1] = 5
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> temp = (1)
>>> type(temp)
<class 'int'>
>>> 
>>> temp = 1,2,3,4
>>> type(temp)
<class 'tuple'>
>>> 
>>> 
>>> 3*temp
(1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
>>> #*不再作为乘号，而是用来重复
>>> 
>>> 
>>> #添加元素
>>> temp = temp[:2] + ("anqi",) + temp(2:)
SyntaxError: invalid syntax
>>> temp = temp[:2] + ("anqi",) + temp(2:)
SyntaxError: invalid syntax
>>> temp = temp[:2] + ("anqi",) + temp[2:]
>>> temp
(1, 2, 'anqi', 3, 4)
>>> 
>>> 
>>> 
