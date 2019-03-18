Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> number = [1 3 5 7 8 9]
SyntaxError: invalid syntax
>>> number = [1,3,5,7,8,9]
>>> #计算参数在列表中出现的次数
>>> number.count(2)
0
>>> #寻找参数出现的位置
>>> number.index(5)
2
>>> #在指定范围内寻找
>>> number.index(5,1,3)
2
>>> #列表倒序
>>> number.reverse()
>>> number
[9, 8, 7, 5, 3, 1]
>>> 
>>> 
>>> #升序排列
>>> number.sort()
>>> number
[1, 3, 5, 7, 8, 9]
>>> 
>>> #降序排列
>>> number.sort(reverse = True)
>>> number
[9, 8, 7, 5, 3, 1]
>>> 
