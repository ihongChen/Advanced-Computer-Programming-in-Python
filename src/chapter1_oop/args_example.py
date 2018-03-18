## args examples.py
def method(arg1, arg2, arg3):
    print('arg1: {}'.format(arg1))
    print('arg2: {}'.format(arg2))
    print('arg3: {}'.format(arg3))

def method2(f_arg, *argv):
    print('first and normal:{}'.format(f_arg))
    for arg in argv:
        print('the next arg is : {}'.format(arg))

if __name__ == '__main__':
    kwargs = {'arg1':1,'arg2':'two','arg3':'three'}
    method2('Lorem','ipsum','ad','his','scripts')
    method(**kwargs)