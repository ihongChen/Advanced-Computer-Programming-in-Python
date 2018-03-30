# encoding :utf8


def kwtest(*args, **kwargs):
    print('args:', args)  # tuple
    print('kwargs:', kwargs)  # dict
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key)


if __name__ == '__main__':
    kwtest('a', 'b', 'c', name='jack', city='TPE', school='NTU')
