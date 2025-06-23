class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currentSum = 0
        prefixSumsToCountMap = {0:1}

        for num in nums:
            currentSum += num
            difference = currentSum - k
            res += prefixSumsToCountMap.get(difference, 0)
            prefixSumsToCountMap[currentSum] = 1 + prefixSumsToCountMap.get(currentSum, 0)

        return res
