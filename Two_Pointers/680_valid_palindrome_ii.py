# First Attempt Got TLE
class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            newString = s
            newString = newString[:i] + newString[i + 1:]
            if newString == newString[::-1]:
                return True
        
        return False

# Optimal Solution
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0 , len(s) - 1
        limit = 1

        while l < r:
            if s[l] != s[r]:
                skipL, skipR = s[l + 1: r + 1], s[l: r]
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l += 1
            r -= 1
        return True
