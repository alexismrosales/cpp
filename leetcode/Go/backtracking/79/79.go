package main

func exist(board [][]byte, word string) bool {
	exists := false
	var findWord func(x, y, wordIndex int)
	findWord = func(x, y, wordIndex int) {
		if wordIndex == len(word) {
			exists = true
			return
		}
		// If we are in the limits
		if x < 0 || x >= len(board) || y < 0 || y >= len(board[0]) || board[x][y] != word[wordIndex] {
			return
		}
		temp := board[x][y]
		// Setting a different value temporary
		board[x][y] = '#'
		// Up
		findWord(x, y+1, wordIndex+1)
		// Down
		findWord(x, y-1, wordIndex+1)
		// Left
		findWord(x-1, y, wordIndex+1)
		// Right
		findWord(x+1, y, wordIndex+1)
		board[x][y] = temp
	}
	for i := 0; i < len(board); i++ {
		for j := 0; j < len(board[0]); j++ {
			findWord(i, j, 0)
			if exists {
				return true
			}
		}
	}
	return exists
}
