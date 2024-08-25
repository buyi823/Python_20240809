magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!\n")

animals = ['dog', 'cat', 'tiger', 'mantis', 'swan']
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!\n")

# 数值类列表
for value in range(1, 5):
    print(value)
# 使用range()创建列表
numbers = list(range(1, 6))
print(numbers)
even_numbers = list(range(2, 11, 2))
odd_numbers = list(range(1, 11, 2))
print(even_numbers)
print(odd_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = []
for digit in range(0, 11):
    digits.append(digit)
print(digits)
print(f"The minium{min(digits)}")
print(max(digits))
print(sum(digits))
#列表解析
squares = [value ** 2 for value in range(1, 11)]
print(squares)

index_number = [number ** 3 for number in range(1, 11)]
print(index_number)

test_number = []
for i in range(1, 1000001):
    test_number.append(i)
print(max(test_number))
print(min(test_number))
print(sum(test_number))


odd_num = []
for odd in range(1, 21, 2):
    odd_num.append(odd)
print(odd_num)

odd_num = [odd for odd in range(1, 21, 2)]
print(odd_num)

# 使用列表输出能被3整除的数
numbers = list(range(3, 31, 3))
for number in numbers:
    print(number)
# 列表解析方式 list comprehension
numbers = [number for number in range(3, 31, 3)]
print(numbers)

# 生成列表的几种中方式
lists = list(range(1, 11))
print(lists)

lists = []
for i in range(11):
    lists.append(i)
print(lists)

lists = [list for list in range(11)]
print(lists)
# 切片
print(lists[0:3])
print(lists[1:4])
print(lists[0:4])
print(lists[2:])
print(lists[-3:])

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)




