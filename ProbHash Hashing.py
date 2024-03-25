"""class std"""
class Student:
    """student"""
    def __init__(self, std_id, name, gpa):
        """setter"""
        self.std_id = std_id
        self.name = name
        self.gpa = gpa

    def print_detail(self):
        """print"""
        print("ID:", self.std_id)
        print("Name:", self.name)
        print("GPA: {:.2f}".format(self.gpa))

class ProbHash:
    """hashing"""
    def __init__(self, size):
        """setter"""
        self.hash_table = [None] * size
        self.size = size

    def hash(self, key):
        """hash"""
        return key % self.size

    def rehash(self, hkey):
        """rehash"""
        return (hkey + 1) % self.size

    def insert_data(self, student):
        """insert"""
        hkey = self.hash(student.std_id)
        if self.hash_table[hkey] is None:
            self.hash_table[hkey] = student
            print("Insert {} at index {}".format(student.std_id, hkey))
        else:
            index = hkey
            while self.hash_table[index] is not None:
                index = self.rehash(index)
                if index == hkey:
                    print("The list is full. {} could not be inserted.".format(student.std_id))
                    return
            self.hash_table[index] = student
            print("Insert {} at index {}".format(student.std_id, index))

    def search_data(self, std_id):
        """search"""
        hkey = self.hash(std_id)
        index = hkey
        while self.hash_table[index] is not None:
            if self.hash_table[index].std_id == std_id:
                print("Found {} at index {}".format(std_id, index))
                return self.hash_table[index]
            index = self.rehash(index)
            if index == hkey:
                break
        print("{} does not exist.".format(std_id))
        return None

def main():
    """main"""
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_detail()
            print("------")
        else:
            print("Invalid Condition!")

main()
