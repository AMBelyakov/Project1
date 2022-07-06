def print_numbers(limit):
    for i in range(limit):
        print(i)


n = int(input('n='))
print_numbers(n)


def increase_number(number):
    print('Number was', number)
    number += 1
    print('Number became', number)


x = 8
increase_number(x)
print(x)

my_list = [1, 2]


def add_to_list(some_list):
    some_list.append(8)


add_to_list(my_list)
print(my_list)


# example1
def hello():
    print('Hello,World!')
    print("(this text was printed from a function)")
    print()


hello()
hello()


# example2
def print_numbers(limit):
    for i in range(limit):
        print(i)


def main():
    print_numbers(3)
    print()
    print_numbers(5)


if __name__ == "__main__":
    main()


# example3
def add_numbers(first, second):
    print('Add numbers called with', first, second)
    return first + second


result = add_numbers(2, 3)
print(result)
result = add_numbers(2, add_numbers(5, 7))
print(result)
result = add_numbers(2, 3) - add_numbers(1, 2)
print(result)


# example4
def function(x):
    if x < 0:
        return x * 2
    else:
        return x * 3


def main():
    for i in range(-3, 4):
        y = function(i)
        print('function', '(', i, ')=', y, sep='')


main()


# example5
def print_info(object='unknown object', color='black', price=0):
    print('Object:', object, sep='\t')
    print('Color:', color, sep='\t')
    print('price:', price, sep='\t')
    print()


print_info('pen', 'red', 1)
print_info(object='pen', color='red', price=1)
print_info(color='orange', object='cup', price=5)
print_info('coffee', price=10, color='black')

# example6
print_info(color='red')
