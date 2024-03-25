"""Class std"""
class Student:
    """Student"""
    def __init__(self, std_id, name, gpa):
        """setter"""
        self.std_id = std_id
        self.name = name
        self.gpa = gpa
    def print_details(self):
        """print"""
        print("ID:", self.std_id)
        print("Name:", self.name)
        print("GPA: {:.2f}".format(self.gpa))
def main(text_in):
    """main"""
    import json
    std_in = json.loads(text_in)
    std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
    std.print_details()
main(input())
