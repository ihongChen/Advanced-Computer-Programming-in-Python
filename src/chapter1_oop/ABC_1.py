## abc
from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    
    @abstractmethod
    def func_1(self):
        pass
    
    @abstractmethod
    def func_2(self):
        pass


class SubClass(Base):
    def func_1(self):
        pass
    def func_2(self):
        pass

    ## we intentionally forget implement func_2 

print('Is it subclass?',issubclass(SubClass, Base))
print('Is it instance?', isinstance(SubClass(), Base)) 
# a = Base() ## Can't instantiate abstarct class 

