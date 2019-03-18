Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> str = "anqi is a beauty"
>>> str[3:]
'i is a beauty'
>>> 
>>> 
>>> str1 = str[9:] + "lovely" + str[9:]
>>> str1
' beautylovely beauty'
>>> 
>>> #首字母大写
>>> str = "anqi is a beauty"
>>> str1 = str
>>> str1.capitalize()
'Anqi is a beauty'
>>> 
>>> 
>>> #全部改为小写
>>> str1.casefold()
'anqi is a beauty'
>>> 
>>> #居中
>>> str.center(30)
'       anqi is a beauty       '
>>> 
>>> #寻找
>>> str.count(e,[:])
SyntaxError: invalid syntax
>>> str.count(e)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    str.count(e)
NameError: name 'e' is not defined
>>> str.count("e")
1
>>> 
>>> 
>>> #是否以该元素结尾
>>> str.endswith("e")
False
>>> 
>>> 
>>> #替换空格 默认空格字符为8
>>> str3 = "anqi\tis\tbeauty"
>>> str3.expandtabs()
'anqi    is      beauty'
>>> str3.expandtabs([tabspace=4])
SyntaxError: invalid syntax
>>> str3.expandtabs(4)
'anqi    is  beauty'
>>> 
>>> 
>>> #检测是否在字符串中
>>> str.find("e")
11
>>> 
>>> 
>>> #index检测 不在字符串中时会返回异常
>>> str.index("w")
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    str.index("w")
ValueError: substring not found
>>> 
>>> 
>>> #字符串中至少有一个字符 且 所有字符均为字母或数字则true
>>> str.isalnum()
False
>>> str4="anqiisbeauty"
>>> str4.isalnum()
True
>>> 
>>> 
>>> 
>>> #字符串中至少有一个字符 且 所有字符均为字母则true
>>> str4.isalpha()
True
>>> 
>>> 
>>> #字符串中至少有一个字符 且 所有字符均为数字则true
>>> str4.isdigit()
False
>>> 

>>> 
>>> #至少包含一个区分大小写的字符 且全为小写 则true
>>> str.islower()
True
>>> 
>>> 
>>> #只包含数字
>>> str.isnumeric()
False
>>> 
>>> 
>>> #只包含空格
>>> str.isspace()
False
>>> 
>>> 
>>> #只包含大写
>>> str.istitle()
False
>>> 
>>> 
>>> #是否标题化/ 所有单词首字母均大写
>>> str.istitle()
False
>>> 
>>> 
>>> #只包含大写（不要在意上面那个错了的）
>>> str.isupper()
False
>>> 
>>> 
>>> #选作分隔符
>>> str.join("12345")
'1anqi is a beauty2anqi is a beauty3anqi is a beauty4anqi is a beauty5'
>>> str.join("1 2 3 4 5")
'1anqi is a beauty anqi is a beauty2anqi is a beauty anqi is a beauty3anqi is a beauty anqi is a beauty4anqi is a beauty anqi is a beauty5'
>>> 
>>> 
>>> #左对齐
>>> str.ljust()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    str.ljust()
TypeError: ljust() takes at least 1 argument (0 given)
>>> str.ljust(30)
'anqi is a beauty              '
>>> 
>>> 
>>> ##去掉字符串左边空格
>>> str6 = "    anqi"
>>> str6.lstrip()
'anqi'
>>> 
>>> 
>>> #选取分隔符将字符串分割为三元组
>>> str2=str
>>> str2.rpartition("is")
('anqi ', 'is', ' a beauty')
>>> 
>>> 
>>> #替换
>>> str2.replace("anqi","feizai")
'feizai is a beauty'
>>> 
>>> 
>>> 
>>> #默认空格切割字符串
>>> str2.split()
['anqi', 'is', 'a', 'beauty']
>>> 
>>> 
>>> #大小写转换
>>> str.swapcase();
'ANQI IS A BEAUTY'
>>> 
>>> 
>>> 
>>> 
>>> #指定内容转换
>>> str.translate(str.maketrans("s","t"))
'anqi it a beauty'
>>> 
>>> 
>>> 
