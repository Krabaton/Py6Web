from debounce import debouncer


def test():
    print('Test run')


deb = debouncer(test, 1000)

while True:
    deb()
