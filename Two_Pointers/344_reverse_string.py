# Changing in place
class Solution:
    def reverseString(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

# Classic Two pointer
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1

# Slicing Assignment
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]

# Stack Solution
class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1


# Recursion
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(l , r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l + 1, r - 1)

        reverse(0, len(s) - 1)
