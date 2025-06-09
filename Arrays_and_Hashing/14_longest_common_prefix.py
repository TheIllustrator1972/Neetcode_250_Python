# Initial Approach
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = strs[0]

        for s in strs:
            i = 0
            while i < len(s) and i < len(commonPrefix) and s[i] == commonPrefix[i]:
                i += 1
            commonPrefix = commonPrefix[:i]

        return commonPrefix
