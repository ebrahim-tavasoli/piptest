#!/usr/bin/python
# -*- coding: utf-8 -*-

print('py' 'thon')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']
letters[2:5] = []

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3

str()
repr()

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
     print(f'{name:10} ==> {phone:10d}')

#Other modifiers can be used to convert the value before it is formatted. '!a' applies ascii(), '!s' applies str(), and '!r' applies repr()

print(f'My hovercraft is full of {animals!r}.')


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

# these are equal      

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

str.rjust()
str.ljust()
str.zfill()
str.center()

try_except = '''
If an exception occurs during execution of the try clause, the exception may be handled by an except clause. If the exception is not handled by an except clause, the exception is re-raised after the finally clause has been executed.

An exception could occur during execution of an except or else clause. Again, the exception is re-raised after the finally clause has been executed.

If the try statement reaches a break, continue or return statement, the finally clause will execute just prior to the break, continue or return statement’s execution.

If a finally clause includes a return statement, the finally clause’s return statement will execute before, and instead of, the return statement in a try clause.
'''

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
	else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)
#result is 2.0
#executing finally clause
divide(2, 0)
#division by zero!
#executing finally clause
divide("2", "1")
#executing finally clause
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "<stdin>", line 3, in divide
#TypeError: unsupported operand type(s) for /: 'str' and 'str'

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


