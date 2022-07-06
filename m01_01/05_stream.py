from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, max_buffer=10):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, max_buffer=10):
        print('read from socket')

    def write(self, data):
        print('write to socket')


class FileStream(IStream):
    def read(self, max_buffer=10):
        print('read from file')

    def write(self, data):
        print('write to file')


def serialize(stream):
    if not isinstance(stream, IStream):
        raise TypeError('Is not IStream!')
    print('Is true!')


f = FileStream()
s = SocketStream()

serialize(f)
serialize(s)
serialize(str)