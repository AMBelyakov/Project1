# 1
int_list = [1, 2, 3, 5]
char_list = ['a', 'c', 'z', 'x']
empty_list = []

print('Numbres:', int_list)
print('Chars:', char_list)
print('Empty_list:', empty_list)

list_from_range = list(range(5))
print('From range:', list_from_range)

list_from_string = list('a string')
print('From range:', list_from_string)

# 2
my_list = [5, 7, 9, 1, 1, 2]
print(my_list[0])
print(my_list[1])

index = int(input('Enter an index:'))
element = my_list[index]
print(element)

# negative_indices
my_list = [5, 7, 9, 1, 1, 2]
pre_last = my_list[-2]
print(pre_last)
result = my_list[0] + my_list[-1]
print(result)

# slicing
my_list = [5, 7, 9, 1, 1, 2]
sub_list = my_list[:3]
print(sub_list)
print(my_list[2:-2])
print(my_list[4:5])
sub_list = my_list[0:-1:2]
print(sub_list)
print(my_list[2:-2:2])
print(my_list[-1:0:-1])
print(my_list[::-1])
print(my_list[2::2])
print(my_list[:-2])
print(my_list[::-2])

# in_example
my_list = [5, 7, 9, 1, 1, 2]
value = int(input('Enter a number:'))
if value in my_list:
    print('This number is in list')
else:
    print('This number is not in list')

# len_example
my_list = [5, 7, 9, 1, 1, 2, 123]
print('Number of elements:', len(my_list))
my_list = []
print('Number of elements:', len(my_list))

# string_indexing
string = 'a string'
print(string[0])
print(string[2])
print(string[-1])

print(string[2:5])
print(string[:5])
print(string[2:])
print(string[::2])
print(string[::-1])

print(string[2] + string[-3:])

# in_str
string = input('Enter a string')
if 'q' in string:
    print('There is a "q" in the string')
else:
    print('There is not a "q" in the string')

print('ing' in 'si ng')

# str_len
string = input('Enter a string:')
print(len(string))

# append
my_list.append(3)
my_list.append(5)
my_list = [my_list[0] + my_list[1]]

print(my_list)

# del
my_list = [5, 1, 5, 7, 8, 1, 0, -23]

print(my_list)

del my_list[2]
print(my_list)

# mutation
my_list = [5, 1, 5, 7, 8, 1, 0, -23]

print(my_list)

my_list[3] = 18

print(my_list)

# traversal
my_list = [5, 1, 5, 7, 8, 1, 0, -23]
for x in my_list:
    print('{}^2={}'.format(x, x ** 2))

# fibonacci
n = 10
fibs = [1, 1]
for i in range(n - 2):
    fibs.append(fibs[i] + fibs[i + 1])
print(fibs)
