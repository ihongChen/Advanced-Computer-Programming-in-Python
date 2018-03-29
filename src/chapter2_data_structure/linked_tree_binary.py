# Linked Structure based Binary Tree


class Node:

    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return 'parent:{}, value:{}'.format(self.parent, self.value)


class BinaryTree:

    def __init__(self, root_node=None):
        self.root_node = root_node

    def add_node(self, value):
        if self.root_node is None:  # root
            self.root_node = Node(value)
        else:  # not root
            temp = self.root_node
            added = False
            while not added:
                if value <= temp.value:  # 值比節點小 -> 往左
                    if temp.left_child is None:  # 若沒有左支,成為左節點
                        temp.left_child = Node(value, temp.value)
                        added = True
                    else:  # 若有左支,往下一層找
                        temp = temp.left_child

                else:
                    if temp.right_child is None:
                        temp.right_child = Node(value, temp.value)
                        added = True
                    else:
                        temp = temp.right_child

    def __repr__(self):
        def traverse_tree(node, side='root'):
            ret = ''

            if node is not None:
                ret += '{} -> {}\n'.format(node, side)
                ret += traverse_tree(node.left_child, 'left')
                ret += traverse_tree(node.right_child, 'right')
            return ret
        return traverse_tree(self.root_node)


if __name__ == '__main__':

    tree = BinaryTree()
    tree.add_node(3)
    tree.add_node(4)
    tree.add_node(10)
    tree.add_node(2)
    print(tree)