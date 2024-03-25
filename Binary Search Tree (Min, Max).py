"""KKK"""

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
    def is_empty(self):
        """is this bst empty"""
        return self.root is None
    def preorder(self, root):
        """preorder"""
        if root is not None:
            print("-> {}".format(root.get_data()), end=" ")
            self.preorder(root.get_left())
            self.preorder(root.get_right())
    def inorder(self, root):
        """inorder"""
        if root is not None:
            self.inorder(root.get_left())
            print("-> {}".format(root.get_data()), end=" ")
            self.inorder(root.get_right())
    def postorder(self, root):
        """postorder"""
        if root is not None:
            self.postorder(root.get_left())
            self.postorder(root.get_right())
            print("-> {}".format(root.get_data()), end=" ")
    def traverse(self):
        """traverse all type"""
        if self.is_empty():
            return print("This is an empty binary search tree.")
        print('Preorder: ', end='')
        self.preorder(self.get_root())
        print()
        print('Inorder: ', end='')
        self.inorder(self.get_root())
        print()
        print('Postorder: ', end='')
        self.postorder(self.get_root())
        print()
    def find_max(self):
        """find max"""
        pointer = self.root
        while pointer.get_right() is not None:
            pointer = pointer.get_right()
        return pointer.get_data()
    def find_min(self):
        """find min"""
        pointer = self.root
        while pointer.get_left() is not None:
            pointer = pointer.get_left()
        return pointer.get_data()

def main():
    """main here"""
    my_bst = BST()
    for _ in range(int(input())):
        my_bst.insert(int(input()))
    my_bst.traverse()
    print("Max:", my_bst.find_max())
    print("Min:", my_bst.find_min())
main()
