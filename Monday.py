empty_list = []
empty_tuple = ()
empty_dict = {}

print(type(empty_dict))

empty_list = [1233, 12, 313, "Some string", True, None, ['One', 'Two', 3]]

print(empty_list)
empty_list[2] = [1233, True, 'another string']
print(empty_list)

list_element = [1233, True, 'another string']
empty_list = [1233, 12.313, 'Some string', True, list_element, ['One', 'Two', 3]]
print(empty_list[::2])

courses = ['History', 'Math', 'Literature', 'Physics', 'Programming']
numbers = [1, 5, 6, 7, 3, 76, 23, 34]
courses2 = ['Economics', 'Marketing', 'Math', 'Art', 'art']

list_1 = ['Math', 'History', 'Programming', 'Physics']
list_2 = list_1.copy()
print(list_1)
print(list_2)

list_1[2] = 'Sports'
list_2[0] = 'Art'

print(list_1)
print(list_2)










