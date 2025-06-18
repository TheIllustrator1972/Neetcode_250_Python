class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(len(board)):
            for column in range(len(board[row])):
                currentChar = board[row][column]
                if currentChar == ".":
                    continue
                if currentChar in columns[column] or currentChar in rows[row] or currentChar in squares[(row // 3, column // 3)]:
                    return False
                columns[column].add(currentChar)
                rows[row].add(currentChar)
                squares[(row // 3, column // 3)].add(currentChar)
        
        return True
