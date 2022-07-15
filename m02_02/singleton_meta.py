class MetaSingleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


class Singleton(metaclass=MetaSingleton):
    pass


class InheritSingleton(Singleton):
    pass


# isg = InheritSingleton()
sg = Singleton()
isg = InheritSingleton()
print(sg == isg)
