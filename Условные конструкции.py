# simple_if_example
number = int(input('Enter a number:'))
if number > 5:
    print('This number is greater than five.')

if number is not None:
    pass

# if-else
x = float(input('x='))
if x > 0:
    y = x ** 0.5
else:
    y = x ** 2
print(y)

name = input()
if name == "Artem":
    print('You have entered', name)
    print('This is my name , too')
else:
    print('Your name differs from mine')

# nested_if
x = float(input())
if 0 < x < 7:
    print('Value is in range,let`s continue')
    y = 2 * x - 5
    if y < 0:
        print('y is negative')
    elif y > 0:
        print('y is positive')
    else:
        print('y=0')

# elif_switch
print("""Menu:
1.File
2.View
3.Exit
""")


choise = input('Enter your choise:')
if choise == '1':
    print('You have selected File menu')
elif choise == '2':
    print('You have selected View menu')
elif choise == '3':
    print('Stopping')
else:
    print('Incorrect choise')

# condition
is_ready = True
if is_ready:
    state_msg = 'Ready'
else:
    state_msg = 'Not ready yet'
print(state_msg)

# state_msg=is_ready and 'Ready' or 'Not ready yet'
# state_msg='Ready' if is_ready else 'Not ready yet'
# print('Ready' if is_ready else 'Not ready yet')

# truth_value_testing
string = input('Enter a string:')
if string:
    print('The string is "{}"'.format(string))

number = int(input('Enter an integer:'))
if number:
    print('The number is not zero')
else:
    print('The number is zero')

if string:  # if string is not None or string!='':
    pass
