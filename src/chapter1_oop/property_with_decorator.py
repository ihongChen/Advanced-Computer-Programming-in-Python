# property with decorator

class Color:

    def __init__(self, rgb_code, name):
        self._rgb_code = rgb_code
        self._name = name
    
    ## create the property using the name of the attribute.
    ## Then we define how to set/get/delete it
    @property
    def name(self):
        print('Function to get the name color')
        return self._name
    
    @name.setter
    def name(self,new_name):
        print('Function to set the name as {}'.format(new_name))
        self._name = new_name
    
    @name.deleter
    def name(self):
        print('Erase the name')
        del self._name

if __name__ == '__main__':
    c1 = Color(rgb_code='111',name='red')
    print(c1.name)
    c1.name = 'blue'
    print(c1.name)
    del c1.name
