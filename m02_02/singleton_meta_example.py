from dataclasses import dataclass


class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]


# class Setting(metaclass=Singleton):
#     def __init__(self):
#         self.db = 'MySQL'
#         self.port = 3306

@dataclass
class Setting(metaclass=Singleton):
    db: str = 'MySQL'
    port: int = 3306


m1_connect = Setting()
m2_connect = Setting()

print(m1_connect is m2_connect)
print(m1_connect.db, m1_connect.port)
m1_connect.db = 'Postgres'
print(m2_connect.db, m2_connect.port)
print(m1_connect, m2_connect)
