## abstract 

class Base:
    def func_1(self):
        raise NotImplementedError

    def func_2(self):
        raise NotImplementedError

class SubClass(Base):
    def func_1(self):
        print('func_1() called')
    
if __name__ == '__main__':
    b1 = Base()
    b2 = SubClass()
    b2.func_1()
    b2.func_2()

    