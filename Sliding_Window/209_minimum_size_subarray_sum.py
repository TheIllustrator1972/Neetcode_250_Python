# O (n) Approach

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0 , 0
        res = sys.maxsize
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return 0 if res == sys.maxsize else res

  # nlog(n)
  class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        prefixSums = [0] * (n + 1)

        for i in range(n):
            prefixSums[i + 1] = prefixSums[i] + nums[i]

        res = float('inf')
        for i in range(n):
            target_sum = prefixSums[i] + target
          # Gives the leftmost index where the prefix_sum[bound] ≥ prefix_sum[i] + target
            bound = bisect.bisect_left(prefixSums, target_sum)
            if bound <= n:
                res = min(res, bound - i)
        return 0 if res == float('inf') else res
