from functools import wraps


def decorator_one(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Decorator #1')
        return result
    return wrapper


def decorator_two(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'Decorator #2')
        return result
    return wrapper


@decorator_one
@decorator_two
def prefix_name(name):
    return f'Mr.(s) {name}'


print(prefix_name('Alex'))
print(prefix_name.__wrapped__('Sasha'))
print(prefix_name.__wrapped__.__wrapped__('Kirill'))
