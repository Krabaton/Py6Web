from functools import partial


def type_of_property(name, required_type, reg=None):
    __name = '__' + name

    @property
    def prop(self):
        return getattr(self, __name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, required_type):
            raise TypeError(f'{name} must be {required_type.__name__}')
        # if reg = True ...
        setattr(self, __name, value)

    return prop


String = partial(type_of_property, required_type=str)
Integer = partial(type_of_property, required_type=int)
Boolean = partial(type_of_property, required_type=bool)


class Person:
    name = String('name')
    age = Integer('age')
    favorite = Boolean('favorite')

    def __init__(self, name, age, favorite):
        self.__name = None
        self.__age = None
        self.__favorite = None
        self.name = name
        self.age = age
        self.favorite = favorite


if __name__ == '__main__':
    person = Person('Krabat', 46, True)
    person.name = 'Yurii'
    try:
        person.age = 'Old fart'
    except TypeError as err:
        print(err)
    
    print(person.name, person.age, person.favorite)
