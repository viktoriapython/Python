# from math import sqrt
# a = 3
# b = 4
# print('Input length of shorter triangle sides:', a, b )
#
# c = ('The length of the hypotenuse')
#
#
# c = sqrt(a**2 + b**2)
#
# print('The length of the hypotenuse is', c)
#
# side_a, side_b = input('Please enter two triangle sides separated by coma: ').split(',')
# print()

######
side_a, side_b = input('Please enter two triangle sides separated by coma: ').split(', ')

print(((int(side_a) ** 2) + (int(side_b) ** 2)) ** 0.5)