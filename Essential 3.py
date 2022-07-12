#raise ValueError('supplied value is invalid')

#2
print('Calculator')

try:
    a = float(input('a='))
    b = float(input('b='))
    print(a/b)
except (ZeroDivisionError,ValueError) as error:
    print(error)
#except Exception as error:
 #    print(type(error))
print('Stopping the calculator')

#3
def main():
    while True:
        try:
            first_number = float(input('First number='))
            second_number = float(input('Second number='))
            print('Result:',first_number/second_number)
            break
        except (ZeroDivisionError,ValueError) as error:
            print('Error:',error)
            print('Please try again')

if __name__=='__main__':
    main()

#4
try:
    3/0
except:
    pass
print('Programm flows futher')

#5
class ObjectWithDestructor:
    def __del__(self):
        print('destruction invoked')
        raise Exception
print('Creating object...')
obj=ObjectWithDestructor()

print('Deleting object')
del obj

print('Done')

#6

def do_stuff():
    try:
        raise ZeroDivisionError
    except ZeroDivisionError:
        print('division by zero')

try:
    do_stuff()
except ValueError:
    print('Value error')

#7
def main():
    try:
        raise ValueError('value is incorrect')
    except ValueError as error:
        print('Exception:',error)
        raise
try:
    main()
except ValueError:
    print('ValueError detected')

#8
#a=5
#b=0
#try:
#    result=a/b
#except ZeroDivisionError as error:
#    raise ValueError('variable b is incorrect') from None

#9
MAX_STARS=30
WIDTH=80
def print_result(number):
    if number==0:
        stars_count=MAX_STARS
    else:
        stars_count=round(MAX_STARS/number)
        if stars_count>MAX_STARS:
            stars_count=MAX_STARS
    number_field_width=WIDTH-2*stars_count
    stars='*'* stars_count
    fmt='{0}{1:^'+ str(number_field_width)+'}{0}'
    print(fmt.format(stars,number))
def main():
    while True:
        try:
            first_number = float(input('First number='))
            second_number = float(input('Second number='))
            result=first_number/second_number
        except (ZeroDivisionError,ValueError) as error:
            print('Error:',error)
            print('Please try again')
        else:
            print_result(result)
            break

if __name__=='__main__':
    main()

#10
def fn():
    try:
        return
    finally:
        print('Finally block')

fn()

#11
import warnings
name=input('Enter your first and last name:')

if name.count(' ')!=1:
    warnings.warn('Name format may be incorrest')
print('Hello, ',name,'!',sep='')