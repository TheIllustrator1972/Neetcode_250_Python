
# Reversing Approach
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        l , r = 0, len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l , r = 0, k - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l , r = k, len(nums) - 1

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

  # Reversing Shortened
          k = k % len(nums)
        nums.reverse()

        nums[0:k] = nums[0:k][::-1]
        nums[k:len(nums)] = nums[k:len(nums)][::-1]

# Modulus approach
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        ans = [0] * n
        for i in range(0, n):
            ans[(i + k) % n] = nums[i]

        nums[:] = ans

