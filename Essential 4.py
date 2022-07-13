def my_for(iterable, callback):
    it = iter(iterable)
    while True:
        try:
            value = next(it)
            callback(value)
        except StopIteration:
            break


def loop_body(value):
    print('Next value received', value)


my_for(range(10), loop_body)

# 2
values = [5, 3, 1, 8]
for x in values:
    print(x)

for char in 'asdf':
    print(char)


# 3
class SimpleIterable:
    def __getitem__(self, index):
        if 0 <= index <= 5:
            return index * 2
        else:
            raise IndexError


iterable = SimpleIterable()
for value in iterable:
    print(value)

# 4
import math


class MyRange:
    def __init__(self, first, second=None, step=1):
        if second is None:
            self.start = 0
            self.end = first
        else:
            self.start = first
            self.end = second
        if step != 0:
            self.step = step
        else:
            raise ValueError('Step cannot be zero')

        self.length = math.ceil((self.end - self.start) / self.step)

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if 0 <= index < len(self):
            return self.start + index * self.step
        else:
            raise IndexError('MyRange index is out of range')

    def __repr__(self):
        return 'MyRange ({}, {}, {})'.format(self.start, self.end, self.step)

    def __iter__(self):
        current = self.start  # return RangeIterator(self)
        for _ in range(len(self)):
            yield current
            current += self.step


class RangeIterator:

    def __init__(self, range_instance):
        self.range = range_instance
        self.next_value = range_instance.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_value >= self.range.end and self.range.step > 0 or self.next_value <= self.range.end and self.range.step < 0:
            raise StopIteration

        result = self.next_value
        self.next_value += self.range.step

        return result


r = MyRange(10)
it = iter(r)
for it in range(10):
    print(it)
for it in range(3, 8, 2):
    print(it)
for it in range(10, 0, -1):
    print(it)


# 6
def generator():
    yield 'hello'
    yield 'world'


g = generator()
print(next(g))
print(next(g))


# 7
def fibonacci(count):
    first, second = 0, 1
    for _ in range(count):
        yield second
        first, second = second, first + second


count = int(input('How many Fibonaccy numbers to print?'))
for fib in fibonacci(count):
    print(fib)

# 8
generator = (x * y for x in range(5) for y in range(3) if (x + y) % 2 == 0)
for value in generator:
    print(value)
print()
print(sum(x ** 2 for x in range(10)))


# 9
def subgenerator():
    yield '[subgenerator] hello'
    yield '[subgenerator] world'


def generator():
    yield '[generator]    start'
    yield from subgenerator()
    yield '[generator]    end'


for value in generator():
    print(value)


# 5
class List:
    class _Node:  # элементы
        __slots__ = ('value', 'next')

        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    class _NodeIterator:
        def __init__(self, first):
            self._next_node = first

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration
            value = self._next_node.value
            self._next_node = self._next_node.next

            return value

    def __init__(self, iterable=None):
        self._head = None
        self._tail = None
        self._length = 0
        if iterable is not None:
            self.extend(iterable)

        def __len__(self):
            return self._length

        def append(self, value):
            node = List._Node(value)
            if len(self) == 0:
                self._head = self._tail = node
            else:
                self.tail.next += node
                self.tail = node

            self._length += 1

        def extend(self, iterable):
            for value in iterable:
                self.append(value)

        def __getitem__(self, index):
            if index < 0:
                index += len(self)

            if not 0 <= index < len(self):
                raise IndexError('list index out of range')

            node = self._head
            for _ in range(index):
                node = node.next

            return node.value

        def __iter__(self):
            node = self._head  # return List._NodeIterator(self._head)
            while node is not None:
                yield node.value
                node = node.next


if __name__ == '__main__':
    numbers = List(range(100000))
    for x in numbers:
        if x % 1000 == 0:
            print(x)
