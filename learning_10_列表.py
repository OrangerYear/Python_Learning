Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #创建普通列表
>>> member = ["anqi","beauty"]
>>> number = [1,3,5,7,9]
>>> 
>>> 
>>> #创建混合列表
>>> mix = [1,"anqi",[1,2]]
>>> 
>>> #空列表
>>> empty = []
>>> 
>>> 
>>> #向列表添加元素
>>> member.append("beautiful")#append只能加一个
>>> member
['anqi', 'beauty', 'beautiful']
>>> 
>>> member.extend("wonderful")#按字母加一个
>>> member
['anqi', 'beauty', 'beautiful', 'w', 'o', 'n', 'd', 'e', 'r', 'f', 'u', 'l']
>>> 
>>> member.extend(["shine","diamond"])#加多个
>>> member
['anqi', 'beauty', 'beautiful', 'w', 'o', 'n', 'd', 'e', 'r', 'f', 'u', 'l', 'shine', 'diamond']
>>> 
>>> member.insert(0,"gift")#指定添加位置
>>> member
['gift', 'anqi', 'beauty', 'beautiful', 'w', 'o', 'n', 'd', 'e', 'r', 'f', 'u', 'l', 'shine', 'diamond']
>>> 
>>> 
>>> #交换位置
>>> temp = member[0]
>>> member[0] = member[1]
>>> member[1]=temp
>>> member
['anqi', 'gift', 'beauty', 'beautiful', 'w', 'o', 'n', 'd', 'e', 'r', 'f', 'u', 'l', 'shine', 'diamond']
>>> 
>>> 
>>> #删除元素
>>> member.remove("anqi")
>>> member
['gift', 'beauty', 'beautiful', 'w', 'o', 'n', 'd', 'e', 'r', 'f', 'u', 'l', 'shine', 'diamond']
>>> 
>>> del member[0]
>>> member
['beauty', 'beautiful', 'w', 'o', 'n', 'd', 'e', 'r', 'f', 'u', 'l', 'shine', 'diamond']
>>> 
>>> member.pop()
'diamond'
>>> member
['beauty', 'beautiful', 'w', 'o', 'n', 'd', 'e', 'r', 'f', 'u', 'l', 'shine']
>>> member.pop(1)
'beautiful'
>>> member
['beauty', 'w', 'o', 'n', 'd', 'e', 'r', 'f', 'u', 'l', 'shine']
>>> 
>>> 
>>> 
>>> #列表分片
>>> member[1:3]
['w', 'o']
>>> member[:3]
['beauty', 'w', 'o']
>>> member[1:]
['w', 'o', 'n', 'd', 'e', 'r', 'f', 'u', 'l', 'shine']
>>> member[:]
['beauty', 'w', 'o', 'n', 'd', 'e', 'r', 'f', 'u', 'l', 'shine']
>>> copymember = member
>>> copymember
['beauty', 'w', 'o', 'n', 'd', 'e', 'r', 'f', 'u', 'l', 'shine']
>>> 
