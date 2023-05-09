def uppercase(s):
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            print(chr(ord(c) - 32), end='')
        else:
            print(c, end='')
    print()

