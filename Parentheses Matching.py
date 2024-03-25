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
            return "Underflow: Cannot pop data from an empty list"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def is_parentheses_matching(expression):
    stack = ArrayStack()

    for char in expression:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.is_empty():
                return False
            else:
                stack.pop()

    return stack.is_empty()

# ตัวอย่างการเรียกใช้ฟังก์ชัน
expression = input()
result = is_parentheses_matching(expression)

if result:
    print("Parentheses in", expression, "are matched")
else:
    print("Parentheses in", expression, "are unmatched")

print(result)
