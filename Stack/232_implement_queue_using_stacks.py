class MyQueue:
    def __init__(self):
        self.s = []
        self.extra = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        while self.s:
            self.extra.append(self.s.pop())
        ans = self.extra[-1]
        self.extra.pop()
        while self.extra:
            self.s.append(self.extra.pop())
        return ans
        
    def peek(self) -> int:
        return self.s[0]

    def empty(self) -> bool:
        return len(self.s) == 0


#  O(1) Solution
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
        
    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2
