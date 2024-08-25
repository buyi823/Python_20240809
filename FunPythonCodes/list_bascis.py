bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(bicycles[1].title())
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)
traffic = ['car', 'bike', 'motorcycle', 'supercar']

for i in traffic:
    dreams = f"I would like to won a {i}"
    print(dreams)

# list operation
bicycles[0] = 'ducati'  #修改列表元素
print(bicycles)
bicycles.append('yamaha')
print(bicycles)
motorcycles = []  # 建立一个空列表，使用append函数添加
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0, 'ducati')  # insert element
print(motorcycles)
del motorcycles[0]  # del：适用于删除列表中的特定元素、切片或整个列表，不返回删除的元素。
print(motorcycles)

popped_motorcycle = motorcycles.pop() # pop()：适用于删除并返回列表中的特定元素，通常用于需要获取并删除元素的情况。
# 简单判断，如果不在使用某个元素了，直接del，如果删除后还想继续使用，可以使用pop()
print(motorcycles)
print(f"The last motorcycle I owned was a {popped_motorcycle.title()}")
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")
print(motorcycles)
remove_element = motorcycles.remove('yamaha')
print(motorcycles)
print(remove_element)

famous_man = ['Michale', 'Bryant', 'James', 'Washington']
print(famous_man)
for i in famous_man:
    print(f"I would like to have dinner with {i}")
famous_man.insert(3, 'Lincon')
famous_man.insert(4, 'Bush')
print(famous_man)
famous_man.append('Blaine')
print(famous_man)
while len(famous_man) > 2:   # 删除列表中的元素,列表中剩余两个元素
    print(f"Sorry, we have no seats, {famous_man.pop()}")
print(famous_man)
del famous_man[0:]
print(famous_man)

# 列表排序  sort()  reverse()永久性排序
print("列表排序  sort()  reverse()永久性排序")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.sort()
print(cars)
cars.reverse() # 只是反转列表元素的顺序
print(cars)
cars.sort(reverse=False)
cars.sort(reverse=True)
print(cars)

#  临时排序
print("临时排序")
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is  the original list again:")
print(cars)
print(len(cars))

# practice
print("Here are the places I want to go:")
places = ['LosAngeles', 'San Francisco', 'Seattle', 'las Vegas', 'Houston', 'Chicago', 'New York', 'Washington', 'Philadelphia']
print(places)
print(f"Sort them alphabetically:\n{sorted(places)}")
print(f"original list:\n{places}")
places.reverse()
print(places)
places.reverse()
print(places)
print(len(places))

