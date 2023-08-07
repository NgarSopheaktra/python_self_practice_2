class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

# Example usage
stack = Stack()
print (stack.push(5))
stack.push(10)
print(stack.pop())
print(stack.is_empty())