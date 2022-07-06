class MyClass:
    def __init__(self, value):
        self.value = value

    def method(self):
        return self.value


m = MyClass(10)
print(m.method())


def method(self):
    return self.value


def init(self, value):
    print('Run init method')
    self.value = value


NewMyClass = type('NewMyClass', (object, ), {'method': method, '__init__': init})

m = NewMyClass(12)
print(m.method())
