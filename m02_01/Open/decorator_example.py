class Greeting:
    def __init__(self, username):
        self.username = username

    def greet(self) -> str:
        return f'Hello {self.username}'


class GreetingDecorator:
    def __init__(self, wrapper: Greeting):
        self.wrapper = wrapper

    def greet(self) -> str:
        base_greet = self.wrapper.greet()
        return base_greet.upper()


message = GreetingDecorator(Greeting('Michail'))
print(message.greet())
# new_message = GreetingDecorator(message)
# print(new_message.greet())
