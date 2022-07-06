class CountingClass:
    instance_created = 0

    def __new__(cls, *args, **kwargs):
        print(cls, "__new__ CountingClass called")
        instance = super().__new__(cls)
        instance.number = cls.instance_created
        cls.instance_created = cls.instance_created + 1
        return instance if instance.number != 1 else None

    def __init__(self, value):
        print(f'__init_() called with {value}')
        self.value = value


if __name__ == '__main__':
    print(f'Start: {CountingClass.instance_created}')

    for i in range(3):
        print(CountingClass(i))


    print(f'End: {CountingClass.instance_created}')
