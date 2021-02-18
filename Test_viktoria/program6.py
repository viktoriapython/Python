# list1 = [5, 6, 7, 8, 9, 1, 5, 7]
# list2 = [10, 11, 12, 13, 11, 12, 10]
#
# def Repeat(x):
#     size = len(x)
#     repeated = []
#     for i in range(size):
#         k = i + 1
#         for j in range(k, size):
#             if x[i] ==x[j] and x[i] not in repeated:
#                 repeated.append(x[i])
#     return repeated
#
# print(Repeat(list1))
# print(Repeat(list2))
################

test_list1 = [1, 2, 3, 4, 4, 5, 5, 5, 7, 8, 8, 8, 10, 10, 10]
max_count = 0
new_list = []

#print(test_list1.count(1))

for num in test_list1:
    if test_list1.count(num) > max_count:
        max_count = test_list1.count(num)
    print(max_count)

for num in test_list1:
    if test_list1.count(num) ==max_count:
        new_list.append(num)
new_list = list(set(new_list))

print(new_list)






