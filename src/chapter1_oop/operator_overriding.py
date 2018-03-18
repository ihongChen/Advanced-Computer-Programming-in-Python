## operator overriding

class ShoppingCart:

    def __init__(self, product_list):
        self.product_list = product_list ## python dictionary

    def __call__(self, product_list=None):
        if product_list is None:
            product_list = self.product_list
        self.product_list = product_list

    def __add__(self, other_cart):
        added_list = self.product_list
        for p in other_cart.product_list.keys():
            if p in self.product_list.keys():
                value = other_cart.product_list[p] + self.product_list[p]
                added_list.update({p:value})
            else:
                added_list.update({p: other_cart.product_list[p]})
        return ShoppingCart(added_list)
    
    def __repr__(self):
        return '\n'.join('Product:{} | Quantity:{}'.format(
            p, self.product_list[p]) for p in self.product_list.keys()
        )

if __name__ == '__main__':
    s_cart1 = ShoppingCart({'muffin':3, 'milk':2, 'water':6})
    s_cart2 = ShoppingCart({'milk':3, 'soda':2, 'beer':12})
    s_cart3 = s_cart1 + s_cart2
    print(s_cart3.product_list)
    print(s_cart3)