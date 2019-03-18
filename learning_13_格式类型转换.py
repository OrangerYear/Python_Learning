Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> "{0} is {1} {2}".format("anqi","a","beauty")
'anqi is a beauty'
>>> #传递到fomat方法 再传递到参数
>>> "{0} is {1} {2}".format(0 = "anqi",1 = "a",2 ="beauty")
SyntaxError: keyword can't be an expression
>>>  "{a} is {b} {c}".format(a = "anqi",b = "a",c ="beauty")
SyntaxError: unexpected indent
>>> "{a} is {b} {c}".format(a = "anqi",b = "a",c ="beauty")
'anqi is a beauty'
>>> 
>>> 
>>> #ASCII码
>>> "%c" % 97
'a'
>>> "%c %c %c" % (97,98,99)
'a b c'
>>> 
