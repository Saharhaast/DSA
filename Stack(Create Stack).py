"""ArrayStack"""
class ArrayStack:
    """ArrayStack"""
    def __init__(self):
        """Setting Self"""
        self.size = 0
        self.data = []

    def push(self, input_data):
        """Push data onto the stack."""
        try:
            if input_data.isdigit():
                input_data = int(input_data)
            elif input_data.replace(".", "", 1).isdigit():
                input_data = float(input_data)
        except (TypeError, ValueError, ArithmeticError, AttributeError):
            pass
        finally:
            self.data.append(input_data)
            self.size += 1

    def pop(self):
        """Pop data from the stack."""
        if not self.is_empty():
            self.size -= 1
            return self.data.pop()
        else:
            print("Underflow: Cannot pop data from an empty list")
            return None

    def is_empty(self):
        """Check if the stack is empty."""
        return self.size == 0

    def get_stack_top(self):
        """Get the data at the top of the stack."""
        if not self.is_empty():
            return self.data[-1]
        else:
            print("Underflow: Cannot get stack top from an empty list")
            return None

    def get_size(self):
        """Get the size of the stack."""
        return self.size

    def print_stack(self):
        """Print the data in the stack."""
        print(self.data)


# ตัวอย่างการใช้งาน
STACK_ = ArrayStack()

STACK_.push("100")
STACK_.push(100)
STACK_.push("3.14")
STACK_.push(3.14)
STACK_.push("66.4a")
STACK_.push("Ackerman")

STACK_.print_stack()

print(STACK_.get_size())
VAR1_ = STACK_.pop()
print(VAR1_)
STACK_.print_stack()
print(STACK_.get_size())

while not STACK_.is_empty():
    print(STACK_.pop())

print()
print(STACK_.pop())
print(STACK_.get_stack_top())
print(VAR1_)
