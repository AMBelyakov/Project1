class Base:
    def method(self):
        print('Hello!')


class Child:
    def child_method(self):
        print('Hello from child method!')

    def method(self):
        print('Hello from redefined method!')


obj = Child()
obj.method()
obj.child_method()


# 2
class Figure:
    def __init__(self, side=0.0):
        self.side = side


class Square(Figure):
    def draw(self):
        for i in range(self.side):
            print('*' * self.side)


class Triangle(Figure):
    def draw(self):
        for i in range(1, self.side + 1):
            print('*' * i)


def main():
    square = Square(5)
    square.draw()
    print()
    triangle = Triangle(8)
    triangle.draw()


if __name__ == '__main__':
    main()


# 3
class Horse:
    def run(self):
        print('I am running')


class Bird:
    def fly(self):
        print('I am flying')


class Pegasus(Horse, Bird):
    pass


def main():
    pegasus = Pegasus()
    pegasus.run()
    pegasus.fly()


if __name__ == '__main__':
    main()


# 4
class Base:
    def method(self):
        print('Method class:', __class__.__name__)
        print('Instance class:', type(self).__name__)


class Child(Base):
    pass


if __name__ == '__main__':
    base_instance = Base()
    base_instance.method()
    child_instance = Child()
    child_instance.method()


# 5
class A:
    def method(self):
        print('A method')


class B(A):
    pass


class C(A):
    def method(self):
        print('C method')


class D(B, C):
    pass


for cls in [A, B, C, D]:
    print(cls.__name__ + ':', cls.mro())
obj = D()
obj.method()
print(D.mro())


# 6
class MethodContainer:
    def __init__(self, data):
        self.data = data

    def method(self):
        print('Metod invoked')
        print('data=', self.data)


instance = MethodContainer(8)
print(type(MethodContainer.method))
print(type(instance.method))
print(MethodContainer.method(instance))
print(instance.method())


# 7
class Base:
    def method(self):
        print('Base method invoked on', type(self).__name__, 'instance')


class Child(Base):
    def method(self):
        super().method()  # Base.method(self)
        print('Child method invoked on', type(self).__name__, 'instance')


base_instance = Base()
base_instance.method()
child_instance = Child()
child_instance.method()
Base.method(child_instance)


# 8
class Animal:
    def __init__(self):
        self.can_run = False
        self.can_fly = False

    def print_abilities(self):
        print(type(self).__name__ + ':')
        print('Can run', self.can_run)
        print('Can fly', self.can_fly)
        print()


class Horse(Animal):
    def __init__(self):
        super().__init__()
        self.can_run = True


class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.can_fly = True


class Pegasus(Horse, Bird):
    pass


if __name__ == '__main__':
    horse = Horse()
    horse.print_abilities()

    bird = Bird()
    bird.print_abilities()

    pegasus = Pegasus()
    pegasus.print_abilities()


# 9
def check_instance(obj, cls):
    return check_subclass(type(obj), cls)


def check_subclass(child, base):
    if child == base:  # return base in child.mro()
        return True

    for direct_base in child.__bases__:
        if base == direct_base:
            return True
        return check_subclass(direct_base, base)

    return False


print(isinstance(8,int))
print(isinstance(8,object))
print(isinstance(8,str))

print(issubclass(bool,bool))
print(issubclass(bool,int))
print(issubclass(bool,object))
print(issubclass(bool,str))