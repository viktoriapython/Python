condition = True
while condition:
    user_input = input('Please enter your ID ')
#print(int(user_input))

try:
    user_input = str(int(user_input))
    if len(user_input) != 11:
        raise UserWarning
    else:
        condition = False

except:
    print('ID code is too short or too long')


finally:
    print('Program finishes working')


