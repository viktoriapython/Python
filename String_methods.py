a = 'Hello'
b = 'World'

print(a + b)
print(a + '' + b)

print('First word is', a)
print('First word is ' + a + '.')

salary = 1000
string = 'Johns salary is {}'
print(string.format(salary))

apples = 3
bananas = 5
pears = 2
fruit_string = "John has {} bananas, {} apples and {} pears"
print(fruit_string.format(apples, bananas, pears))

fruit_string2 = "John has {1} bananas, {0} apples and {2} pears"
print(fruit_string2.format(apples, bananas, pears))

price_string = "This {product:} costs {price:.2f} euros"
print(price_string.format(price=350, product="computer"))


x = 12231.3456789
y = 131.1314
print('The value of x is %.4f' % x)
print('The value of y is %.2f' %y)

emp_name = 'John'
emp_age = 30
emp_salary = 1500

emp_string = 'Hi, my name is %(name)s! I am %(age)s old. My salary is %(salary).2f' % {'name': emp_name, 'salary': emp_salary, 'age': emp_age}
print(emp_string)

emp_string2 = f'Hi, my name is {emp_name}! I am {emp_age} old. My salary is {emp_salary:.2f}'
print(emp_string2)

byte_string = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
print(byte_string.decode('utf-16'))