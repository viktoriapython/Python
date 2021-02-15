id_code = input('Please enter your ID code')
# 1 2 3 4 5 6 7 8 9 1
# 3 4 5 6 7 8 9 1 2 3

chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

#control_number = 1 * int(id_code[0]) + 2 * int(id_code[1])\
                 #+ 3 * int(id_code[2]) + 4 * int(id_code[3]) + 5 * int(id_code[4]))) % 11

#id_code = '48507222217'
#control_number = 2
#if control_number == id_code[-1]:
    #print('OK')
#else:
    #print('NOK')

#id_code = input('Please enter your ID code')

id_code_list = list(id_code)

counter = 0
result = 0
for num in chk1:
    result = result + chk1[counter] * int(id_code_list[counter])
    counter += 1
check_num = result % 11

if check_num == int(id_code[-1]):
    print('ID code is valid')
elif check_num == 10:
    counter = 0
    result = 0
    for num in chk2:
        result = result + chk2[counter] * int(id_code_list[counter])
        counter += 1
    check_num = result % 11
    if check_num == int(id_code[-1]):
        print('ID code is valid')
    else:
        print('ID code is not valid')
else:
    print('Code is not valid!!!!!!!!')

def id_check(id_code, chk_list):
    counter = 0
    result = 0
    for num in chk_list:
        result += int(id_code[counter]) * num
        counter += 1
    return result % 11

id_code = list(input('Please enter your id: '))

chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]

if id_check(id_code, chk1) == 10:
    result = id_check(id_code, chk2)
    if result % 11 == int(id_code[10]):
        print('ID code is valid')
    else:
        print('iD code is invalid')
elif id_check(id_code, chk1) ==int(id_code[10]):
    print('ID code is valid')
print(id_check(id_code, chk1))

