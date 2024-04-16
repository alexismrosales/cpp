package main

func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}
	zigzag := ""
	sum := 0
	toJump := numRows - 1
	// We will jump to the numRows + numRows-1 pos, n times if the array location exists
	for range len(s) {
		if sum <= numRows-1 {
			zigzag += string(s[sum])
			sum = toJump
		} else {
			sum = 0
		}
	}
	return zigzag
}
