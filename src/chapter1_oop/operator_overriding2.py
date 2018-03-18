## operator overriding

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __lt__(self, other_point):
        self_mag = (self.x ** 2) + (self.y **2)
        other_mag = (other_point.x ** 2) + (other_point.y **2)
        return self_mag < other_mag
    
if __name__ == '__main__':
    p1 = Point(2,4)
    p2 = Point(3,7)
    print(p1>p2)