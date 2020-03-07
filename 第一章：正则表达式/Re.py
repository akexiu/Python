#正则表达式
import re
from random import randrange,choice
from string import ascii_lowercase as ls
from sys import maxsize
from time import  ctime


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
"""使用sub和subn搜索与替换"""
#第三个参数中包含第一个参数的值替换成第二个参数，大小写有区别
print(re.sub("[abc]","D","abcdefabcd"))
print(re.subn("[abc]","D","abcdefabcd"))#替换并且返回替换的总数量

"""复杂的字符串分割 split分割符"""
print(re.split(":","a:b:c"))
DATE = ("Linux","Windows","Apple","YouSee")
for date in DATE:
    print(re.split(", |(?=(?:\d{4}|[A-Z]{2}))",date))
    #r"(?i)" 忽略大小写
    # r"(?s)"表示（.）号区分大小写
    # r"(?x)" 该标允许用户通过抑制在正则表达式中使用空白符来创建更加易懂的表达式，
print(re.findall(r"(?x)yes","/yes \/yesa. YES||"))

"""读取文件"""
f=open("C:\\Users\\Administrator\\Desktop\\git基本操作.txt","r")
for ls in f:
    print(ls)
f.close()

"""正则表达式练习数据生成器 以下生产有点问题"""
tlds =('com','edu','net','org','gov')
for i in range(randrange(5,11)):
    dtint = randrange(maxsize)
    dtstr = ctime(dtint)
    llen =  randrange(4,8)
    login = "a".join(choice(ls) for j in range(llen))
    dlen = randrange(llen,13)
    dom = "c".join(choice(ls) for j in range(dlen))
    print("%s::%s@%s.%s::%d-%d-%d" % (dtstr,login,dom,choice(tlds),dtint,llen,dlen))
    print(dom)

"""明天继续：第二章，网络编程，2020-3-7"""