# eval(expression, global, locals) -> result

def example():
    foo = 16
    loc = locals()
    print(f'Before: {loc}')
    baz = eval('foo + 10')
    print(f'After: {loc}')
    print(baz)


def example2():
    foo = 16
    baz = 10
    loc = locals()
    print(f'Before: {loc}')
    foo = eval('foo + 1')
    print(f'After: {loc}')
    locals()
    print(loc)
    print(f'foo={foo}')


def example3():
    foo = 16
    baz = 10
    loc = {'foo': 13, 'baz': baz}
    print(f'Before: {loc}')
    foo = eval('foo + 1', {}, loc)
    print(f'After: {loc}')
    print(f'foo={foo}')


if __name__ == '__main__':
    print('Example #1')
    example()
    print('Example #2')
    example2()
    print('Example #3')
    example3()