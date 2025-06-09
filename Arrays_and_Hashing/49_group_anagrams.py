# Initial Approach O (m * n log(n))
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myHash = defaultdict(list) # this calls a list() -> [] when a new element is accessed
        for s in strs: 
            key = tuple(sorted(s)) # ('s', 'b', 'c') tuple, immutable and hashable
            myHash[key].append(s)
            
        return list(myHash.values())


# More Efficient approach O(m * n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs: 
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
            
        return list(res.values())
