# python将不能修改的值称为不可变的,而不可变的列表被成为元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print(dimensions)
# 如果元组只有一个元素,必须加上逗号
my_t = (3,)
print(my_t)
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

foods = ('noddle', 'dumpling', 'sandwich', 'fried chicken', 'pizza', 'hamburger')
for food in foods:
    print(food)

