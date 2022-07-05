# while_example
response = ""
while response != "exit":
    response = input("Type 'exit' to exit:")

n = 1
while n <= 3:
    print('n=', n)
    n += 1

number = 0
while number <= 0:
    number = int(input('Enter a positive integer:'))
print("You have entered:", number)

"""print('All natural numbers')
n=2
while True:
    print(n)
    n**=2"""

# break_example
while True:
    print('Enter "exit" to exit loop')
    response = input('>')
    if response == "exit":
        break
print('Loop has stopped')

name = None
while True:
    print('Menu:')
    print('1.Enter name')
    print('2.Print greeting')
    print('3.Quit')
    response = input('Please choose an action:')
    print()
    if response == '1':
        print('Enter your name')
    elif response == '2':
        if name:
            print('Hello,', name, '!', sep='')
        else:
            print('I don`t know your name')
    elif response == '3':
        break
    else:
        print('Incorrect input')
    print()

# continue_example
number = 0
while number < 10:
    number += 1
    if number == 5:
        continue
    print('Current number is', number)

# while_else
counter = 5
while counter:
    print(counter)
    counter -= 1
else:
    print('Loop is completed')
    print('counter=', counter)

# while_else_break
attempts_left = 3
while attempts_left > 0:
    attempts_left -= 1
    passowrd = input('Enter your password:'"you have {} attempts left".format(attempts_left + 1))
    if passowrd == '98eaxc':
        print('Access granted')
        break
    else:
        print('Access denied')

# for example
for i in range(10):
    print('i=', i)
# for_break
for i in range(10):
    print(i)
    if i == 8:
        break
# for_continue
for i in range(10):
    if i == 8:
        continue
    print(i)
# for_else
for attempts_left in range(3, 0, -1):
    while attempts_left > 0:
        attempts_left -= 1
        passowrd = input('Enter your password:'"you have {} attempts left".format(attempts_left))
        if passowrd == '98eaxc':
            print('Access granted')
            break
        else:
            print('Access denied')

# nested_loops
for row in range(5):
    for column in range(30):
        print('*', end='')
    print()
