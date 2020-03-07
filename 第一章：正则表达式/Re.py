#正则表达式
import re


c = re.compile('as')
print(c.groupindex)

'''匹配成功，则输出匹配的内容'''
m = re.match('foo','foo1')
if m is not None:
    print(m.group())

'''search 在字符串中模糊查询'''
s =re.search('foo','sea food')
if s is not None:
    print(s.group())

'''（. 号不能匹配 \n 和空字符串）'''
pointstr = '3.14'
mp = re.match(pointstr,'3014')
print(mp.group())

"""创建字符集 【】"""
str = '[cr][up]'
mstr = re.match(str,'cu') #匹配cu
print(mstr.group())

"""重复特殊字符以及分组"""
patt = '\w+@(\w+\.)*\w+\.com'
print(re.match(patt,'akexiu@a.com').group())

"""子组"""
sonstr = '(\w\w\w)-(\d\d\d)'
print(re.match(sonstr,'abc-123').group(2))
print(re.match(sonstr,'abc-123').groups())

"""findall() finditer 查询每一次出现的位置"""
print(re.findall('a','banana'))
print(re.finditer(r'(c\w+)','china check',re.I).__next__().group(1))

"""1.3.12 2020-3-7明天继续"""