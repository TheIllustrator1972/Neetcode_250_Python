# O(n) Approach
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

# Modified Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # Left Portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # Right Sorted Portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
