# Sorting Approach
# nlog(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

# using a set
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for n in nums: 
            if(n in nums_set): 
                return True
            nums_set.add(n)
        return False

# Creating an element-freq map directly
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_map = Counter(nums)
    
        for _, count in my_map.items():
            if count > 1: 
                return True
        return False
