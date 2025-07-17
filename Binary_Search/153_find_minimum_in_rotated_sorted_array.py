# Binary Search Approach
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        res = 5001

        while l <= r:
            if nums[l] <= nums[r]:
                res = min(res, nums[l])

            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return res
