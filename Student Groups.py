class ArrayStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

def distribute_students(groups, students):
    stack = ArrayStack()
    for student in students:
        stack.push(student)

    result = []

    for i in range(groups):
        current_group = []
        for j in range(len(students) // groups):
            current_group.append(stack.pop())
        result.append(current_group)

    for i in range(len(students) % groups):
        result[i].append(stack.pop())

    return result

def display_groups(groups):
    for i, group in enumerate(groups, start=1):
        print(f"Group {i}: {', '.join(group)}")

# Input
num_groups = int(input())
num_students = int(input())
student_names = [input() for _ in range(num_students)]

# Process
groups = distribute_students(num_groups, student_names)

# Output
display_groups(groups)
