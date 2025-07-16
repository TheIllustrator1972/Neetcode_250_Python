class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0

        i = 0
        while i < len(nums) - 1 and nums[i] < nums[i + 1]:
            pivot += 1
            i += 1
        

        def binarySearchInRange(l: int, r: int):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1

        presentInLeft = binarySearchInRange(0 , pivot)
        if presentInLeft != -1:
            return presentInLeft

        presentInRight = binarySearchInRange(pivot + 1, len(nums) - 1)
        if presentInRight != -1: 
            return presentInRight
        return -1
