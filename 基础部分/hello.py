#!/usr/bin/env python3 
print('你好，这是第一个Python的程序')


# name = input('请输入你的名字！！')
# print('喔，你很帅哦', name)


print('\'使用了转义符')

a = '我是a'
b = a
a = '我不是a'
print(b)    # 打印的是 ‘我是啊’  证明是浅拷贝 只是指向a的地址

HOME = '用全部大写来表示常量'
longStr = '''试一下
...ddd
...这是多行字符串
...dddd..'''
print(longStr)
if HOME :
    print(HOME)   # 这种方式是代码块  {  }  但是 要空格缩进

# 运算的话 有and or not  对应 && || ！  
# 除法 用 /  有小数    // 没有小数  
s1 = 72
s2 = 85
r = 85 - 72 
r = r / 72 *100
print('%.2f%%'%r)

# list 等于js中的数组
arr = ['老王','小张']
arr[-1]    # 取倒数第一个 -2 倒数第二个 以此类推
len(arr)   # 数组的长度
arr.append('我是添加的元素')             # 添加到数组的最后面 类似push
arr.insert(1,'我要插入到下标为1的地方')    # 插入到指定的位置 
arr.pop()                   # 删除最后一个
print(arr)

# tuple 不可变数组  用（）不是[]  就是不可变了  也不能添加删除
fixArr = ('老张','老王','老孔')

# 流程控制
who = False
are = True
if who:
    print('你好')
elif are:
    print('你不好')   # elif - -！这种写法真的好吗 。。。。elif
else:
    print('你是傻逼')

# 循环 for item in XXX:  for in这种语法好像js中也有 不过好像是取对象中的属性
for item in list(range(10)):
    print(item)

# 字典
dic = {'haha':100}
dicVal = dic['haha']
print(dicVal)    
# 判断是否存在
print('haha' in dic)     
print(dic.get('hah','没有值就显示我'))  #dic.get('key')
'''
    这个多行注释 我是服气的！！！！

    和list比较，dict有以下几个特点：

    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
    而list相反：

    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。

'''

# 函数 
# 使用def来定义哦 然后依次是函数名 （形参）： 然后是函数内容 
# 默认参数必须指向不变对象 
# 默认参数 默认按照顺序来取参数 若要改变顺序 指定改变默认值  a= "值"
# 可以运行空函数 内部 要放一个 pass
def func(self):
    # 对参数进行限定
    if not isinstance (self, (int ,float)):
        raise TypeError('傻逼，参数类型不对')
    pass
    print('我是函数内的内容哦',self)
    
func(1)

# 可以返回多个值？？？ 厉害了 老铁 
# 函数可以同时返回多个值，但其实就是一个tuple。 不可变数组
def more(a):
     # 多个值用逗号隔开
    return 1, 2

print(more('what'))
# 还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码

def func2(A=None):
    if A is None:
        A = []
    A.append('end')    
    return 

print(func2())
print(func2())