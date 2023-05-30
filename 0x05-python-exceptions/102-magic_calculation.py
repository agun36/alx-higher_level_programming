#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
<<<<<<< HEAD
            result += (a ** b) / i
        except:
            result = b + a
            break
=======

            result += a ** b / i

        except Exception:
            result = b + a
            break

>>>>>>> 35fc098d76bd43a019855f6e5c4c744b7858b434
    return result
