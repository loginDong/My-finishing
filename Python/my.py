print ("Hello,Python")

# cuonter = 100
# mile = 0.04
# name = 'alien'

# print (cuonter)
# print (mile)
# print (name)

# s = 'abcdef'
#截取不包含尾下标的字符.  截取可以接收第三个参数，从startIndex到endIndex之间
# print (s[1:5])


# str = 'Hello World!'
 
# print(str)           # 输出完整字符串
# print(str[0])        # 输出字符串中的第一个字符
# print(str[2:5])      # 输出字符串中第三个至第五个之间的字符串
# print(str[2:])       # 输出从第三个字符开始的字符串
# print(str * 2)       # 输出字符串两次
# print(str + "TEST")  # 输出连接的字符串



# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列
# for i in range(1,5):
# 	for j in range(1,5):
# 		for k in range(1,5):
# 			if(i != j) and (j != k) and (k != i):
# 				print(i,j,k)

# a = 20
# b = 20
# c = 30
# print(a+b,a-b,b/a,b*c)

#取整数，返回商的整数部分，向下取整
# print(9//2)

# 比较运算符	描述	           实例
# ==	    等于 -         比较对象是否相等	(a == b) 返回 False。
# !=	    不等于 -       比较两个对象是否不相等	(a != b) 返回 true.
# <>	    不等于 -       比较两个对象是否不相等	(a <> b) 返回 true。这个运算符类似 != 。
# >	        大于 -         返回x是否大于y	(a > b) 返回 False。
# <	        小于 -         返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。这分别与特殊的变量True和False等价。	(a < b) 返回 true。
# >=	    大于等于	-     返回x是否大于等于y。	(a >= b) 返回 False。
# <=	    小于等于 -	  返回x是否小于等于y。	(a <= b) 返回 true。

# 赋值运算符	描述              	实例
# =	        简单的赋值运算符	    c = a + b 将 a + b 的运算结果赋值为 c
# +=	    加法赋值运算符	    c += a 等效于 c = c + a
# -=	    减法赋值运算符	    c -= a 等效于 c = c - a
# *=	    乘法赋值运算符	    c *= a 等效于 c = c * a
# /=	    除法赋值运算符	    c /= a 等效于 c = c / a
# %=	    取模赋值运算符	    c %= a 等效于 c = c % a
# **=	    幂赋值运算符	        c **= a 等效于 c = c ** a
# //=	    取整除赋值运算符	    c //= a 等效于 c = c // a


# 逻辑运算符	逻辑表达式	描述	                                                                    实例
# and	    x and y	    布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	    (a and b) 返回 20。
# or	    x or y	    布尔"或"	- 如果 x 是非 0，它返回 x 的值，否则它返回 y 的计算值。	            (a or b) 返回 10。
# not	    not x	    布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	    not(a and b) 返回 False
#


# 运算符	    描述	                                                实例
# in	    如果在指定的序列中找到值返回 True，否则返回 False。	    x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
# not in	如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。
# eg:       a = 10
#           b = 20
#           list = [1, 2, 3, 4, 5 ];

#         if ( a in list ):
#            print "1 - 变量 a 在给定的列表中 list 中"
#         else:
#            print "1 - 变量 a 不在给定的列表中 list 中"
#
#         if ( b not in list ):
#            print "2 - 变量 b 不在给定的列表中 list 中"
#         else:
#            print "2 - 变量 b 在给定的列表中 list 中"



#if语句的判断条件可以用>（大于）、<(小于)、==（等于）、>=（大于等于）、<=（小于等于）来表示其关系
# if(a == b):
#     print("a等于b")
# else:
#     print("a和b不相等")

    #判断条件为多个数的时候    python不支持switch语句来判断 都用

# if 判断条件1:
#     执行语句1……
# elif 判断条件2:
#     执行语句2……
# elif 判断条件3:
#     执行语句3……
# else:
#     执行语句4……


# BOARD_SIZE = 8
#
# def under_attack(col, queens):
#    left = right = col
#    for r, c in reversed(queens):
#  #左右有冲突的位置的列号
#        left, right = left - 1, right + 1
#
#        if c in (left, col, right):
#            return True
#    return False
#
# def solve(n):
#    if n == 0:
#        return [[]]
#
#    smaller_solutions = solve(n - 1)
#
#    return [solution+[(n,i+1)]
#        for i in range(BOARD_SIZE)
#            for solution in smaller_solutions
#                if not under_attack(i+1, solution)]
# for answer in solve(BOARD_SIZE):
#    print(answer)


#把一个数组里面的项按照奇数和偶数分成两个不同的数组

#注意空格  嵌套执行的程序要在前面加空格/tab（对齐） 才能执行 否则知识单独执行某一程序

# while 语句时还有另外两个重要的命令 continue，break 来跳过循环，continue 用于跳过该次循环，break 则是用于退出循环

# 如果条件判断语句永远为 true，循环将会无限的执行下去

# while … else 在循环条件为 false 时执行 else 语句块

    # numbers = [6,8,9,7,11,14,23,15,60,77]
    # even = []
    # odd = []
    # while len(numbers) > 0 :
    #     number = numbers.pop()
    #     if (number % 2 == 0):
    #         even.append(number)
    #     else:
    #         odd.append(number)
    #
    # print(even)
    # print(odd)

#break语句
# var = 10
# while var > 0:
#     print('当前变量值 :', var)
#     var = var - 1
#     if var == 5:  # 当变量 var 等于 5 时退出循环
#         break
#
# print("Good bye!")


#continue语句
# var = 10
# while var > 0:
#    var = var -1
#    if var == 5: #当var是5的时候 跳过
#       continue
#    print('当前变量值 :', var)
# print("Good bye!")

#pass语句
# pass 不做任何事情，一般用做占位语句


#ptthon的类型转换
# int(x [,base ])         将x转换为一个整数
# long(x [,base ])        将x转换为一个长整数
# float(x )               将x转换到一个浮点数
# complex(real [,imag ])  创建一个复数
# str(x )                 将对象 x 转换为字符串
# repr(x )                将对象 x 转换为表达式字符串
# eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s )               将序列 s 转换为一个元组
# list(s )                将序列 s 转换为一个列表
# chr(x )                 将一个整数转换为一个字符
# unichr(x )              将一个整数转换为Unicode字符
# ord(x )                 将一个字符转换为它的整数值
# hex(x )                 将一个整数转换为一个十六进制字符串
# oct(x )                 将一个整数转换为一个八进制字符串



# math 模块、cmath 模块

# Python math 模块提供了许多对浮点数的数学运算函数。
# Python cmath 模块包含了一些用于复数运算的函数。

import math
import cmath

#print(len(dir(math))) #['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
#print(dir(cmath))#['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh', 'cos', 'cosh', 'e', 'exp', 'inf', 'infj', 'isclose', 'isfinite', 'isinf', 'isnan', 'log', 'log10', 'nan', 'nanj', 'phase', 'pi', 'polar', 'rect', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau']

# 函数	            返回值 ( 描述 )
# abs(x)	        返回数字的绝对值，如abs(-10) 返回 10
# ceil(x)	        返回数字的上入整数，如math.ceil(4.1) 返回 5
# cmp(x, y)	        如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1
# exp(x)	        返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
# fabs(x)	        返回数字的绝对值，如math.fabs(-10) 返回10.0
# floor(x)	        返回数字的下舍整数，如math.floor(4.9)返回 4
# log(x)	        如math.log(math.e)返回1.0,math.log(100,10)返回2.0
# log10(x)	        返回以10为基数的x的对数，如math.log10(100)返回 2.0
# max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
# min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
# modf(x)	        返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
# pow(x, y)	x**y    运算后的值。
# round(x [,n])	    返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
# sqrt(x)	        返回数字x的平方根

#随机数函数
# choice(seq)	    从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
# randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
# random()	        随机生成下一个实数，它在[0,1)范围内。
# seed([x])	        改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# shuffle(lst)	    将序列的所有元素随机排序
# uniform(x, y)	    随机生成下一个实数，它在[x,y]范围内。

# 三角函数
# acos(x)	    返回x的反余弦弧度值。
# asin(x)	    返回x的反正弦弧度值。
# atan(x)	    返回x的反正切弧度值。
# atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
# cos(x)	    返回x的弧度的余弦值。
# hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
# sin(x)	    返回的x弧度的正弦值。
# tan(x)	    返回x弧度的正切值。
# degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
# radians(x)	将角度转换为弧度

#
# pi	数学常量 pi（圆周率，一般以π来表示）
# e	    数学常量 e，e即自然常数（自然常数）
#
# str1 = "hello World"
# str2 = "python Study"
#
# print ("str1[0]:" , str1[0])
# print ("str2[1:5]:" , str2[1:5])  #不包括5



#Python转义字符：
	# 转义字符		描述
	# \(在行尾时)		续行符
	# \\			反斜杠符号
	# \'			单引号
	# \"			双引号
	# \a			响铃
	# \b			退格(Backspace)
	# \e			转义
	# \000			空
	# \n			换行
	# \v			纵向制表符
	# \t			横向制表符
	# \r			回车
	# \f			换页
	# \oyy			八进制数，yy代表的字符，例如：\o12代表换行
	# \xyy			十六进制数，yy代表的字符，例如：\x0a代表换行
	# \other		其它的字符以普通格式输出


#Python字符串运算符				变量 a 值为字符串 "Hello"，b 变量值为 "Python"：
# 操作符				描述								实例
# +					字符串连接 						>>>a + b    'HelloPython'
# *					重复输出字符串 					>>>a * 2 	'HelloHello'
# []				通过索引获取字符串中字符 			>>>a[1] 	'e'
# [ : ]				截取字符串中的一部分 				>>>a[1:4] 	'ell'
# in				成员运算符 - 如果字符串中包含给定的字符返回 True 		>>>"H" in a 		True
# not in			成员运算符 - 如果字符串中不包含给定的字符返回 True 	>>>"M" not in a 	True
# r/R				原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
# >>>print r'\n' 	\n 		>>> print R'\n' 	\n
# %					格式字符串



# Python字符串格式化  最基本用法：将一个值插入到有字符串格式符%s的字符串中   同C中的sprintf一样
# eg：
# print ("My name is %s and weight is %d kg!" % ('Zara', 21))    # 输出：  My name is Zara and weight is 21 kg!

#字符串格式化符号
# 符号				描述
# %c				格式化字符及其ASCII码
# %s				格式化字符串
# %d				格式化整数
# %u				格式化无符号整型
# %o				格式化无符号八进制数
# %x				格式化无符号十六进制数
# %X				格式化无符号十六进制数（大写）
# %f				格式化浮点数字，可指定小数点后的精度
# %e				用科学计数法格式化浮点数
# %E				作用同 %e，用科学计数法格式化浮点数
# %g 				%f和 %e的简写
# %G 				%f和%E的简写
# %p				用十六进制数格式化变量的地址

#格式化操作符辅助指令
# 符号		功能
# *			定义宽度或者小数点精度
# -			用做左对齐
# +			在正数前面显示加号( + )
# <sp>		在正数前面显示空格
# #			在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
# 0			显示的数字前面填充'0'而不是默认的空格
# %			'%%'输出一个单一的'%'
# (var)		映射变量(字典参数)
# m.n.		m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)




# Python字符串的内建函数：
# 	方法															描述
# string.capitalize() 									把字符串的第一个字符大写
#
# string.center(width) 									返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
#
# string.count(str, beg=0, end=len(string)) 				返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
#
# string.decode(encoding='UTF-8', errors='strict') 		以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'
#
# string.encode(encoding='UTF-8', errors='strict') 		以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
#
# string.endswith(obj, beg=0, end=len(string)) 			检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
#
# string.expandtabs(tabsize=8) 							把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。
#
# string.find(str, beg=0, end=len(string)) 				检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
#
# string.format() 										格式化字符串
#
# string.index(str, beg=0, end=len(string)) 				跟find()方法一样，只不过如果str不在 string中会报一个异常.
#
# string.isalnum() 										如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
#
# string.isalpha() 										如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
#
# string.isdecimal() 										如果 string 只包含十进制数字则返回 True 否则返回 False.
#
# string.isdigit() 										如果 string 只包含数字则返回 True 否则返回 False.
#
# string.islower()										如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
#
# string.isnumeric()										如果 string 中只包含数字字符，则返回 True，否则返回 False
#
# string.isspace()										如果 string 中只包含空格，则返回 True，否则返回 False.
#
# string.istitle()										如果 string 是标题化的(见 title())则返回 True，否则返回 False
#
# string.isupper()										如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
#
# string.join(seq)										以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
#
# string.ljust(width)										返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
#
# string.lower()											转换 string 中所有大写字符为小写.
#
# string.lstrip()											截掉 string 左边的空格
#
# string.maketrans(intab, outtab])						maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
#
# max(str)												返回字符串 str 中最大的字母。
#
# min(str)												返回字符串 str 中最小的字母。
#
# string.partition(str)									有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
#
# string.replace(str1, str2,  num=string.count(str1))		把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
#
# string.rfind(str, beg=0,end=len(string) )				类似于 find()函数，不过是从右边开始查找.
#
# string.rindex( str, beg=0,end=len(string))				类似于 index()，不过是从右边开始.
#
# string.rjust(width)										返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
#
# string.rpartition(str)									类似于 partition()函数,不过是从右边开始查找
#
# string.rstrip()											删除 string 字符串末尾的空格.
#
# string.split(str="", num=string.count(str))				以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+ 个子字符串
#
# string.splitlines([keepends])							按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
#
# string.startswith(obj, beg=0,end=len(string))			检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
#
# string.strip([obj])										在 string 上执行 lstrip()和 rstrip()
#
# string.swapcase()										翻转 string 中的大小写
#
# string.title()											返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
#
# string.translate(str, del="")							根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 del 参数中
#
# string.upper()											转换 string 中的小写字母为大写
#
# string.zfill(width)										返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0




# Python 列表脚本操作符

# Python表达式				 		结果									描述
# len([1, 2, 3])			 		3									长度
# [1, 2, 3] + [4, 5, 6]			[1, 2, 3, 4, 5, 6]					组合
# ['Hi!'] * 4						['Hi!', 'Hi!', 'Hi!', 'Hi!']		重复
# 3 in [1, 2, 3]					True								元素是否存在于列表中
# for x in [1, 2, 3]: print x,	1 2 3								迭代


# Python包含以下函数:
# 方法						概述
# 1	cmp(list1, list2)		# 比较两个列表的元素
# 2	len(list)				# 列表元素个数
# 3	max(list)				# 返回列表元素最大值
# 4	min(list)				# 返回列表元素最小值
# 5	list(seq)				# 将元组转换为列表


# Python包含以下方法:
# 方法						概述
# 1	list.append(obj)		# 在列表末尾添加新的对象
# 2	list.count(obj)			# 统计某个元素在列表中出现的次数
# 3	list.extend(seq)		# 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# 4	list.index(obj)			# 从列表中找出某个值第一个匹配项的索引位置
# 5	list.insert(index, obj) # 将对象插入列表
# 6	list.pop([index=-1])	# 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# 7	list.remove(obj)		# 移除列表中某个值的第一个匹配项
# 8	list.reverse()			# 反向列表中元素
# 9	list.sort(cmp=None, key=None, reverse=False)		# 对原列表进行排序


print("元组")
# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合  元素不可以删除 但是可以用del删除整个元组
# len() 计算个数  + 拼接    *  复制   in 元素是否存在

#元组的内置函数
# 序号			方法						描述
# 1			cmp(tuple1, tuple2)		比较两个元组元素。
# 2			len(tuple)				计算元组元素个数。
# 3			max(tuple)				返回元组中元素最大值。
# 4			min(tuple)				返回元组中元素最小值。
# 5			tuple(seq)				将列表转换为元组。




print("Python 字典（Dictionary)")
#字典是另一种可变容器类型且可以存储任意类型对象
#字典的格式   d = {key1 : value1, key2 : value2 }
# 访问字典里的值： dictName['attrName']    修改字典  直接赋值     del dict['Name']删除键是'Name'的条目     dict.clear()清空词典所有条目    del dict删除词典
#1)  不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
#2)  键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行

#字典的内置函数和方法
#cmp(dict1,dict2) 比较两个字典元素   len(dict)计算字典长度     str(dict) 输出字典可打印的字符串表示

#字典所包含的内置方法
# 函数	                                描述
# 1	dict.clear()                        删除字典内所有元素
# 2	dict.copy()                         返回一个字典的浅复制
# 3	dict.fromkeys(seq[, val])           创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值   没有seq后面的list 默认值都显示为none  只有一个X的话  所有的seq里面的每个值的默认值都显示为这个X
# 4	dict.get(key, default=None)         返回指定键的值，如果值不在字典中返回default值
# 5	dict.has_key(key)                   如果键在字典dict里返回true，否则返回false
# 6	dict.items()                        以列表返回可遍历的(键, 值) 元组数组
# 7	dict.keys()                         以列表返回一个字典所有的键
# 8	dict.setdefault(key, default=None)  和get()类似, 但如果键不存在于111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111字典中，将会添加键并将值设为default
# 9	dict.update(dict2)                  把字典dict2的键/值对更新到dict里
#10 dict.values()                       以列表返回字典中的所有值
#11 pop(key[,default])                  删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
#12 popitem()                           随机返回并删除字典中的一对键和值。


#首字母大写
# name = "dong li yang   "
# print(name.title()) -->"Dong Li Yang"      #upper()全部字母大写   lower()全部字母小写
# print(name.rstrip())    #删除字符串末尾的空白，只是暂时性的删除 如果需要永久性的删除 吧新的结果存储到原来的变量名中   lstrip() 删除开头的空白

# first_name = "Dong"
# last_name = "Liyang"
# full_name = first_name + " " + last_name
# print(full_name + " said:'good good study,day day up !'")


# list中添加元素 append()追加 insert()指定位置插入

print("Python时间和日期")

import time;
# task = time.time()
# print("当前时间戳为：",task)
# python函数用一个元组装起来的九组数字来处理时间
# 序号	    属性	            值
# 0	        tm_year	        2008
# 1	        tm_mon	        1 到 12
# 2	        tm_mday	        1 到 31
# 3	        tm_hour	        0 到 23
# 4	        tm_min	        0 到 59
# 5	        tm_sec	        0 到 61 (60或61 是闰秒)
# 6	        tm_wday	        0到6 (0是周一)
# 7	        tm_yday	        1 到 366(儒略历)
# 8     	tm_isdst	    -1, 0, 1, -1是决定是否为夏令时的旗帜

# 当前时间
# localTime = time.localtime(time.time())
# print("本地时间为：",localTime)   #>>> time.struct_time(tm_year=2019, tm_mon=3, tm_mday=4, tm_hour=16, tm_min=40, tm_sec=28, tm_wday=0, tm_yday=63, tm_isdst=0) <元组>

# 获取格式化时间                           
# nowTime = time.asctime(time.localtime(time.time()))
# print("当前时间为：",nowTime)  #  Mon Mar  4 16:43:17 2019

#格式化日期
# 格式化成2016-03-20 11:45:39形式
# print(time.strftime("%Y-%m-%d %H:%M:%s",time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式
# print("print(time.strftime('%a %d %d %H:%M:%s %Y')) ")

# 将格式字符串转换为时间戳
# a = "Sat Mar 28 22:24:24 2016"
# print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

# 时间日期格式化符号
# %y    两位数的年份表示（00-99）
# %Y    四位数的年份表示（000-9999）
# %m    月份（01-12）
# %d    月内中的一天（0-31）
# %H    24小时制小时数（0-23）
# %I    12小时制小时数（01-12）
# %M    分钟数（00=59）
# %S    秒（00-59）
# %a    本地简化星期名称
# %A    本地完整星期名称
# %b    本地简化的月份名称
# %B    本地完整的月份名称
# %c    本地相应的日期表示和时间表示
# %j    年内的一天（001-366）
# %p    本地A.M.或P.M.的等价符
# %U    一年中的星期数（00-53）星期天为星期的开始
# %w    星期（0-6），星期天为星期的开始
# %W    一年中的星期数（00-53）星期一为星期的开始
# %x    本地相应的日期表示
# %X    本地相应的时间表示

# calendar模块

import calendar;
# cal = calendar.month(2019,3)
# print("2019-3 日历：")
# print(cal) --->>>           March 2019
#                         Mo Tu We Th Fr Sa Su
#                                      1  2  3
#                          4  5  6  7  8  9 10
#                         11 12 13 14 15 16 17
#                         18 19 20 21 22 23 24
#                         25 26 27 28 29 30 31


# Time模块
#     time.timezone       属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）。
# 	  time.tzname         属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。

# Time模块包含的内置模块  有时间处理的 有转换时间格式的
# 序号	    函数                         描述
# 1	    time.altzone                返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
# 2	    time.asctime([tupletime])   接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
# 3	    time.clock( )               用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
# 4	    time.ctime([secs])          作用相当于asctime(localtime(secs))，未给参数相当于asctime()
# 5	    time.gmtime([secs])         接收时间戳（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
# 6	    time.localtime([secs])      接收时间戳（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
# 7	    time.mktime(tupletime)      接受时间元组并返回时间戳（1970纪元后经过的浮点秒数）。
# 8	    time.sleep(secs)            推迟调用线程的的运行，secs指秒数
# 9	    time.strftime(fmt[,tupletime])      接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
# 10	time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')   根据fmt的格式把一个时间字符串解析为时间元组。
# 11	time.time( )                返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
# 12	time.tzset()                根据环境变量TZ重新初始化时间相关设置。

# calendar模块
# 内置函数
# 序号	        函数及描述
# 1	        calendar.calendar(year,w=2,l=1,c=6)             返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
# 2	        calendar.firstweekday( )                        返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
# 3	        calendar.isleap(year)                           是闰年返回 True，否则为 False。
    #                                                       eg：  >>> import calendar
    #                                                             >>> print(calendar.isleap(2000))
    #                                                             True
    #                                                             >>> print(calendar.isleap(1900))
    #                                                             False
# 4	        calendar.leapdays(y1,y2)                        返回在Y1，Y2两年之间的闰年总数。
# 5	        calendar.month(year,month,w=2,l=1)              返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
# 6	        calendar.monthcalendar(year,month)              返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
# 7	        calendar.monthrange(year,month)                 返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
# 8	        calendar.prcal(year,w=2,l=1,c=6)                相当于 print calendar.calendar(year,w,l,c).
# 9	        calendar.prmonth(year,month,w=2,l=1)            相当于 print calendar.calendar（year，w，l，c）。
# 10	    calendar.setfirstweekday(weekday)               设置每周的起始日期码。0（星期一）到6（星期日）。
# 11	    calendar.timegm(tupletime)                      和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间戳（1970纪元后经过的浮点秒数）。
# 12	    calendar.weekday(year,month,day)                返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。


import time;
import calendar;
# （1）当前时间戳
# 1538271871.226226
time.time()

# （2）时间戳 → 时间元组，默认为当前时间
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=3, tm_hour=9, tm_min=4, tm_sec=1, tm_wday=6, tm_yday=246, tm_isdst=0)
time.localtime()
time.localtime(1538271871.226226)

# （3）时间戳 → 可视化时间
# time.ctime(时间戳)，默认为当前时间
time.ctime(1538271871.226226)

# （4）时间元组 → 时间戳
# 1538271871
time.mktime((2018, 9, 30, 9, 44, 31, 6, 273, 0))

# （5）时间元组 → 可视化时间
# time.asctime(时间元组)，默认为当前时间
time.asctime()
time.asctime((2018, 9, 30, 9, 44, 31, 6, 273, 0))
time.asctime(time.localtime(1538271871.226226))

# （6）时间元组 → 可视化时间（定制）
# time.strftime(要转换成的格式，时间元组)
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# （7）可视化时间（定制） → 时间元祖
# time.strptime(时间字符串，时间格式)
print(time.strptime('2018-9-30 11:32:23', '%Y-%m-%d %H:%M:%S'))

# （8）浮点数秒数，用于衡量不同程序的耗时，前后两次调用的时间差
time.clock()


#使用datetime来获取当前的时间和日期
# import datetime
# i = datetime.datetime.now()
# print ("当前的日期和时间是 %s" % i)
# print ("ISO格式的日期和时间是 %s" % i.isoformat() )
# print ("当前的年份是 %s" %i.year)
# print ("当前的月份是 %s" %i.month)
# print ("当前的日期是  %s" %i.day)
# print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
# print ("当前小时是 %s" %i.hour)
# print ("当前分钟是 %s" %i.minute)
# print ("当前秒是  %s" %i.second)


# Python函数
print("自定义一个函数 函数代码块以def关机看次开头 后接函数表示符名称和圆括号() , 参数和自变量放在圆括号中间 也可以定义参数")
print("函数内容以冒号起始，并且缩进      return[表达式]结束函数 选择性的返回一个值给调用房 不带表达式的return相当于返回None")
# 实例：  def printme( str ):
#            "打印传入的字符串到标准显示设备上"
#            print str
#            return    #将字符串作为传入参数并打印到标准显示设备上

        #printme("调用函数")

#加了*的变量名会存放所有为命名的变量参数 （不定长参数   同argumrnts参数一样）
# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return;

# 调用printinfo 函数
# printinfo(10);   ==>>>输出:10
# printinfo(70, 60, 50);   ==>>>输出:70 60 50

# 匿名函数

# lambda表达式来创建匿名函数
# sum = lambda arg1, arg2: arg1 + arg2;
# print "相加后的值为 : ", sum( 10, 20 ) ==>>相加后的值为 :  30
# print "相加后的值为 : ", sum( 20, 20 ) ==>>相加后的值为 :  40


# total = 0;  # 这是一个全局变量
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2;  # total在这里是局部变量.
#     print("函数内是局部变量 : ", total)
#     return total;
#
#
# # 调用sum函数
# sum(10, 20);
# print("函数外是全局变量 : ", total)
# 函数内是局部变量 :  30
# 函数外是全局变量 :  0




# Python模块
# import 模块名
# 调用引入模块里面的函数

# from...import 模块名
# 引入...模块里面指定的某一部分
# from...import *
# 引入...模块里面所有的内容


















