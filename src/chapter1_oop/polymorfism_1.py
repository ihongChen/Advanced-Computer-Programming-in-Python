# polymorfism_1.py

class Variable:
    def __init__(self, data):
        self.data = data

    def representative(self):
        pass

class Income(Variable):
    def representative(self):
        return sum(self.data) / len(self.data)

class City(Variable):
    # class variable
    _city_pop_size = {
        'Shanghai' : 24000,
        'San Paulo' : 21300,
        'Paris' : 10800,
        'London' : 860,
        'Tokyo' : 13500,
        'Moscow' : 12000
    }

    def representative(self):
        dictC = {
            City._city_pop_size[c]:c for c in self.data
            if c in City._city_pop_size.keys()
        }
        return dictC[max(dictC.keys())]

if __name__ == '__main__':
    income = Income([1,2,3,4,5,6,7,8,9])
    print(income.representative())
    city = City(['Shanghai','Tokyo','Moscow','NOT HERE'])
    print(city.representative())