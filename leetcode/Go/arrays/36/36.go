package main

func isValidSudoku(board [][]byte) bool {
	numbersRow := make(map[byte]struct{})
	numbersCol := make(map[byte]struct{})
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if board[j][i] == '.' {
				continue
			}
			// Iterate over a whole row and verify if a number is repeated
			if _, exists := numbersRow[board[i][j]]; exists {
				return false
			}
			numbersRow[board[i][j]] = struct{}{}
		}
		numbersRow = make(map[byte]struct{})

	}
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if board[j][i] == '.' {
				continue
			}
			// Iterate over a whole row and verify if a number is repeated
			if _, exists := numbersRow[board[j][i]]; exists {
				return false
			}
			numbersCol[board[j][i]] = struct{}{}
		}
		numbersCol = make(map[byte]struct{})
	}
	if !checkSubBoxes(board) {
		return false
	}
	return true
}

func checkSubBoxes(board [][]byte) bool {
	numbers := make(map[byte]struct{})
	// Iterating for all 9 subBoxes
	i, m := 0, 0
	for i < len(board) && m < len(board[0]) {
		for k := i; k < i+3; k++ {
			for j := m; j < m+3; j++ {
				if board[k][j] == '.' {
					continue
				}
				if _, exists := numbers[board[k][j]]; exists {
					return false
				}
				numbers[board[k][j]] = struct{}{}
			}
		}
		i = i + 3
		if i >= len(board) {
			m = m + 3
			i = 0
		}
		numbers = make(map[byte]struct{})
	}
	return true
}
