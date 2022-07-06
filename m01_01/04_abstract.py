from abc import ABCMeta, abstractmethod


class Baz(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self):
        pass

    @staticmethod
    @abstractmethod
    def method():
        pass


class Bar(Baz):
    @property
    def name(self):
        pass

    @name.setter
    def name(self):
        pass

    @staticmethod
    def method():
        pass

bar = Bar()
