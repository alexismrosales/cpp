package main

func maxArea(height []int) int {
	p1, p2 := 0, len(height)-1
	max := 0
	for p1 < p2 {
		width := p2 - p1
		h := min(height[p1], height[p2])
		area := width * h
		if area > max {
			max = area
		}
		if height[p1] < height[p2] {
			p1++
		} else {
			p2--
		}
	}
	return max
}
