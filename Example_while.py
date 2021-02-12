while True:
    user_input = input('Please enter id: ')
    if len(user_input) != 11:
       print('Please try again')
       continue
    else:
       print(user_input)
       break

