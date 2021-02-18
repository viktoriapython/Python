# fruits = ['apple', 'banana', 'melon', 'pear', 'watermelon']
# print(fruits)
#
# fruits.reverse()
# print(fruits)
########

##some_list = [1, 2, 5, 67, 8, 4, 3, 8, 9]
some_list = input('Please enter some numbers separated by coma: ').split(', ')
#print(some_list[::-1])
#some_list.reverse()
#print(sum)


for num in some_list[::-1]:
    print(num)

