# Sorting 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Hashing
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Hash map approach
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        for ch in s:
            hashMap[ch] = hashMap.get(ch, 0) + 1
        
        for ch in t:
            hashMap[ch] = hashMap.get(ch, 0) - 1

        for freq in hashMap.values():
            if freq != 0:
                return False
        return True
