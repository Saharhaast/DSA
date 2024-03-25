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
    def delete(self, data):
        """delete node"""
        if self.is_empty() is True:
            print("Delete Error, {} is not found in Binary Search Tree.".format(data))
            return None
        else:
            current = self.root
            prev = None
            while current is not None and data != current.get_data():
                prev = current
                if data < current.get_data():
                    current = current.get_left()
                else:
                    current = current.get_right()
            if current is None:
                print("Delete Error, {} is not found in Binary Search Tree.".format(data))
                return None
            elif current.get_left() is None and current.get_right() is None:
                if prev:
                    if prev.get_left() == current:
                        prev.set_left(None)
                    else:
                        prev.set_right(None)
                else:
                    self.root = None
            elif current.get_left() is not None and current.get_right() is None:
                child = current.get_left()
                if prev:
                    if prev.get_left() == current:
                        prev.set_left(child)
                    else:
                        prev.set_right(child)
                else:
                    self.root = child
            elif current.get_left() is None and current.get_right() is not None:
                child = current.get_right()
                if prev:
                    if prev.get_left() == current:
                        prev.set_left(child)
                    else:
                        prev.set_right(child)
                else:
                    self.root = child
            else:
                go_to_left = current.get_left()
                prev = current
                while go_to_left.get_right() is not None:
                    prev = go_to_left
                    go_to_left = go_to_left.get_right()
                replace = go_to_left.get_data()
                if prev.get_left() == go_to_left:
                    prev.set_left(go_to_left.get_left())
                else:
                    prev.set_right(go_to_left.get_left())
                current.set_data(replace)

def main():
    """main here"""
    my_bst = BST()
    while 1:
        text = input()
        if text == "Done":
            break
        condition, data = text.split(": ")
        if condition == "I":
            my_bst.insert(int(data))
        elif condition == "D":
            my_bst.delete(int(data))
        else:
            print("Invalid Condition")
    my_bst.traverse()
main()
