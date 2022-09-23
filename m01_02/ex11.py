def type_of_property(name, required_type):
    __name = '__' + name

    @property
    def prop(self):
        return getattr(self, __name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, required_type):
            raise TypeError(f'{name} must be {required_type.__name__}')
        setattr(self, __name, value)

    return prop


class Person:
    name = type_of_property('name', str)
    age = type_of_property('age', int)

    def __init__(self, name, age):
        self.__name = None
        self.__age = None
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person({self.name}, {self.age})"


if __name__ == '__main__':
    person = Person('Krabat', 46)
    print(person)
    person.name = 'Yurii'
    try:
        person.age = 'Old fart'
    except TypeError as err:
        print(err)
    
