"""313"""
class BSTNode:
    """bst node"""
    def __init__(self):
        """init"""
        self.data = int(input())
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

def main():
    """main here"""
    p_new = BSTNode()
    print(p_new.get_data())
    print(p_new.get_left())
    print(p_new.get_right())
main()
