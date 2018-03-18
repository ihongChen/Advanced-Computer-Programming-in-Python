class Apartment:
    '''
    Class that represent an apartment for sale \n
    value is in USD
    '''

    def __init__(self, _id, mts2, value):
        self._id = _id
        self.mts2 = mts2
        self.value = value
        self.sold = False

    def sell(self):
        if not self.sold:
            self.sold = True
        else:
            print('Apartment {} was sold'
                  .format(self._id))

if __name__ == '__main__':
    house = Apartment(_id=121, mts2=100, value=5000)
    print('sold?', house.sold)
    house.sell()
    print('sold?', house.sold)
    house.sell()
