"Datanode"
class DataNode:
    """data-next setting"""
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """head-count setting"""
    def __init__(self):
        self.head = None
        self.count = 0

    def traverse(self):
        """traversal"""
        if not self.head:
            print("This is an empty list.")
            return

        current = self.head
        while current:
            print(current.data, end="")
            if current.next:
                print(" -> ", end="")
            current = current.next
        print()

    def insert_last(self, data):
        """last?"""
        new_node = DataNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.count += 1

    def insert_front(self, data):
        """front?"""
        new_node = DataNode(data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insert_before(self, node_data, data):
        """before?"""
        new_node = DataNode(data)

        if self.head.data == node_data:
            self.insert_front(data)
            return

        current = self.head
        while current.next and current.next.data != node_data:
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.count += 1

    def delete(self, data):
        """deleted"""
        if self.head.data == data:
            self.head = self.head.next
            self.count -= 1
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        current.next = current.next.next
        self.count -= 1

def main():
    """main"""
    mylist = SinglyLinkedList()
    for _ in range(int(input())):
        text = input()
        condition, data = text.split(": ")
        if condition == "F":
            mylist.insert_front(data)
        elif condition == "L":
            mylist.insert_last(data)
        # elif condition == "B":
        #     mylist.insert_before(*data.split(", "))
        # elif condition == "D":
        #     mylist.delete(data)
        else:
            print("Invalid Condition!")
    mylist.traverse()
main()
