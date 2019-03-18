Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> a = list()
>>> a
[]
>>> b = "anqi is a beauty"
>>> b
'anqi is a beauty'
>>> b = list(b)
>>> b
['a', 'n', 'q', 'i', ' ', 'i', 's', ' ', 'a', ' ', 'b', 'e', 'a', 'u', 't', 'y']
>>> 
>>> c = (1,1,2,4,5,7,8)
>>> c = list(c)
>>> c
[1, 1, 2, 4, 5, 7, 8]
>>> len(b)
16
>>> max(b)
'y'
>>> chars = "135790"
>>> min(chars)
'0'
>>> 
====== RESTART: C:/Users/橘子。/Desktop/python_learning/learning_15_max.py ======
Traceback (most recent call last):
  File "C:/Users/橘子。/Desktop/python_learning/learning_15_max.py", line 1, in <module>
    max = tuple[0,2,4,6,7,9]
TypeError: 'type' object is not subscriptable
>>> max = tuple[0,2,4,6,7,9]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    max = tuple[0,2,4,6,7,9]
TypeError: 'type' object is not subscriptable
>>> max = tuple[0]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    max = tuple[0]
TypeError: 'type' object is not subscriptable
>>> sorted(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    sorted(b)
NameError: name 'b' is not defined
>>> b = [1,2,4,6,8,7,8]
>>> sorted(b)
[1, 2, 4, 6, 7, 8, 8]
>>> reversed(b)
<list_reverseiterator object at 0x02C07CF0>
>>> list(reversed(b))
[8, 7, 8, 6, 4, 2, 1]
>>> enumerate(b)
<enumerate object at 0x02C1D468>
>>> list(enumerate(b))
[(0, 1), (1, 2), (2, 4), (3, 6), (4, 8), (5, 7), (6, 8)]
>>> 
>>> a = [1,2,3,5,7,9]
>>> b = ["a","c","f"]
>>> list(zip(a,b))
[(1, 'a'), (2, 'c'), (3, 'f')]
>>> 
