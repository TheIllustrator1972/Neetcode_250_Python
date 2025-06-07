class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
      return n + n

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums.append(nums[i])
        return nums

# More Extensible
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for j in range(len(nums)):
                ans.append(nums[j])
        return ans
