from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        exists = False
        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        def backtracking(i, j, wordIndex) -> bool:
            if board[i][j] != word[wordIndex]:
                return False
            if wordIndex == len(word):
                return True

            tmpVal = board[i][j]
            board[i][j] = "#"

            for direction in directions:
                x, y = direction
                x, y = x + i, y + j
                if  0 <= x < len(board) and  0 <= y < len(board[0]):
                    if backtracking(x, y, wordIndex+1):
                        return True

            board[i][j]= tmpVal
            return False 
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    exists = backtracking(i, j, 0)
                    if exists:
                        return True
                    
        return exists
        
