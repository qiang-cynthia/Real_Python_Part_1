# -*- coding: utf-8 -*-

def square(number):
    result = number ** 2
    return result

input_number = float(input('Enter a number: '))
output = square(input_number)
print('The output is {}.'.format(output))
