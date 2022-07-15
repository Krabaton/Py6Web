class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance


class InheritSingleton(Singleton):
    pass


# isg = InheritSingleton()
sg = Singleton()
isg = InheritSingleton()
print(sg, isg)
