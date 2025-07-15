class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = len(matrix) - 1

        def findNumInRow(row: int):
            l = 0
            r = len(matrix[row]) - 1
            while l <= r:
                midInRow = l + (r - l) // 2
                if matrix[row][midInRow] < target:
                    l = midInRow + 1
                elif matrix[row][midInRow] > target:
                    r = midInRow - 1
                else:
                    return True
            return False

        while l <= r:
            mid = (l + r) // 2 
            firstInRow = matrix[mid][0]
            
            if firstInRow <= target <= matrix[mid][-1]:
                return findNumInRow(mid)
            elif firstInRow > target:
                r = mid - 1
            else:
                l = mid + 1
    
        return False
