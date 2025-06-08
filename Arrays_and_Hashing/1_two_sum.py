# Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i , j]
        return []

# Checking while filling the hash
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {}
        for i in range(len(nums)):
            if target - nums[i] in myHash:
                return [i, myHash[target - nums[i]]]
            myHash[nums[i]] = i
        return []
