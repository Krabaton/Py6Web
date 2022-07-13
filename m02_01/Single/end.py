from abc import abstractmethod, ABC


class IPhoneNumber(ABC):

    @abstractmethod
    def value_of(self):
        ...


class IPerson(ABC):

    @abstractmethod
    def get_phone_number(self):
        ...


class PhoneNumber(IPhoneNumber):
    def __init__(self, phone: int, operator_code: str):
        self.phone = phone
        self.operator_code = operator_code

    def value_of(self):
        return f'+38({self.operator_code}){self.phone}'


class Person(IPerson):
    def __init__(self, name: str, phone: PhoneNumber) -> None:
        self.name = name
        self.phone = phone

    def get_phone_number(self) -> str:
        return f'{self.name}: {self.phone.value_of()}'


person = Person('Alex', PhoneNumber(9945512, '065'))
print(person.get_phone_number())
