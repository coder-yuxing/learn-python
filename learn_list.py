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