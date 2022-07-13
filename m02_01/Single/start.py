class Person:
    def __init__(self, name: str, phone: int, operator_code: str):
        self.name = name
        self.phone = phone
        self.operator_code = operator_code

    def get_phone_number(self):
        return f'{self.name}: +38({self.operator_code}){self.phone}'


person = Person('Alex', 9945512, '065')
print(person.get_phone_number())
