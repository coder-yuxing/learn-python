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



