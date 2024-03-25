"""313"""
class BSTNode:
    """bst node"""
    def __init__(self):
        """init"""
        self.data = None
        self.left = None
        self.right = None
    def get_data(self):
        """get data"""
        return self.data
    def set_data(self, data):
        """set data"""
        self.data = data
    def get_left(self):
        """get left"""
        return self.left
    def set_left(self, left):
        """set left"""
        self.left = left
    def get_right(self):
        """get right"""
        return self.right
    def set_right(self, right):
        """set right"""
        self.right = right

class BST:
    """bst"""
    def __init__(self):
        """init"""
        self.root = None
    def get_root(self):
        """get root"""
        return self.root
    def set_root(self, root):
        """set root"""
        self.root = root
    def insert(self, data):
        """insert data"""
        if self.root is None:
            self.root = BSTNode()
            self.root.set_data(data)
        else:
            pointer = self.root
            while True:
                if data < pointer.get_data():
                    if pointer.get_left() is None:
                        p_new = BSTNode()
                        p_new.set_data(data)
                        pointer.set_left(p_new)
                        break
                    else:
                        pointer = pointer.get_left()
                elif data > pointer.get_data():
                    if pointer.get_right() is None:
                        p_new = BSTNode()
                        p_new.set_data(data)
                        pointer.set_right(p_new)
                        break
                    else:
                        pointer = pointer.get_right()
    def preorder(self, root):
        """preorder"""
        if root is not None:
            print("-> {}".format(root.get_data()), end=" ")
            self.preorder(root.get_left())
            self.preorder(root.get_right())

def main():
    """main here"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    print("Preorder: ", end="")
    my_bst.preorder(my_bst.get_root())
main()
