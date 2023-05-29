#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result += (a ** b) / i
       except Exception as e:
            if str(e) == 'Too far':
                result = b + a
            else:
                result = 0
            break
    return result
