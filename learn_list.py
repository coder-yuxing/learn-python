# 列表(list) 是Python 中的一个对象
# 列表中可以保存多个有序的数据

# 列表的使用
# 1. 列表的创建
# 通过 [] 创建列表
my_list = [] # 创建一个空列表
print(my_list, type(my_list))

# 列表中存储的数据，称之为元素
# 一个列表中可以存储多个元素，也可以在创建列表时就指定列表中的元素
my_list = [10, 20, 30]
print(my_list)

# 列表中可以保存任意的对象
my_list = [10, "hello", True, 1.23]
print(my_list)

# 列表中存储的元素是有序的，列表中每个元素都有一个索引
# 索引是从0开始的整数
# 可以通过索引来获取对应位置上的索引
my_list = [10, 20, 30, 40]
print(my_list[0])
print(my_list[1])
print(my_list[-1])
print(my_list[-2])
# 索引超出最大范围时会抛出异常
# print(my_list[5]) # IndexError: list index out of range

# 通过 len() 函数可以获取列表的长度
print(len(my_list))



# 切片
# 切片是指从现有的列表中获取一个子列表的操作
# 语法：列表[起始:结束]
#   通过切片获取元素时，会包括指定的起始位置元素，但不包括结束位置的元素
#   做切片操作时，总会返回一个新的列表，不会影响原有的列表
#   起始和结束位置的索引都可以省略不写
#   若省略起始位置，则会从第一个元素开始截取
#   若省略结束位置，则会从起始位置一直截取到最后
students = ['xiaoming', 'xiaohong', 'yuxing', 'damocles', 'zhangsan']
newStu = students[1:3]
print(newStu) # ['xiaohong', 'yuxing']

print(students[1:]) # ['xiaohong', 'yuxing', 'damocles', 'zhangsan']
print(students[:4]) # ['xiaoming', 'xiaohong', 'yuxing', 'damocles']
print(students[:]) # ['xiaoming', 'xiaohong', 'yuxing', 'damocles', 'zhangsan']
print(students[-1:]) # ['zhangsan']

# 切边支持指定截取时的步长
# 语法：[起始:结束:步长]， 默认步长为1
print(students[1:4:1]) # ['xiaohong', 'yuxing', 'damocles']
print(students[1:4:2]) # ['xiaohong', 'damocles']
# 若步长为负数时，会从后往前截取
print(students[::-1]) # ['zhangsan', 'damocles', 'yuxing', 'xiaohong', 'xiaoming']


# 常用操作
# + 和 *
my_list = [1,2,3]
my_list_2 = [4,5,6]
# + 操作可以将连个列表拼接为一个列表
my_list_3 = my_list + my_list_2
print(my_list_3) # [1, 2, 3, 4, 5, 6]

# * 操作可以将一个列表重复n次变为一个新的列表
my_list_4 = my_list * 2
print(my_list_4) # [1, 2, 3, 1, 2, 3]

# in 和 not in
# in 用于判断一个元素是否存在于列表中
print(2 in my_list) # True
# not in 用于判断一个元素是否不存在与列表中
print(10 not in my_list) # True

# len() 函数用于获取列表的元素个数
print(len(my_list)) # 3

# min() 函数用于获取一个列表中的最小值
print(min(my_list)) # 1

# max() 函数用于获取一个列表中的最大值
print(max(my_list)) # 3

# 两个方法：index() 和 count()
# 方法与函数的区别: 方法是属于某一个对象的，只能通过对象调用
# index()方法用于获取指定元素在列表中的索引位置
print(my_list.index(3)) # 2

# count() 方法用于统计指定元素在列表中的个数
print(my_list.count(1)) # 1


# 通过索引修改列表中的值
my_list = [1,2,3]
my_list[1] = 10
print(my_list) # [1, 10, 3]

# del 删除元素
del my_list[1]
print(my_list) # [1, 3]

# 通过切片修改元素
my_list[0:2] = [10, 11]
print(my_list) # [10, 11]


my_list[0:0] = [12] # 该操作相当于向列表头部插入元素
print(my_list) # [12, 10, 11]


# 当设置步长时，复制的元素必须与切片中元素个数一致
my_list[::2] = [1,2 ]
print(my_list)

# 列表中的方法
# append() 向列表的最后追加一个元素
my_list = [1,2,3]
my_list.append(4)
print(my_list) # [1, 2, 3, 4]

# insert() 向列表的指定位置插入一个元素
my_list.insert(2, 6)
print(my_list) # [1, 2, 6, 3, 4]

# extend() 扩展列表，需要一个序列作为参数，将入参序列添加到当前列表中
my_list_2 = [4,5,6]
my_list.extend(my_list_2)
print(my_list) # [1, 2, 6, 3, 4, 4, 5, 6]

# clear() 用于清空列表
my_list.clear()
print(my_list) # [1, 2, 6, 3, 4, 4, 5, 6]

# pop() 根据指定索引删除元素, 并返回删除的元素
# 当入参为空时，删除列表末尾元素
my_list = [1,2,3]
print(my_list.pop(2)) # 3
print(my_list.pop()) # 2

# remove() 删除指定的元素, 若要删除的元素在列表中存在多个时，会删除第一个
my_list = ['hah', 'xiangming']
my_list.remove('hah')
print(my_list) # ['xiangming'] 

# reverse() 用于反转列表
my_list = [1,2,3]
my_list.reverse()
print(my_list) # [3, 2, 1]

# sort() 对列表进行排序
my_list = list('aravvzdgdsfknjcjnewrwe')
print(my_list) # ['a', 'r', 'a', 'v', 'v', 'z', 'd', 'g', 'd', 's', 'f', 'k', 'n', 'j', 'c', 'j', 'n', 'e', 'w', 'r', 'w', 'e']
my_list.sort() # 默认正序排列
print(my_list) # ['a', 'a', 'c', 'd', 'd', 'e', 'e', 'f', 'g', 'j', 'j', 'k', 'n', 'n', 'r', 'r', 's', 'v', 'v', 'w', 'w', 'z']
my_list.sort(reverse=True)
print(my_list) # ['z', 'w', 'w', 'v', 'v', 's', 'r', 'r', 'n', 'n', 'k', 'j', 'j', 'g', 'f', 'e', 'e', 'd', 'd', 'c', 'a', 'a']


# 列表循环
# while 循环
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    
# for 循环
# 语法：for 遍历 in 序列:
#          代码块
for i in my_list:
    print(i)
