class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sumOfWeights = 0
        maxWeight = 0

        for num in weights:
            if num > maxWeight:
                maxWeight = num
            sumOfWeights += num
        
        l = maxWeight
        r = sumOfWeights

        def carryWeightsInShipOfSize(capacity: int) -> bool:
            days_needed = 1
            currentSum = 0
            for weight in weights:
                if currentSum + weight > capacity:
                    days_needed += 1
                    currentSum = weight
                else:
                    currentSum += weight
            return days_needed <= days

        res = 500
        while l <= r:
            mid = (l + r) // 2
            if carryWeightsInShipOfSize(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res
