class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)

        leftProduct = 1
        rightProduct = 1

        for i in range(len(nums)):
            left[i] = leftProduct
            leftProduct = leftProduct * nums[i]

        for i in range(len(nums) - 1, -1, -1):
            right[i] = rightProduct
            rightProduct = rightProduct * nums[i]
            
        result = [left[i] * right[i] for i in range(len(left))]
        return result
