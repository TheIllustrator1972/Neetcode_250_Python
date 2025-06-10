# Sortin Approach  
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort() # in place sort
        return nums[len(nums) // 2]

# Hash Approach
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_map = Counter(nums)
        return max(my_map, key = my_map.get)

# Booyre Moore voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = None
        for n in nums:
            if count == 0:
                res = n
            count += 1 if res == n else -1
        return res
