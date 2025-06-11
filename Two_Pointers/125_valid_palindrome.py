# List Comprehension
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join([ch for ch in s if ch.isalnum()]).lower()
        return filtered == filtered[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

# Two Pointer Solution  
  class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while(l < r):
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if(s[l].lower() != s[r].lower()):
                return False

            l += 1
            r -= 1
        
        return True
# Custom Alphanum
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while(l < r):
            while l < r and not self.alnum(s[l]):
                l += 1
            while r > l and not self.alnum(s[r]):
                r -= 1
            
            if(s[l].lower() != s[r].lower()):
                return False

            l += 1
            r -= 1
        
        return True

    def alnum(self, c):
            return ((ord('A') <= ord(c) <= ord('Z')) or
            (ord('a') <= ord(c) <= ord('z')) or
            (ord('0') <= ord(c) <= ord('9')))
