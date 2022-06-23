
class MyStack:

    def __init__(self, stack = []):
        self.stack = stack

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        x = self.stack[-1]
        del self.stack[-1]
        return x

    def top(self) -> int:
        if self.empty():
            return -1
        else:
            return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
# obj.push(3)
# param_2 = obj.pop()
# param_3 = obj.top()
param_4 = obj.empty()
print(param_4)
