def function():
    """
    Exmple function
    Some long definition.
    """
    print('function called')


function()
help(function)
print(function.__doc__)

# radix-change
number = int(input('Enter a number:'))
print('Binary:      ', bin(number))
print('Octal:       ', oct(number))
print('Hexademical: ', hex(number))

# reversed_exapmle
for i in reversed(range(5)):
    print(i)
for i in reversed("asdf"):
    print(i)

# min_max
a = float(input('A='))
b = float(input('B='))
c = float(input('C='))
print('Min:', min(a, b, c))
print('Max:', max(a, b, c))


# nested_functions
def outer_function():
    def inner_function():
        print('Inner function')

    print('Outer function')
    inner_function()


outer_function()


# scoping_exmple1
def function():
    global var
    var = 'new variable'
    # var='local variable'
    print(var)


var = 'global variable'
function()
print(var)


# scoping_exmple2
def outer_function():
    var = 8

    def inner_function():
        nonlocal var  # global var
        print(var)
        var = 10

    print(var)
    inner_function()
    print(var)


var = 0
print(var)
outer_function()
print(var)


# factorial
# non_recursiv
def non_recursiv_factorial(n):
    result = 1
    for multiplier in range(2, n + 1):
        result *= multiplier


print(non_recursiv_factorial(10))


# recursiv
def recursiv_factorail(n):
    if n == 0:
        return 1
    else:
       return n * recursiv_factorail(n - 1)


print(recursiv_factorail(5))

# fibonacci
import functools


@functools.lru_cache(maxsize=None)
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(1, 11):
    print(fib(i))


def hanoi(n, a, b, c):
    if n != 0:
        hanoi(n - 1, a, c, b)
        print('Transfer ring from', a, 'to', c)
        hanoi(n - 1, b, a, c)
hanoi(3, 'A', 'B', 'C')
