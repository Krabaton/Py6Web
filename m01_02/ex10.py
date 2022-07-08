class Person:
    def __init__(self, name, age):
        self.__name = None
        self.__age = None
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be string')
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('age must be int')
        self.__age = value


if __name__ == '__main__':
    person = Person('Krabat', 46)
    person.name = 'Yurii'
    try:
        person.age = 'Old fart'
    except TypeError as err:
        print(err)
    
