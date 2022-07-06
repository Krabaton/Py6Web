print('Определение метакласса')


class OurMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        print(mcs, "__new__ metaclass called")
        print(kwargs)
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(mcs, "__prepare__ metaclass called")
        print(kwargs)
        return super().__prepare__(name, bases)

    def __call__(cls, *args, **kwargs):
        print(cls, "__call__ metaclass called")
        print(kwargs)
        return super().__call__(*args, **kwargs)


print('Определение класса')


class MyClass(metaclass=OurMeta, test='Alex'):
    def __new__(cls, *args, **kwargs):
        print(cls, "__new__ MyClass called")
        print(kwargs)
        return super().__new__(cls)

    def __init__(self, value):
        print(self, "__init__ called")
        super().__init__()
        self.value = value


if __name__ == '__main__':
    print('Создание экземпляра класса')
    instance = MyClass(10)