def add_everything_up(a, b):
    try:
        return format(a + b, '.3f')
    except:
        return f'{a}' + f'{b}'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))