# property wo decorator
class Color:

    def __init__(self, rgb_code, name):
        self.rgb_code = rgb_code
        self._name = name
    
    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    name = property(get_name,set_name)

if __name__ == '__main__':
    c1 = Color('123','red')
    print(c1.name)    
    c1.name = 'blue'
    print(c1.name)