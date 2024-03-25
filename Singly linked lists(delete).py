"""singly linked lists"""
class DataNode:
    """Delete"""
    def __init__(self, data=None):
        """Attribute"""
        self.__data = data
        self.__next = None
    def get_data(self):
        """return data"""
        return self.__data
    def set_data(self, data):
        """set new data"""
        self.__data = data
    def get_next(self):
        """return next"""
        return self.__next
    def set_next(self, _next):
        """set new next"""
        self.__next = _next

class SinglyLinkedList:
    """singly linked list"""
    def __init__(self):
        """init"""
        self.count = 0
        self.head = None

    def insert_last(self, data):
        """insert last"""
        pnew = DataNode(data)
        if self.head is None:
            self.head = pnew
        else:
            start = self.head
            while start.get_next() is not None:
                start = start.get_next()
            start.set_next(pnew)
        self.count += 1
    def insert_front(self, data):
        """insert front"""
        pnew = DataNode(data)
        pnew.set_next(self.head)
        self.head = pnew
        self.count += 1
    def insert_before(self, node, data):
        """insert before"""
        pnew = DataNode(data)
        if self.head is None:
            print("Cannot insert,", node, "does not exist.")
        elif self.head.get_data() == node:
            pnew.set_next(self.head)
            self.head = pnew
            self.count += 1
        else:
            start = self.head
            while start.get_next() and start.get_next().get_data() != node:
                start = start.get_next()
            if start.get_next() is None:
                print("Cannot insert,", node, "does not exist.")
            else:
                pnew.set_next(start.get_next())
                start.set_next(pnew)
    def traverse(self):
        """traverse"""
        if self.head is None:
            print("This is an empty list.")
        else:
            start = self.head
            while start.get_next() is not None:
                print(start.get_data(), end=" -> ")
                start = start.get_next()
            print(start.get_data())

    def delete(self, data):
        """delete node"""
        pdel = DataNode(data)
        if self.head is None:
            print("Cannot delete,", data, "does not exist.")
        elif self.head.get_data() == pdel.get_data():
            self.head = self.head.get_next()
        else:
            start = self.head
            while start.get_next() is not None and start.get_next().get_data() != pdel.get_data():
                start = start.get_next()
            if start.get_next() is None:
                print("Cannot delete,", data, "does not exist.")
            else:
                start.set_next(start.get_next().get_next())

def main():
    """main here"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        elif condition == "B":
            mylist.insert_before(*data.split(", "))
        elif condition == "D":
            mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()
main()
